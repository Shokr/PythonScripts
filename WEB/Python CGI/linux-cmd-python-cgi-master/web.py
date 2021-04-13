#!/usr/bin/python3
import subprocess
import cgi

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
myx = mydata.getvalue("c")
myy = mydata.getvalue("d")

if myx == str(1):
    output = subprocess.getoutput("sudo date")
    print(output)
elif myx == str(2):
    output = subprocess.getoutput("sudo cal")
    print(output)
elif myx == str(3):
    output = subprocess.getoutput("sudo docker create -it centos")
    print(output)
elif myx == str(4):
    output = subprocess.getoutput("sudo docker ps")
    print(output)
elif myx == str(5):
    output = subprocess.getoutput("sudo docker images")
    print(output)
elif myx == str(6):
    output = subprocess.getoutput("sudo firefox")
    print(output)
elif myx == str(7):
    output = subprocess.getoutput("sudo firefox https://google.com")
    print(output)
elif myx == str(8):
    output = subprocess.getoutput("sudo ls")
    print(output)
elif myx == str(9):
    output = subprocess.getoutput("sudo pwd")
    print(output)
elif myx == str(10):
    output = subprocess.getoutput("sudo mkdir Newclearfolder")
    print(output)
else:
    print()

    output = subprocess.getoutput("sudo " + myy)
    print(output)
