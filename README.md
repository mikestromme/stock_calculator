# make exe

pip install pyinstaller
pyinstaller --onefile your_script_name.py


# hide cmd window
#!/bin/bash
./your_executable_name.exe > /dev/null 2>&1 &

bash launch.sh
