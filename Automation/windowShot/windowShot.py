"""
Take a screenshot for a window, query by window title (windowShot.py 'Mail') output to tmp directory.
"""
import os
from sys import argv

from Quartz import CGWindowListCopyWindowInfo
from Quartz import kCGNullWindowID
from Quartz import kCGWindowListExcludeDesktopElements
from Quartz import kCGWindowListOptionOnScreenOnly

windowList = CGWindowListCopyWindowInfo(
    kCGWindowListOptionOnScreenOnly | kCGWindowListExcludeDesktopElements,
    kCGNullWindowID,
)
systemWindows = ["SystemUIServer", "Window Server", "Spotlight"]
searchname = argv[1].lower()
for i in windowList:
    if (
        searchname in i["kCGWindowOwnerName"].lower()
        and i["kCGWindowOwnerName"] not in systemWindows
    ):
        print(i["kCGWindowNumber"], i["kCGWindowOwnerName"])
        os.system(
            'screencapture -l{0} "tmp/{0}{1}.png"'.format(
                i["kCGWindowNumber"], i["kCGWindowOwnerName"]
            )
        )
