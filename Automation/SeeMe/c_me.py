"""
The script takes grabs the title of the active window and print out the amount of time spent on the output file,
after that you can use this data to see how much time you spend on each application.
"""
import sys
from time import sleep
from time import time

from AppKit import NSWorkspace

if len(sys.argv) != 2:
    sys.exit("Usage: SCRIPT output_file.txt")

file = open(sys.argv[1], "a")
lastname = ""
t = time()
while True:
    activeAppName = NSWorkspace.sharedWorkspace().activeApplication(
    )["NSApplicationName"]
    if activeAppName != lastname:
        if lastname:
            file.write("\n" + "% 10d" % (int(time() - t), ) + "\t" + lastname)
        lastname = activeAppName
        t = time()
        file.flush()

    sleep(1)
