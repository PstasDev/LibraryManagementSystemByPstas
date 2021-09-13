#Importing additonal libraries/services
import os.path
import os
import sys
import time
import json
import urllib.request
import base64
import logging
import datetime

#Setup logging
isLogsDirExists = os.path.isdir("./Logs")
if isLogsDirExists == True:
	logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S', filename='Logs/setup.log', encoding='utf-8', level=logging.DEBUG)
else:
	os.mkdir("Logs")
	logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S', filename='Logs/setup.log', encoding='utf-8', level=logging.DEBUG)

currentversion = 202108221750

window = os.get_terminal_size()
autoscreenwidth = window[0]
autoscreenheight = window[1]

RED_FORMAT = "\033[0;31;40m"
RED_BG_FORMAT = "\033[0;37;41m"
GREEN_FORMAT = "\033[0;32;40m"
GREEN_BG_FORMAT = "\033[0;37;42m"
BASIC_FORMAT = "\033[0;37;40m"
WHITE_BG_FORMAT = "\033[0;30;47m"

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

print(".")
cls()

screenwidth = autoscreenwidth

if int(screenwidth) < 120:
	print("Your screen size is too small to run the software")
	time.sleep(2)
	cls()
	exit()
else:
	pass
maxlength = float(screenwidth) - 2

cls()
window = os.get_terminal_size()
autoscreenwidth = window[0]
autoscreenheight = window[1]
screenwidth = autoscreenwidth

if int(screenwidth) < 120:
	print("Your screen size is too small to run the software")
	time.sleep(2)
	cls()
	exit()
else:
	pass
maxlength = float(screenwidth) - 2
outputchkble = "Library Management System - setup.py"
outputchkble = " " + outputchkble + " "
lenochkble = len(outputchkble)
if (lenochkble % 2) == 0:
	txtisodd = False
else:
	txtisodd = True

if txtisodd == False:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "
else:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = spaces1 + 1
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "

header = "\033[1;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[1;37;40m" + spaces2 + "]"
print(header)
print("")

time.sleep(1.55)

print("Checking main file exsits...")
ifMainFileExists = os.path.exists('./main.py')
if ifMainFileExists == True:
	print("Success")
	time.sleep(0.25)
	pass
else:
	print("\033[0;37;41mNecessary file missing. Please try to download again the repository!\033[1;37;40m")
	time.sleep(5)
	cls()
	exit()
cls()

window = os.get_terminal_size()
autoscreenwidth = window[0]
autoscreenheight = window[1]
screenwidth = autoscreenwidth

if int(screenwidth) < 120:
	print("Your screen size is too small to run the software")
	time.sleep(2)
	cls()
	exit()
else:
	pass
maxlength = float(screenwidth) - 2
outputchkble = "Library Management System - setup.py"
outputchkble = " " + outputchkble + " "
lenochkble = len(outputchkble)
if (lenochkble % 2) == 0:
	txtisodd = False
else:
	txtisodd = True

if txtisodd == False:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "
else:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = spaces1 + 1
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "

header = "\033[1;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[1;37;40m" + spaces2 + "]"
print(header)
print("")

try:
	f = "https://api.npoint.io/625d776fd852e28204a0"
	with urllib.request.urlopen(f) as url:
		data = json.loads(url.read().decode())

	if data["thistask"] == "check_latest":
		if data["latest_version"] == currentversion:
			print("You have the latest version of the software!")
			time.sleep(0.75)
		elif data["latest_version"] > currentversion:
			print("A newer version is available for the software. If you want to install it, please follow the instructions at this link below")
			print("https://github.com/BallaBotond/LibraryManagementSystemByPstas/wiki/Updating-the-Software")
			time.sleep(7)
		else:
			pass
	else:
		pass
except Exception as exceptFromCode:
	print("\033[0;37;41mCan't check the latest version. Check the Troubleshooting manual below:\033[1;37;40m")
	print("https://github.com/BallaBotond/LibraryManagementSystemByPstas/wiki/Internet-Troubleshooting-Manual-if-the-software-can't-reach-a-server")
	logging.error(exceptFromCode)
	time.sleep(3)
cls()

window = os.get_terminal_size()
autoscreenwidth = window[0]
autoscreenheight = window[1]
screenwidth = autoscreenwidth

if int(screenwidth) < 120:
	print("Your screen size is too small to run the software")
	time.sleep(2)
	cls()
	exit()
else:
	pass
maxlength = float(screenwidth) - 2
outputchkble = "Library Management System - setup.py - Last Verification"
outputchkble = " " + outputchkble + " "
lenochkble = len(outputchkble)
if (lenochkble % 2) == 0:
	txtisodd = False
else:
	txtisodd = True

if txtisodd == False:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "
else:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = spaces1 + 1
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "

header = "\033[1;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[1;37;40m" + spaces2 + "]"
print(header)
print("")

print("If you want to install the software now")
time.sleep(1.5)
print(f"{RED_FORMAT}WARNING! IF YOU REINSTALLING THE SOFTWARE PLEASE MAKE SURE, YOU HAVE A RECOVERY SAVE OF THE 'Saves' FOLDER!{BASIC_FORMAT}")
print("Think about it... If you don't want to install the software, close the window (5)")
time.sleep(1)
cls()

window = os.get_terminal_size()
autoscreenwidth = window[0]
autoscreenheight = window[1]
screenwidth = autoscreenwidth

if int(screenwidth) < 120:
	print("Your screen size is too small to run the software")
	time.sleep(2)
	cls()
	exit()
else:
	pass
maxlength = float(screenwidth) - 2
outputchkble = "Library Management System - setup.py - Last Verification"
outputchkble = " " + outputchkble + " "
lenochkble = len(outputchkble)
if (lenochkble % 2) == 0:
	txtisodd = False
else:
	txtisodd = True

if txtisodd == False:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "
else:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = spaces1 + 1
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "

header = "\033[1;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[1;37;40m" + spaces2 + "]"
print(header)
print("")

print("If you want to install the software now")
print(f"{RED_FORMAT}WARNING! IF YOU REINSTALLING THE SOFTWARE PLEASE MAKE SURE, YOU HAVE A RECOVERY SAVE OF THE 'Saves' FOLDER!{BASIC_FORMAT}")
print("Think about it... If you don't want to install the software, close the window (4)")
time.sleep(1)
cls()

window = os.get_terminal_size()
autoscreenwidth = window[0]
autoscreenheight = window[1]
screenwidth = autoscreenwidth

if int(screenwidth) < 120:
	print("Your screen size is too small to run the software")
	time.sleep(2)
	cls()
	exit()
else:
	pass
maxlength = float(screenwidth) - 2
outputchkble = "Library Management System - setup.py - Last Verification"
outputchkble = " " + outputchkble + " "
lenochkble = len(outputchkble)
if (lenochkble % 2) == 0:
	txtisodd = False
else:
	txtisodd = True

if txtisodd == False:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "
else:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = spaces1 + 1
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "

header = "\033[1;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[1;37;40m" + spaces2 + "]"
print(header)
print("")

print("If you want to install the software now")
print(f"{RED_FORMAT}WARNING! IF YOU REINSTALLING THE SOFTWARE PLEASE MAKE SURE, YOU HAVE A RECOVERY SAVE OF THE 'Saves' FOLDER!{BASIC_FORMAT}")
print("Think about it... If you don't want to install the software, close the window (3)")
time.sleep(1)
cls()

window = os.get_terminal_size()
autoscreenwidth = window[0]
autoscreenheight = window[1]
screenwidth = autoscreenwidth

if int(screenwidth) < 120:
	print("Your screen size is too small to run the software")
	time.sleep(2)
	cls()
	exit()
else:
	pass
maxlength = float(screenwidth) - 2
outputchkble = "Library Management System - setup.py - Last Verification"
outputchkble = " " + outputchkble + " "
lenochkble = len(outputchkble)
if (lenochkble % 2) == 0:
	txtisodd = False
else:
	txtisodd = True

if txtisodd == False:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "
else:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = spaces1 + 1
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "

header = "\033[1;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[1;37;40m" + spaces2 + "]"
print(header)
print("")

print("If you want to install the software now")
print(f"{RED_FORMAT}WARNING! IF YOU REINSTALLING THE SOFTWARE PLEASE MAKE SURE, YOU HAVE A RECOVERY SAVE OF THE 'Saves' FOLDER!{BASIC_FORMAT}")
print("Think about it... If you don't want to install the software, close the window (2)")
time.sleep(1)
cls()

window = os.get_terminal_size()
autoscreenwidth = window[0]
autoscreenheight = window[1]
screenwidth = autoscreenwidth

if int(screenwidth) < 120:
	print("Your screen size is too small to run the software")
	time.sleep(2)
	cls()
	exit()
else:
	pass
maxlength = float(screenwidth) - 2
outputchkble = "Library Management System - setup.py - Last Verification"
outputchkble = " " + outputchkble + " "
lenochkble = len(outputchkble)
if (lenochkble % 2) == 0:
	txtisodd = False
else:
	txtisodd = True

if txtisodd == False:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "
else:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = spaces1 + 1
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "

header = "\033[1;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[1;37;40m" + spaces2 + "]"
print(header)
print("")

print("If you want to install the software now")
print(f"{RED_FORMAT}WARNING! IF YOU REINSTALLING THE SOFTWARE PLEASE MAKE SURE, YOU HAVE A RECOVERY SAVE OF THE 'Saves' FOLDER!{BASIC_FORMAT}")
print("Think about it... If you don't want to install the software, close the window (1)")
time.sleep(1)
cls()

window = os.get_terminal_size()
autoscreenwidth = window[0]
autoscreenheight = window[1]
screenwidth = autoscreenwidth

if int(screenwidth) < 120:
	print("Your screen size is too small to run the software")
	time.sleep(2)
	cls()
	exit()
else:
	pass
maxlength = float(screenwidth) - 2
outputchkble = "Library Management System - setup.py - Last Verification"
outputchkble = " " + outputchkble + " "
lenochkble = len(outputchkble)
if (lenochkble % 2) == 0:
	txtisodd = False
else:
	txtisodd = True

if txtisodd == False:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "
else:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = spaces1 + 1
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "

header = "\033[1;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[1;37;40m" + spaces2 + "]"
print(header)
print("")

print(f"{RED_FORMAT}WARNING! You now want to install the software, but in some cases, the older saves are not available for the newer!{BASIC_FORMAT}\n")
print("If you now want to install, press ENTER")
time.sleep(0.75)
enterConfirm = input("And if you don't, close the window")
cls()

window = os.get_terminal_size()
autoscreenwidth = window[0]
autoscreenheight = window[1]
screenwidth = autoscreenwidth

if int(screenwidth) < 120:
	print("Your screen size is too small to run the software")
	time.sleep(2)
	cls()
	exit()
else:
	pass
maxlength = float(screenwidth) - 2
outputchkble = "Library Management System - setup.py - Installing... (1/4)"
outputchkble = " " + outputchkble + " "
lenochkble = len(outputchkble)
if (lenochkble % 2) == 0:
	txtisodd = False
else:
	txtisodd = True

if txtisodd == False:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "
else:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = spaces1 + 1
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "

header = "\033[1;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[1;37;40m" + spaces2 + "]"
print(header)
print("")

print("Installing in: 5")
time.sleep(1)
cls()

window = os.get_terminal_size()
autoscreenwidth = window[0]
autoscreenheight = window[1]
screenwidth = autoscreenwidth

if int(screenwidth) < 120:
	print("Your screen size is too small to run the software")
	time.sleep(2)
	cls()
	exit()
else:
	pass
maxlength = float(screenwidth) - 2
outputchkble = "Library Management System - setup.py - Installing... (1/4)"
outputchkble = " " + outputchkble + " "
lenochkble = len(outputchkble)
if (lenochkble % 2) == 0:
	txtisodd = False
else:
	txtisodd = True

if txtisodd == False:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "
else:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = spaces1 + 1
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "

header = "\033[1;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[1;37;40m" + spaces2 + "]"
print(header)
print("")

print("Installing in: 4")
time.sleep(1)
cls()

window = os.get_terminal_size()
autoscreenwidth = window[0]
autoscreenheight = window[1]
screenwidth = autoscreenwidth

if int(screenwidth) < 120:
	print("Your screen size is too small to run the software")
	time.sleep(2)
	cls()
	exit()
else:
	pass
maxlength = float(screenwidth) - 2
outputchkble = "Library Management System - setup.py - Installing... (1/4)"
outputchkble = " " + outputchkble + " "
lenochkble = len(outputchkble)
if (lenochkble % 2) == 0:
	txtisodd = False
else:
	txtisodd = True

if txtisodd == False:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "
else:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = spaces1 + 1
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "

header = "\033[1;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[1;37;40m" + spaces2 + "]"
print(header)
print("")

print("Installing in: 3")
time.sleep(1)
cls()

window = os.get_terminal_size()
autoscreenwidth = window[0]
autoscreenheight = window[1]
screenwidth = autoscreenwidth

if int(screenwidth) < 120:
	print("Your screen size is too small to run the software")
	time.sleep(2)
	cls()
	exit()
else:
	pass
maxlength = float(screenwidth) - 2
outputchkble = "Library Management System - setup.py - Installing... (1/4)"
outputchkble = " " + outputchkble + " "
lenochkble = len(outputchkble)
if (lenochkble % 2) == 0:
	txtisodd = False
else:
	txtisodd = True

if txtisodd == False:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "
else:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = spaces1 + 1
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "

header = "\033[1;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[1;37;40m" + spaces2 + "]"
print(header)
print("")

print("Installing in: 2")
time.sleep(1)
cls()

window = os.get_terminal_size()
autoscreenwidth = window[0]
autoscreenheight = window[1]
screenwidth = autoscreenwidth

if int(screenwidth) < 120:
	print("Your screen size is too small to run the software")
	time.sleep(2)
	cls()
	exit()
else:
	pass
maxlength = float(screenwidth) - 2
outputchkble = "Library Management System - setup.py - Installing... (1/4)"
outputchkble = " " + outputchkble + " "
lenochkble = len(outputchkble)
if (lenochkble % 2) == 0:
	txtisodd = False
else:
	txtisodd = True

if txtisodd == False:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "
else:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = spaces1 + 1
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "

header = "\033[1;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[1;37;40m" + spaces2 + "]"
print(header)
print("")

print("Installing in: 1")
time.sleep(1)
cls()

window = os.get_terminal_size()
autoscreenwidth = window[0]
autoscreenheight = window[1]
screenwidth = autoscreenwidth

if int(screenwidth) < 120:
	print("Your screen size is too small to run the software")
	time.sleep(2)
	cls()
	exit()
else:
	pass
maxlength = float(screenwidth) - 2
outputchkble = "Library Management System - setup.py - Installing... (1/4)"
outputchkble = " " + outputchkble + " "
lenochkble = len(outputchkble)
if (lenochkble % 2) == 0:
	txtisodd = False
else:
	txtisodd = True

if txtisodd == False:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "
else:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = spaces1 + 1
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "

header = "\033[1;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[1;37;40m" + spaces2 + "]"
print(header)
print("")

print("Installing...")
time.sleep(1)

print(f"{BASIC_FORMAT}Checking available folders (./Assets)")
isAssetsDirExsits = os.path.isdir("./Assets")
print(f"{BASIC_FORMAT}Checking available folders (./Assets/Saves)")
isAssetsDownSavesDirExists = os.path.isdir("./Assets/Saves")
print(f"{BASIC_FORMAT}Checking available folders (./Assets/ProgramData)")
isAssestDownProgramDataDirExists = os.path.isdir("./Assets/ProgramData")

cls()

window = os.get_terminal_size()
autoscreenwidth = window[0]
autoscreenheight = window[1]
screenwidth = autoscreenwidth

if int(screenwidth) < 120:
	print("Your screen size is too small to run the software")
	time.sleep(2)
	cls()
	exit()
else:
	pass
maxlength = float(screenwidth) - 2
outputchkble = "Library Management System - setup.py - Installling... (2/4)"
outputchkble = " " + outputchkble + " "
lenochkble = len(outputchkble)
if (lenochkble % 2) == 0:
	txtisodd = False
else:
	txtisodd = True

if txtisodd == False:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "
else:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = spaces1 + 1
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "

header = "\033[1;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[1;37;40m" + spaces2 + "]"
print(header)
print("")

if isAssetsDirExsits == True:
	print(f"{GREEN_FORMAT}Checking available folders (./Assets){BASIC_FORMAT}")
else:
	print(f"{RED_FORMAT}Checking available folders (./Assets){BASIC_FORMAT}")
	os.mkdir("Assets")
if isAssetsDownSavesDirExists == True:
	print(f"{GREEN_FORMAT}Checking available folders (./Assets/Saves){BASIC_FORMAT}")
else:
	print(f"{RED_FORMAT}Checking available folders (./Assets/Saves){BASIC_FORMAT}")
	os.mkdir("Assets/Saves")
if isAssestDownProgramDataDirExists == True:
	print(f"{GREEN_FORMAT}Checking available folders (./Assets/ProgramData){BASIC_FORMAT}")
else:
	print(f"{RED_FORMAT}Checking available folders (./Assets/ProgramData){BASIC_FORMAT}")
	os.mkdir("Assets/ProgramData")
time.sleep(2)

cls()

window = os.get_terminal_size()
autoscreenwidth = window[0]
autoscreenheight = window[1]
screenwidth = autoscreenwidth

if int(screenwidth) < 120:
	print("Your screen size is too small to run the software")
	time.sleep(2)
	cls()
	exit()
else:
	pass
maxlength = float(screenwidth) - 2
outputchkble = "Library Management System - setup.py - Installling... (3/4)"
outputchkble = " " + outputchkble + " "
lenochkble = len(outputchkble)
if (lenochkble % 2) == 0:
	txtisodd = False
else:
	txtisodd = True

if txtisodd == False:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "
else:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = spaces1 + 1
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "

header = "\033[1;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[1;37;40m" + spaces2 + "]"
print(header)
print("")

print(f"{GREEN_FORMAT}Checking available folders (./Assets){BASIC_FORMAT}")
print(f"{GREEN_FORMAT}Checking available folders (./Assets/Saves){BASIC_FORMAT}")
print(f"{GREEN_FORMAT}Checking available folders (./Assets/ProgramData){BASIC_FORMAT}")
try:
	file = open("Assets/ProgramData/installverification.ver", "w+")
	file.write("Installed Successfully")
	file.write(datetime.datetime())
	file.close()
except:
	pass

time.sleep(2)

cls()

window = os.get_terminal_size()
autoscreenwidth = window[0]
autoscreenheight = window[1]
screenwidth = autoscreenwidth

if int(screenwidth) < 120:
	print("Your screen size is too small to run the software")
	time.sleep(2)
	cls()
	exit()
else:
	pass
maxlength = float(screenwidth) - 2
outputchkble = "Library Management System - setup.py - Installed Successfully (4/4)"
outputchkble = " " + outputchkble + " "
lenochkble = len(outputchkble)
if (lenochkble % 2) == 0:
	txtisodd = False
else:
	txtisodd = True

if txtisodd == False:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "
else:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = spaces1 + 1
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "

header = "\033[1;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[1;37;40m" + spaces2 + "]"
print(header)
print("")

print(f"{BASIC_FORMAT}Installed Successfully!")

cls()

window = os.get_terminal_size()
autoscreenwidth = window[0]
autoscreenheight = window[1]
screenwidth = autoscreenwidth

if int(screenwidth) < 120:
	print("Your screen size is too small to run the software")
	time.sleep(2)
	cls()
	exit()
else:
	pass
maxlength = float(screenwidth) - 2
outputchkble = "Library Management System - setup.py - Installed Successfully"
outputchkble = " " + outputchkble + " "
lenochkble = len(outputchkble)
if (lenochkble % 2) == 0:
	txtisodd = False
else:
	txtisodd = True

if txtisodd == False:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "
else:
	osztando = maxlength - lenochkble
	spaces1 = osztando / 2
	spaces2 = osztando / 2
	spaces1 = spaces1 + 1
	spaces1 = int(spaces1) * " "
	spaces2 = int(spaces2) * " "

header = "\033[1;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[1;37;40m" + spaces2 + "]"
print(header)
print("")

print(f"{GREEN_FORMAT}Installed Successfully!{BASIC_FORMAT}")
print(f"{BASIC_FORMAT}Now you can close the Window, and start the software, same like this (main.py)")
time.sleep(5)