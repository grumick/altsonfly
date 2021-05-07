import argparse
import os
import random
import string
import threading

parser = argparse.ArgumentParser(description='Generate alternate accounts on fly using Linux')
parser.add_argument('-a', '--add', type=int, dest='amount', help='Amount of alts to generate at once')
parser.add_argument ('-p', '--program', type=str, dest='program', help='Program to launch')
parser.add_argument ('-r', '--remove', action='store_true', help='Delete all existing alts')
arguments = parser.parse_args()

global accountNames
global orignialAltsDirectorySize
orignialAltsDirectorySize = len(os.listdir("/alts/"))
accountNames = []

def randoms(n):
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(n))
    
def generateAlts():
    if arguments.amount > 10:
        print("altsonfly> too many desired additions provided")
    else:
        for accountAmount in range(arguments.amount):
            accountNames.append(randoms(5))
            if len(accountNames) == arguments.amount:
                for i in range(arguments.amount):
                    try:
                        os.system("useradd -m -b /alts/ -G video,audio,network " + accountNames[i])
                        print("altsonfly> Successfully added " + accountNames[i])
                    except:
                        print("altsonfly> Issue encured with adding...")
                    finally:
                        if abs(orignialAltsDirectorySize-len(os.listdir('/alts/'))) is arguments.amount:
                            print("altsonfly> Checking finished... initializing..")
                            initializeAltThreads()
                        else:
                            print(abs(orignialAltsDirectorySize-len(os.listdir('/alts'))))
                            
def initializeAltThreads():
    t = threading.Thread(target=executeProgram())
    t.start()
    
def executeProgram():
    print(os.listdir('/alts/'))
    for accountNamely in accountNames:
        #print("this: " + accountNamely)
        os.system("sudo -u " + accountNamely + " -S " + arguments.program + "&")
        
def main():
    if arguments.amount is None and arguments.program is None:
        if arguments.remove is True:
            euid = os.geteuid()
            if euid != 0:
                print("altsonfly> Root Permissions required")
            else:
                if len(os.listdir("/alts/")) >= 1:
                    for directoryListing in os.listdir("/alts/"):
                        os.system("userdel -r " + str(directoryListing))
                        print("altsonfly> Successfully removed " + directoryListing)
                elif len(os.listdir("/alts/")) == 0:
                    print("altsonfly> No need to delete, directory listing is empty.")
        else:
            parser.print_help()
        return
    elif arguments.amount is None or arguments.program is None:
        print("altsonfly> not enough arguments supplied")
    elif arguments.amount is not None and arguments.program is not None:
        euid = os.geteuid()
        if euid != 0:
            print("altsonfly> Root Permissions required")
        else:
            print("altsonfly> generating alts...")
            generateAlts()
            
if __name__ == '__main__':
    main()
