#Importing additonal libraries/services
import os.path
import os
import sys
import time
import json
import urllib.request
import base64
import logging
import getpass

#Setup logging
isLogsDirExists = os.path.isdir("./Logs")
if isLogsDirExists == True:
	logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S', filename='Logs/main.log', encoding='utf-8', level=logging.DEBUG)
else:
	os.mkdir("Logs")
	logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S', filename='Logs/main.log', encoding='utf-8', level=logging.DEBUG)

currentversion = 202107051546

window = os.get_terminal_size()
autoscreenwidth = window[0]
autoscreenheight = window[1]

RED_FORMAT = "\033[0;31;40m"
RED_BG_FORMAT = "\033[0;37;41m"
GREEN_FORMAT = "\033[0;32;40m"
GREEN_BG_FORMAT = "\033[0;30;42m"
GREEN_BRIGHT_FORMAT = "\033[1;32;40m"
BASIC_FORMAT = "\033[0;37;40m"
BRIGHT_FORMAT = "\033[1;37;40m"
WHITE_BG_FORMAT = "\033[0;30;47m"
GREY_FORMAT = "\033[0;37;90m"

#permissions
allPerms = ["Administrator", "terminal", "users", "database"]
permsToAccessUsersmenu = ["Administrator", "users"]
permsToAccessTerminalmenu = ["Administrator", "terminal"]
permsToAccessDatabasemenu = ["Administrator", "database"]

mainAdminData = """
{"administrators": ["admin"], "adminpasswords": ["YMRtaW4"]}
"""

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
outputchkble = "Library Management System"
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

header = "\033[0;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[0;37;40m" + spaces2 + "]"
print(header)
print("")

isInstallVerificationFileExists = os.path.exists("./Assets/ProgramData/installverification.ver")
if isInstallVerificationFileExists == True:
	print("Verification Successful")
	time.sleep(0.5)
else:
	print("The Verification was not Successful. Please try to install the software, with the setup.py")
	print("Detailed information about the installation:")
	print("https://github.com/BallaBotond/LibraryManagementSystemByPstas/wiki/Installing-the-Software")
	time.sleep(10)
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
outputchkble = "Library Management System"
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

header = "\033[0;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[0;37;40m" + spaces2 + "]"
print(header)
print("")
print("")
print("")
print("")
print("")
maxlength = float(screenwidth)
outputchkble = "Welcome to the Library Management System"
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

centeredLine = "\033[1;37;40m" + spaces1 + outputchkble + spaces2
print(centeredLine)

time.sleep(1)
# print("")
# maxlength = float(screenwidth) - 2
# outputchkble = "This is your screen size"
# outputchkble = " " + outputchkble + " "
# lenochkble = len(outputchkble)
# if (lenochkble % 2) == 0:
# 	txtisodd = False
# else:/
# 	txtisodd = True

# if txtisodd == False:
# 	osztando = maxlength - lenochkble
# 	spaces1 = osztando / 2
# 	spaces2 = osztando / 2
# 	spaces1 = int(spaces1) * "-"
# 	spaces2 = int(spaces2) * "-"
# else:
# 	osztando = maxlength - lenochkble
# 	spaces1 = osztando / 2
# 	spaces2 = osztando / 2
# 	spaces1 = spaces1 + 1
# 	spaces1 = int(spaces1) * "-"
# 	spaces2 = int(spaces2) * "-"

# centeredLine = "\033[0;37;40m<" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[0;37;40m" + spaces2 + ">"
# print(centeredLine)
# time.sleep(1)
# maxlength = float(screenwidth) - 2
# outputchkble = "When this size shrinks under 120 character, the program will be closed automatically at the next window-refresh"
# outputchkble = " " + outputchkble + " "
# lenochkble = len(outputchkble)
# if (lenochkble % 2) == 0:
# 	txtisodd = False
# else:
# 	txtisodd = True

# if txtisodd == False:
# 	osztando = maxlength - lenochkble
# 	spaces1 = osztando / 2
# 	spaces2 = osztando / 2
# 	spaces1 = int(spaces1) * "-"
# 	spaces2 = int(spaces2) * "-"
# else:
# 	osztando = maxlength - lenochkble
# 	spaces1 = osztando / 2
# 	spaces2 = osztando / 2
# 	spaces1 = spaces1 + 1
# 	spaces1 = int(spaces1) * "-"
# 	spaces2 = int(spaces2) * "-"

# centeredLine = "\033[0;37;40m<" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[0;37;40m" + spaces2 + ">"
# print(centeredLine)
# time.sleep(2)
while True:
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
	outputchkble = "Library Management System"
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
	
	header = "\033[0;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[0;37;40m" + spaces2 + "]"
	print(header)
	
	maxlength = float(screenwidth)
	outputchkble = "Checking users and its status..."
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
	
	centeredLine = "\033[0;37;40m" + spaces1 + outputchkble + spaces2
	print(centeredLine)
	
	isAssetsDownUsersDirExists = os.path.isdir("./Assets/Users")
	if isAssetsDownUsersDirExists == True:
		isAdminUsersFileExists = os.path.exists("./Assets/Users/adminusers.lms")
		if isAdminUsersFileExists == True:
			with open('Assets/Users/adminusers.lms') as adminUsersRawFile:
				adminUsersRawJSON = json.load(adminUsersRawFile)
			
			adminUserList = adminUsersRawJSON["administrators"]
			isThereAdministrator = True
		else:
			isThereAdministrator = False
	
		isUserFileExists = os.path.exists("./Assets/Users/users.lms")
		if isUserFileExists == True:
			with open('Assets/Users/users.lms') as usersRawFile:
				usersRawJSON = json.load(usersRawFile)
			
			userList = usersRawJSON["users"]
			isThereUser = True
		else:
			isThereUser = False
	else:
		os.mkdir("Assets/Users")
	
		isThereAdministrator = False
		isThereUser = False
	
	if isThereUser == True and isThereAdministrator == True:
		loginPageDetail = "userscanlogin"
	elif isThereUser == True and isThereAdministrator == False:
		loginPageDetail = "userscanlogin"
	elif isThereUser == False and isThereAdministrator == True:
		loginPageDetail = "adminscanlogin"
	elif isThereUser == False and isThereAdministrator == False:
		loginPageDetail = "noonecanlogin"
	else:
		loginPageDetail = "noonecanlogin"
	
	while True:
		
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
		outputchkble = "Library Management System"
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
	
		header = "\033[0;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[0;37;40m" + spaces2 + "]"
		print(header)
		
		if loginPageDetail == "noonecanlogin":
			loginHeaderFromLoginPageDetail = "Registration"
		elif loginPageDetail == "adminscanlogin":
			loginHeaderFromLoginPageDetail = "Log In as Administrator"
		elif loginPageDetail == "userscanlogin":
			loginHeaderFromLoginPageDetail = "Log In"
		else:
			pass
	
		maxlength = float(screenwidth)
		outputchkble = loginHeaderFromLoginPageDetail
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
	
		centeredLine = BRIGHT_FORMAT + spaces1 + outputchkble + spaces2 + BASIC_FORMAT
		print(centeredLine)
		if loginPageDetail == "noonecanlogin":
			try:
				if passwordfeedback == "dosentmatch":
					print(f"{RED_BG_FORMAT}The two passwords doesn't match{BASIC_FORMAT}")
				elif passwordfeedback == "wrongpassword":
					print(f"{RED_BG_FORMAT}Wrong password{BASIC_FORMAT}")
				elif passwordfeedback == "missinguserdata":
					print(f"{RED_BG_FORMAT}This user exists but there are not user detail files. Please contact an Administrator!{BASIC_FORMAT}")
				elif passwordfeedback == "userdidntexists":
					print(f"{RED_BG_FORMAT}This is not an user{BASIC_FORMAT}")
				elif passwordfeedback == "registersuccess":
					break	
				else:	
					print("Now you can register an Administrator user, because of you have zero")
			except:
				print("Now you can register an Administrator user, because of you have zero")
		else:
			try:
				if passwordfeedback == "dosentmatch":
					print(f"{RED_BG_FORMAT}The two passwords doesn't match{BASIC_FORMAT}")
				elif passwordfeedback == "wrongpassword":
					print(f"{RED_BG_FORMAT}Wrong password{BASIC_FORMAT}")
				elif passwordfeedback == "missinguserdata":
					print(f"{RED_BG_FORMAT}This user exists but there are not user detail files. Please contact an Administrator!{BASIC_FORMAT}")
				elif passwordfeedback == "userdidntexists":
					print(f"{RED_BG_FORMAT}This is not an user{BASIC_FORMAT}")
				elif passwordfeedback == "registersuccess":
					break	
				else:
					print("")
			except:
				print("")
		print(f"{BRIGHT_FORMAT}Username:{BASIC_FORMAT}")
		loginuser = input("")
		print(f"{BRIGHT_FORMAT}Password:{BASIC_FORMAT}")
		loginpassword = getpass.getpass(prompt = f"{WHITE_BG_FORMAT}I hide your password{BASIC_FORMAT}")
		if loginPageDetail == "noonecanlogin":
			print("Password again:")
			loginagain = getpass.getpass(prompt = f"{WHITE_BG_FORMAT}I hide your password{BASIC_FORMAT}")
			if loginagain == loginpassword:
				loginuserb =  "\"" + loginuser + "\""
				loginpassword_bytes = loginpassword.encode('ascii')
				base64_bytes = base64.b64encode(loginpassword_bytes)
				base64_loginpassword = base64_bytes.decode('ascii')
				loginpassword = base64_loginpassword
				loginpasswordb = "\"" + loginpassword + "\""
				registrationData = """{
		"Username": """ + loginuserb + """,
		"Password": """ + loginpasswordb + """,
		"Role": "Administrator",
		"Permissions": ["Administrator"]
	}"""
				file = open(f"Assets/Users/{loginuser}.lms", "w+")
				file.write(registrationData)
				file.close()
	
				isAdminUsersFileExists = os.path.exists("./Assets/Users/adminusers.lms")
				if isAdminUsersFileExists == True:
					with open('Assets/Users/adminusers.lms') as adminUsersRawFile:
						adminUsersRawJSON = json.load(adminUsersRawFile)
					oldadminslist = adminUsersRawJSON["administrators"]
					oldadminslist.append(loginuser)
					newadminslist = oldadminslist
					newadminslistb = str(newadminslist)
					newadminslistb = newadminslistb.replace("'", "\"")
					adminuserdata = """{"administrators": """ + newadminslist + """}"""
					
					file = open("Assets/Users/adminusers.lms", "w+")
	
					file.write(adminuserdata)
	
					file.close()
				else:
					newadminslist = loginuserb
					adminuserdata = """{"administrators": [""" + newadminslist + """]}"""
					
					file = open("Assets/Users/adminusers.lms", "w+")
	
					file.write(adminuserdata)
	
					file.close()
				with open(f'Assets/Users/{loginuser}.lms') as loginuserRawFile:
					loginuserRawJSON = json.load(loginuserRawFile)
			
				
	
				isUserFileExists = os.path.exists("./Assets/Users/users.lms")
				if isUserFileExists == True:
					with open('Assets/Users/users.lms') as usersRawFile:
						usersRawJSON = json.load(usersRawFile)
					olduserslist = usersRawJSON["users"]
					olduserslist.append(loginuser)
					newuserslist = olduserslist
					newuserslistb = str(newuserslist)
					newuserslistb = newuserslistb.replace("'", "\"")
					userdata = """{"users": """ + newuserslist + """}"""
					
					file = open("Assets/Users/users.lms", "w+")
	
					file.write(userdata)
	
					file.close()
				else:
					newuserslist = loginuserb
					userdata = """{"users": [""" + newuserslist + """]}"""
					
					file = open("Assets/Users/users.lms", "w+")
	
					file.write(userdata)
	
					file.close()
				with open(f'Assets/Users/{loginuser}.lms') as loginuserRawFile:
					loginuserRawJSON = json.load(loginuserRawFile)
			
				passwordfeedback = "registersuccess"
	
				userloginned = loginuser
				break
			else:
				passwordfeedback = "dosentmatch"
		else:
			try:
				if passwordfeedback == "registersuccess":
					break
				else:
					isUserFileExists = os.path.exists("Assets/Users/users.lms")
					if isUserFileExists == True:
						with open(f'Assets/Users/users.lms') as usersRawFile:
							usersRawJSON = json.load(usersRawFile)
						if loginuser in usersRawJSON["users"]:
							isLoginUsersCurrentFileExists = os.path.exists(f"./Assets/Users/{loginuser}.lms")
							if isLoginUsersCurrentFileExists == True:
								with open(f'Assets/Users/{loginuser}.lms') as loginuserRawFile:
									loginuserRawJSON = json.load(loginuserRawFile)
								base64_filepassword = loginuserRawJSON["Password"]
								base64_bytes = base64_filepassword.encode('ascii')
								filepassword_bytes = base64.b64decode(base64_bytes)
								filepassword = filepassword_bytes.decode('ascii')
								if loginpassword == filepassword:
									userloginned = loginuser
									break
								else:
									passwordfeedback = "wrongpassword"
							else:
								passwordfeedback = "missinguserdata"
						else:
							passwordfeedback = "userdidntexists"
					else:
						pass
			except:
				isUserFileExists = os.path.exists("Assets/Users/users.lms")
				if isUserFileExists == True:
					with open(f'Assets/Users/users.lms') as usersRawFile:
						usersRawJSON = json.load(usersRawFile)
					if loginuser in usersRawJSON["users"]:
						isLoginUsersCurrentFileExists = os.path.exists(f"./Assets/Users/{loginuser}.lms")
						if isLoginUsersCurrentFileExists == True:
							with open(f'Assets/Users/{loginuser}.lms') as loginuserRawFile:
								loginuserRawJSON = json.load(loginuserRawFile)
							base64_filepassword = loginuserRawJSON["Password"]
							base64_bytes = base64_filepassword.encode('ascii')
							filepassword_bytes = base64.b64decode(base64_bytes)
							filepassword = filepassword_bytes.decode('ascii')
							if loginpassword == filepassword:
								userloginned = loginuser
								break
							else:
								passwordfeedback = "wrongpassword"
						else:
							passwordfeedback = "missinguserdata"
					else:
						passwordfeedback = "userdidntexists"
				else:
					pass
	print("")
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
	outputchkble = "Library Management System"
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

	header = "\033[0;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[0;37;40m" + spaces2 + "]"
	print(header)
	if loginPageDetail == "noonecanlogin":
		loginHeaderFromLoginPageDetail = "Registration"
	elif loginPageDetail == "adminscanlogin":
		loginHeaderFromLoginPageDetail = "Log In as Administrator"
	elif loginPageDetail == "userscanlogin":
		loginHeaderFromLoginPageDetail = "Log In"
	else:
		pass
	maxlength = float(screenwidth)
	outputchkble = loginHeaderFromLoginPageDetail
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

	centeredLine = BRIGHT_FORMAT + spaces1 + outputchkble + spaces2 + BASIC_FORMAT
	print(centeredLine)
	print("")
	print(f"{GREEN_BRIGHT_FORMAT}Username:{BASIC_FORMAT}")
	print(f"{GREEN_FORMAT}{loginuser}{BASIC_FORMAT}")
	print(f"{GREEN_BRIGHT_FORMAT}Password:{BASIC_FORMAT}")
	print(f"{GREEN_BG_FORMAT}I hide this password{BASIC_FORMAT}")
	print(f"{GREEN_FORMAT}Login Successful{BASIC_FORMAT}")
	time.sleep(1.75)
	
	with open(f'Assets/Users/{loginuser}.lms') as loginuserRawFile:
		loginuserRawJSON = json.load(loginuserRawFile)
	with open(f'Assets/Users/{userloginned}.lms') as userloginnedRawFile:
		userloginnedRawJSON = json.load(userloginnedRawFile)
	loginneduserPermissions = userloginnedRawJSON["Permissions"]
	while True:
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
		outputchkble = "Library Management System"
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
	
		header = "\033[0;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[0;37;40m" + spaces2 + "]"
		print(header)
		print("")
		print(f"{BRIGHT_FORMAT}Navigate with the names beetwen the parentheses then press enter{BASIC_FORMAT}")
		print("")
			
		if "Administrator" in loginneduserPermissions:
			print(f"{BASIC_FORMAT}Open terminal(terminal){BASIC_FORMAT}")
		elif "terminal" in loginneduserPermissions:
			print(f"{BASIC_FORMAT}Open terminal(terminal){BASIC_FORMAT}")
		else:
			print(f"{GREY_FORMAT}Open terminal{BASIC_FORMAT}")
		if "Administrator" in loginneduserPermissions:
			print(f"{BASIC_FORMAT}Book database(database){BASIC_FORMAT}")
		elif "database" in loginneduserPermissions:
			print(f"{BASIC_FORMAT}Book database(database){BASIC_FORMAT}")
		else:
			print(f"{GREY_FORMAT}Book database{BASIC_FORMAT}")
		if "Administrator" in loginneduserPermissions:
			print(f"{BASIC_FORMAT}Manage users(users){BASIC_FORMAT}")
		elif "users" in loginneduserPermissions:
			print(f"{BASIC_FORMAT}Manage users(users){BASIC_FORMAT}")
		else:
			print(f"{GREY_FORMAT}Manage users{BASIC_FORMAT}")
	
		userinput = input(f"{BRIGHT_FORMAT}Command: {BASIC_FORMAT}")
		if userinput == "terminal":
			if "Administrator" in loginneduserPermissions:
				pass
			elif "terminal" in loginneduserPermissions:
				pass
			else:
				print(f"{RED_BG_FORMAT}You don't have permission to this command{BASIC_FORMAT}")
				time.sleep(5)
		elif userinput == "database":
			if "Administrator" in loginneduserPermissions:
				pass
			elif "database" in loginneduserPermissions:
				pass
			else:
				print(f"{RED_BG_FORMAT}You don't have permission to this command{BASIC_FORMAT}")
				time.sleep(5)
		elif userinput == "users":
			if any(item in permsToAccessUsersmenu for item in loginneduserPermissions):
				while True:
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
					outputchkble = "Library Management System"
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
				
					header = "\033[0;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[0;37;40m" + spaces2 + "]"
					print(header)
					print(f"{BRIGHT_FORMAT}Navigate with the names beetwen the parentheses then press enter{BASIC_FORMAT}")
					print("")
					print("New user(new)")
					print("User list(list)")
					print("Delete User(delete)")
					print("Delete all users(delall)")
					print("Back(back)")
					userinput = input("Command: ")
					if userinput == "new":
						passwordfeedback = "reseted"
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
						outputchkble = "Library Management System"
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
			
						header = "\033[0;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[0;37;40m" + spaces2 + "]"
						print(header)
			
						time.sleep(2)
			
						while True:
				
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
							outputchkble = "Library Management System"
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
							header = "\033[0;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[0;37;40m" + spaces2 + "]"
							print(header)
							maxlength = float(screenwidth)
							outputchkble = "Create new user"
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
						
							centeredLine = BRIGHT_FORMAT + spaces1 + outputchkble + spaces2 + BASIC_FORMAT
							print(centeredLine)
							try:
								if passwordfeedback == "dosentmatch":
									print(f"{RED_BG_FORMAT}The two passwords doesn't match{BASIC_FORMAT}")
								elif passwordfeedback == "wrongpassword":
									print(f"{RED_BG_FORMAT}Wrong password{BASIC_FORMAT}")
								elif passwordfeedback == "missinguserdata":
									print(f"{RED_BG_FORMAT}This user exists but there are not user detail files. Please contact an Administrator!{BASIC_FORMAT}")
								elif passwordfeedback == "userdidntexists":
									print(f"{RED_BG_FORMAT}This is not an user{BASIC_FORMAT}")
								elif passwordfeedback == "registersuccess":
									break	
								else:
									print("")
							except:
								print("")
							print(f"{BRIGHT_FORMAT}Username:{BASIC_FORMAT}")
							newuser = input("")
							print(f"{BRIGHT_FORMAT}Password:{BASIC_FORMAT}")
							loginpassword = getpass.getpass(prompt = f"{WHITE_BG_FORMAT}I hide this password{BASIC_FORMAT}")
							print("Password again:")
							loginagain = getpass.getpass(prompt = f"{WHITE_BG_FORMAT}I hide this password{BASIC_FORMAT}")
							if loginagain == loginpassword:
								newuserb =  "\"" + newuser + "\""
								loginpassword_bytes = loginpassword.encode('ascii')
								base64_bytes = base64.b64encode(loginpassword_bytes)
								base64_loginpassword = base64_bytes.decode('ascii')
								loginpassword = base64_loginpassword
								loginpasswordb = "\"" + loginpassword + "\""
								roleinput = input(f"{BRIGHT_FORMAT}Select a role for the new user:{BASIC_FORMAT} ")
								roleinputb = "\"" + roleinput + "\""
								newUserPerms = []
								while True:
									print("Please type the permission names, whiches you want to add to the user(if none, press enter):")
									permissionToAppend = input("")
									if permissionToAppend == "":
										break
									else:
										newUserPerms.append(permissionToAppend)
							
									newUserPermsb = str(newUserPerms)
									newUserPermsb = newUserPermsb.replace("'", "\"")
									registrationData = """{
		"Username": """ + newuserb + """,
		"Password": """ + loginpasswordb + """,
		"Role": """ + roleinputb + """,
		"Permissions": """ + newUserPermsb + """
	}"""
								file = open(f"Assets/Users/{newuser}.lms", "w+")
								file.write(registrationData)
								file.close()
								
								if "Administrator" in newUserPerms:
									isAdminUsersFileExists = os.path.exists("./Assets/Users/adminusers.lms")
									if isAdminUsersFileExists == True:
										with open('Assets/Users/adminusers.lms') as adminUsersRawFile:
											adminUsersRawJSON = json.load(adminUsersRawFile)
										oldadminslist = adminUsersRawJSON["administrators"]
										oldadminslist.append(newuser)
										newadminslist = oldadminslist
										newadminslistb = str(newadminslist)
										newadminslistb = newadminslistb.replace("'", "\"")
										adminuserdata = """{"administrators": """ + newadminslistb + """}"""
									
										file = open("Assets/Users/adminusers.lms", "w+")
					
										file.write(adminuserdata)
					
										file.close()
									else:
										newadminslist = newuserb
										adminuserdata = """{"administrators": [""" + newadminslist + """]}"""
									
										file = open("Assets/Users/adminusers.lms", "w+")
					
										file.write(adminuserdata)
						
										file.close()
									with open(f'Assets/Users/{newuser}.lms') as newuserRawFile:
										newuserRawJSON = json.load(newuserRawFile)
								elif roleinput == "Administrator":
									isAdminUsersFileExists = os.path.exists("./Assets/Users/adminusers.lms")
									if isAdminUsersFileExists == True:
										with open('Assets/Users/adminusers.lms') as adminUsersRawFile:
											adminUsersRawJSON = json.load(adminUsersRawFile)
										oldadminslist = adminUsersRawJSON["administrators"]
										oldadminslist.append(newuser)
										newadminslist = oldadminslist
										newadminslistb = str(newadminslist)
										newadminslistb = newadminslistb.replace("'", "\"")
										adminuserdata = """{"administrators": """ + newadminslistb + """}"""
									
										file = open("Assets/Users/adminusers.lms", "w+")
					
										file.write(adminuserdata)
					
										file.close()
									else:
										newadminslist = newuserb
										adminuserdata = """{"administrators": [""" + newadminslist + """]}"""
									
										file = open("Assets/Users/adminusers.lms", "w+")
					
										file.write(adminuserdata)
						
										file.close()
									with open(f'Assets/Users/{newuser}.lms') as newuserRawFile:
										newuserRawJSON = json.load(newuserRawFile)
								else:
									pass
			
								isUserFileExists = os.path.exists("./Assets/Users/users.lms")
								if isUserFileExists == True:
									with open('Assets/Users/users.lms') as usersRawFile:
										usersRawJSON = json.load(usersRawFile)
									olduserslist = usersRawJSON["users"]
									olduserslist.append(newuser)
									newuserslist = olduserslist
									newuserslistb = str(newuserslist)
									newuserslistb = newuserslistb.replace("'", "\"")
									userdata = """{"users": """ + newuserslistb + """}"""
									
									file = open("Assets/Users/users.lms", "w+")
					
									file.write(userdata)
					
									file.close()
								else:
									newuserslist = newuserb
									userdata = """{"users": [""" + newuserslist + """]}"""
									
									file = open("Assets/Users/users.lms", "w+")
					
									file.write(userdata)
					
									file.close()
								with open(f'Assets/Users/{newuser}.lms') as newuserRawFile:
									newuserRawJSON = json.load(newuserRawFile)
							
								passwordfeedback = "registersuccess"
								break
							else:
								passwordfeedback = "dosentmatch"
					elif userinput == "list":
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
						outputchkble = "Library Management System"
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
					
						header = "\033[0;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[0;37;40m" + spaces2 + "]"
						print(header)
						with open(f'Assets/Users/users.lms') as usersRawFile:
							usersRawJSON = json.load(usersRawFile)
						userlist = usersRawJSON["users"]
						print("")
						for x in userlist:
							index = userList.index(x)
							index = index + 1
							index = str(index)
							print("(" + index + ") " + x)
						entertonext = input("Press enter to close this")
					elif userinput == "del":
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
						outputchkble = "Library Management System"
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
					
						header = "\033[0;37;40m[" + spaces1 + "\033[0;30;47m" + outputchkble + "\033[0;37;40m" + spaces2 + "]"
						print(header)
						print("")
						userToDelete = input("Which user is what you want to delete? ")
					elif userinput == "delall":
						pass
					elif userinput == "back":
						break
					else:
						pass
			else:
				print(f"{RED_BG_FORMAT}You don't have permission to this command{BASIC_FORMAT}")
				time.sleep(2)
		else:
			print(f"{RED_FORMAT}This is not an available command or you typed it wrong!{BASIC_FORMAT}")
			time.sleep(1.75)