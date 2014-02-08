# Created By: Omar Quazi
# Copyleft 2014 under the GNU GPL v3. You are permitted to redistribute
# this program with or without modifications; but, the copy must retain this
# license agreement.
# For the full license, please visit  the Free Software Foundation:
# https://www.gnu.org/copyleft/gpl.html

from getpass import getpass
import os

salt = '$5$rounds=100613$ALBhUagdebqrq0Ws$uyRV3Z0TvU/Obi84be6r/5RvKlQG7mhVA4ZaC9A6sU3'
encoded = ""
finalPass = encoded+salt

def lockFunc():
    print "--- Lock Folder? ---"
    print "1. Yes"
    print "2. No"
    enter = raw_input()
    doIt = False
    if enter.upper() == "YES":
        doIt = True
    if enter.upper() == "Y":
        doIt = True
    if enter.upper() == "1":
        doIt = True
    if doIt:
        os.system("ren Locker \"Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}\"")
        os.system("attrib +h +s \"Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}\"")
        print "Success."

def unlockFunc(salt,finalPass):
    print "--- Password To Unlock Folder ---"
    enter = getpass()
    hashReady = list(enter)
    newEnter = ""
    for x in hashReady:
        ascii = ord(x) + 3
        newEnter += chr(ascii)

    hashedPass = newEnter+salt

    if hashedPass == finalPass:
        os.system("attrib -h -s \"Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}\"")
        os.system("ren \"Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}\" Locker")
        print "Success!"
        fail = False
    else:
        fail = True
    return fail

def createFunc():
    print "--- Create a Locker Folder? ---"
    print "1. Yes"
    print "2. No"
    enter = raw_input()
    doIt = False
    if enter.upper() == "YES":
        doIt = True
    if enter.upper() == "Y":
        doIt = True
    if enter.upper() == "1":
        doIt = True
    if doIt:
        os.system("md Locker")
        print "Created Succcessfully."

def fail():
    print "Failed. Password is incorrect."


# Folder Check. Does it exist?

if (os.path.isdir(os.curdir+"\\Locker")):
    lockFunc()
elif (os.path.isdir(os.curdir+"\\Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}")):
    unlock = unlockFunc(salt,finalPass)
    if unlock:
        fail()
else:
    createFunc()

os.system("pause")
