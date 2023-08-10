# MAIN IMPORTS & VARS #
import os
import datetime
import platform
from colorama import Fore
import time
import json
cReset = Fore.RESET
nameColor = Fore.GREEN
user_system = platform.uname()
collectInput = nameColor+f'{user_system.node}'+cReset+':~$ '

global mainDirectoryName
mainDirectoryName = 'PLAYGROUND'
mainDirectory = f'./{mainDirectoryName}'
terminalDirectory = f'{mainDirectory}/TERMINAL_FILES'
journalDirectory = f'{terminalDirectory}/Journal.txt'

#####################
### OPEN SETTINGS ###
#####################


###############################
### COMMANDS & DESCRIPTIONS ###
###############################

helpList = {"x": "Close the terminal.",
            "help": "[TERM] Shows this menu.",
            "ls": "Gives a list of every item in the directory.",
            "dir": "Shows what directory you are operating in.",
            "time": "['date' or 'time'] Shows the current date and time.",
            "clear": "[TERM] Clears the terminal.",
            "settings": "[TERM] Change certain settings for the terminal.",
            "journal": "[APP] Add a line to your journal .TXT file."}

### COMMANDS ###

def otherFile():
    print("Other Files Work, ./commands.py")

def helpCmd():
    print("")
    print(Fore.CYAN + "~ TERMINAL HELP ~" + cReset)
    print("GitHub: https://github.com/ethanp172/Custom-Terminal/tree/main")
    print("If you recieve an error, check the docs error section.")
    print("")
    for cmd, desc in helpList.items():
        print(Fore.CYAN + f'> {cmd}' + cReset)
        print(f'  >> {desc}')
    print("")

def specialHelpCmd(x):
    print("")
    print(f'~ TERMINAL HELP FOR {x} ~')
    print("GitHub: https://github.com/ethanp172/Custom-Terminal/tree/main")
    print("")



def writeJournal():
    import time
    if os.path.isfile(f'{terminalDirectory}\Journal.txt'): # Checks if the journal is a file
        time.sleep(.75)
        ## DO JOURNAL THINGS ##
        print(Fore.CYAN+'Write your journal entry:'+cReset)
        journalInput = input(Fore.MAGENTA+'JOURNAL INPUT '+cReset+':~$ ')
        print(Fore.GREEN+'Would you like to submit: '+Fore.LIGHTGREEN_EX+journalInput+cReset+"?")
        journalAnswer = input("(Y/N) ").upper()

        if journalAnswer == 'N':
            print("STOPPED")
        else:
            f = open(f'{terminalDirectory}/Journal.txt', "a")
            f.write(f'{journalInput} \n')
            print("SUBMITTED!")

    else: # If no journal, then make the journal
        f = open(f'{terminalDirectory}/Journal.txt', "x")
        time.sleep(.55)
        print("No journal file found...")
        time.sleep(1)
        print(f'Journal file created! ({terminalDirectory}\Journal.txt)')




def ls():
    print("")
    print(Fore.CYAN + f'{mainDirectory}' + Fore.BLUE + ' DIRECTORY' + cReset)
    for filename in os.listdir(mainDirectory):
        print(f'━ {filename}')
    print("")

def dir():
    print("")
    print(f'DIRECTORY: {mainDirectory}')
    print("")

def time():
    print(datetime.datetime.now())

def clear():
    i = 0
    while i < 45:
        print("")
        i = i + 1

def upupSecret():
    print("""
_____________________$$$
____________________$___$
_____________________$$$
_____________________$_$
_____________________$_$
___________________$$$_$$$
_________________$$__$$$__$$$
_______________$$__$$$$$$$___$
______________$_______________$
_____________$_________________$
_____________$_________________$
_____________$_____$$$$$$$$$$$$$$$
_____________$____$_______________$
_____________$____$___$$$$$$$$$$$$$
_____________$___$___$___________$$$
_____________$___$___$_$$$___$$$__$$
_____________$___$___$_$$$___$$$__$$
_____________$___$___$___________$$$
_____________$____$___$$$$$$$$$$$$$
_____________$_____$$$$$$$$$$$$$$
_____________$_________________$
_____________$____$$$$$$$$$$$$$$
_____________$___$__$__$__$__$
_____________$__$$$$$$$$$$$$$$
_____________$__$___$__$__$__$
_____________$___$$$$$$$$$$$$$$$
____________$$$_________________$$$
__________$$___$$$_________$$$$$___$$
________$$________$$$$$$$$$__________$$$
_______$__$$_____________________$$$$___$$
____$$$$$___$$$$$$$$______$$$$$$$_______$_$
__$______$$_________$$$$$$______________$_$$
_$____$____$____________________________$_$_$
_$_____$___$______________$$$$$$$$$$$___$_$_$$
_$$$____$___$__$$$$$$$$$$$$__________$___$_$_$$
$___$$$$____$__$_____________________$___$_$$_$
$$$____$___$$__$_____________________$$__$_$__$
$___$__$__$$___$______________________$__$$$__$
$_____$$_$$____$_______________$$$____$__$_$__$
""")



#####################
### TESTING FILES ###
#####################

def testJson():
    print("<!> THIS IS FOR DEBUGGING, DO NOT USE IF YOU ARE NOT A DEVELOPER <!>")
    ## OPEN JSON FILE ##
    with open(f'{terminalDirectory}\Settings.JSON') as config_file:
        data = json.load(config_file)
    
    ## READ JSON DATA ##
    name = data['name']
    dir = data['directory']

    ## MAKE JSON DATA ##
    data["newData"] = "Hello World!"

    ## EDIT JSON DATA ##
    data.pop("directory") # field =
    data["directory"] = "New Information"

    ## WRITE TO JSON FILE ##
    newData = json.dumps(data, indent=2)
    with open(f'{terminalDirectory}\Settings.JSON', 'w') as config_file:
        config_file.write(newData)
    
    ## USE JSON DATA ##
    print(name)
    print(dir)

## SETTINGS ##
def settings():
    # gather JSON files and put into table
    # for each aspect print it like: 1) SETTING: VALUE
    # ask for which table number or SETTING to change
    # ask for new VALUE, then update the JSON file
    # give a success message and eventually make the settings used

    with open(f'{terminalDirectory}\Settings.JSON') as config_file:
        data = json.load(config_file)
        settingList = []
        settingValues = []
        
        for setting in data:
            settingList.append(setting) # Add each setting to the list

        for setting in settingList:
            settingValues.append(data[setting]) # Add each settings value to the list

        print("--[SETTINGS]--")
        print("")
        
        ## Print the setting table ##
        i = 0
        while i < len(data):
            print(f'{i}) {settingList[i]}: {settingValues[i]}')
            i = i + 1
        
        print("")

        print("Would you like to edit a setting?")
        changeDecision = input("Y/N ").upper()
        if changeDecision == "Y":
            print("")
            print("What # would you like to edit?")
            changeInput = int(input("Proive a number: "))
            print(f'{settingList[changeInput]}: {settingValues[changeInput]}')
            print("")

            print("What new value would you like to set?")
            newValue = input()

            data.pop(settingList[changeInput])
            data[settingList[changeInput]] = newValue

            newData = json.dumps(data, indent=2)
            with open(f'{terminalDirectory}\Settings.JSON', 'w') as config_file:
                config_file.write(newData)

        else: # Make sure to add error catching soon
            print("")

## TEST DIRECTORIES ##       
def testDirs():
    testDir = 'C:/Users/crunc/OneDrive/Desktop/CustomTerminalProject'
    for filename in os.listdir(testDir):
        print(f'{filename}')

