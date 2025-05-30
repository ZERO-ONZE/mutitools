# Copyright (c) Azuna
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.


try:
    import sys
    import os

    
    if sys.platform.startswith("win"):
        os.system("cls")
        print("Installing the python modules required for the Azuna Tool:\n")
        os.system("python -m pip install --upgrade pip")
        os.system("python -m pip install -r requirements.txt")
        os.system("python Azuna.py")

    elif sys.platform.startswith("linux"):
        os.system("clear")
        print("Installing the python modules required for the Azuna Tool:\n")
        os.system("pip3 install --upgrade pip")
        os.system("pip3 install -r requirements.txt")
        OpenTelegram()
        os.system("python3 Azuna.py")

except Exception as e:
    input(e)