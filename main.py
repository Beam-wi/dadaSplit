# encoding:utf-8

import os
import cv2
import math

from datetime import datetime
import random


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

while True:
    mode = input(f"请选则业务名称，数据分离（输入：1）、数据合并（输入：2）、退出（输入：q）：")
    if mode == "1":
        while True:
            img_path_in = input(f"请输入需要分离的数据集路径(按 q 返回上一层)：")
            if not os.path.exists(img_path_in) and img_path_in != "q" and img_path_in != "Q" :
                continue
            elif img_path_in == "q" or img_path_in == "Q":
                break
            else:
                while True:
                    num_min = input(f"请输入需要区分的最小数量(按 q 返回上一层)：")
                    # if isinstance(num_min, int) and num_min > 0:
                    if is_number(num_min):
                        num_min_ = int(num_min)
                        data_num = len(os.listdir(img_path_in))
                        if 0 < num_min_ < data_num:
                            print("正在进行中...")
                            now_time = datetime.strftime(datetime.now(), "%Y%m%d-%H%M%S")
                            img_path_out = f"{img_path_in[:-1]}-{now_time}" if img_path_in[-1] == "/" else f"{img_path_in}-{now_time}"
                            os.makedirs(img_path_out)
                            sing_path_list = os.listdir(img_path_in)
                            random.shuffle(sing_path_list)
                            for i in range(math.ceil(len(sing_path_list)/num_min_)):
                                write_list = sing_path_list[i*num_min_: (i+1)*num_min_]
                                if not os.path.exists(f"{img_path_out}/{i}"):
                                    os.makedirs(f"{img_path_out}/{i}")
                                for j, sing_name in enumerate(write_list):
                                    image = cv2.imread(f"{img_path_in}/{sing_name}")
                                    cv2.imwrite(f"{img_path_out}/{i}/{sing_name}", image)
                            print(f"已完成,写入路径为：{img_path_out}")
                            img_path_in = "q"
                            break
                        else:
                            print("输入图片数量超出图片总数！")
                            continue
                    elif num_min == "q" or num_min == "Q":
                        break
                    else:
                        continue
            if img_path_in == "q":
                break

    elif mode == "2":
        while True:
            img_path_in = input(f"请输入需要合并的数据集路径(按 q 返回上一层)：")
            if not os.path.exists(img_path_in) and img_path_in != "q" and img_path_in != "Q":
                continue
            elif img_path_in == "q" or img_path_in == "Q":
                break
            else:
                print("正在进行中...")
                now_time = datetime.strftime(datetime.now(), "%Y%m%d-%H%M%S")
                img_path_new = f"{img_path_in[:-1]}-{now_time}" if img_path_in[-1] == "/" else f"{img_path_in}-{now_time}"
                if not os.path.exists(img_path_new):
                    os.makedirs(img_path_new)
                dataset = list()
                name_dir_list = list()
                for x in os.listdir(img_path_in):
                    if "." not in x:
                        name_dir_list.append(f"{img_path_in}/{x}")
                    else:
                        continue
                for ii, sing_dir in enumerate(name_dir_list):
                    img_name_list = list()
                    for sing_img_name in os.listdir(sing_dir):
                        if ".jpg" in sing_img_name or ".png" in sing_img_name:
                            img_name_list.append(f"{sing_dir}/{sing_img_name}")
                        else:
                            continue
                    dataset.extend(img_name_list)
                for sing_img_path in dataset:
                    image_ = cv2.imread(sing_img_path)
                    sing_img_out = f"{img_path_new}/{sing_img_path.split('/')[-1]}"
                    cv2.imwrite(sing_img_out, image_)
                print(f"已完成,写入路径为：{img_path_new}")
                break
    elif mode == "q" or mode == "Q":
        break
    else:
        while True:
            again = input(f"业务名称选则错误！是否重新选则（y/n）:")
            if again == "Y" or again == "y" or again == "yes" or again == "YES" or again == "Yes":
                break
            elif again == "N" or again == "n" or again == "no" or again == "No" or again == "NO":
                quit()



