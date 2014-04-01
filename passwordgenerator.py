# This will help you generate a password

enter = raw_input("Please enter a password: ")
hashReady = list(enter)
newEnter = ""

for x in hashReady:
    ascii = ord(x) + 3
    newEnter += chr(ascii)

print "Encoded password:",newEnter
print "^Please replace the \"encoded\" variable in main.py with the above^"
