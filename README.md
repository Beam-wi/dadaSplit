## dadaSplit

### dependencies

* python3.6
* pyinstaller==4.1
* numpy==1.16.4
* opencv-python==3.3.1

### Win install

Turn .py to .exe.

    cd Path~/main.py
    pyinstaller -F -i favicon.ico main.py
    
Run .exe
    
    cd ./dist
    double click main.exe


### Linux

    cd Path~/main.py
    chmod u+x ./main.py
