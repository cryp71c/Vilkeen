import os
import main

# Upgrade pip and install requirements.txt
try:
    os.system("python -m pip install -r requirements.txt")
    os.system("python -m pip install --upgrade pip")
except:
    print("There was an error installing the required python packages.")

if __name__ == '__main__':
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    main.main()
