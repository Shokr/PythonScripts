# # Build Sources list form nuke nodes
# nodes = ['/home/shokr/PycharmProjects/soso/x####.txt','/home/shokr/mix/z.txt','/home/shokr/PycharmProjects/soso/y####.txt']


# SOURCES = []

# for node in nodes:
#     if '####' in node:
#         frames = 2
#         i = 1
#         while i <= frames:
#             zx = node.replace('####',  str(format(i, "0>4")))
#             SOURCES.append(zx)
#             i += 1

#     else:
#         SOURCES.append(node)

# print SOURCES


# # Function to make copy file with metadata from sources to local.

# import shutil
# from os import path

# import time

# DESTINATION = '/home/shokr/XLAB/localize'

# for SOURCE in SOURCES:

#     try:
#         filePath, fileName = path.split(SOURCE)
#         # print filepath, file
#         DST = path.join(DESTINATION, fileName)

#         SOURCE_Modification_Time = time.ctime(path.getmtime(SOURCE))
#         DST_Modification_Time = time.ctime(path.getmtime(DST))
#     except:
#         print 'ERROR'


#     if path.exists(DST) and SOURCE_Modification_Time == DST_Modification_Time:
#         print 'Already COPIED'
#     else:
#         try:
#             shutil.copy2(SOURCE, DESTINATION)
#             print 'COPIED'
#         except:
#             print 'File Not Found'


import shutil
import os
from time import ctime

SOURCE = "/home/shokr/PycharmProjects/xapis"
project = SOURCE.split("/")[-1]
print
project

DESTINATION = "/home/shokr/XLAB/localize/"
DESTINATION = os.path.join(DESTINATION, project)

if os.path.exists(DESTINATION) and ctime(os.path.getmtime(SOURCE)) == ctime(
    os.path.getmtime(DESTINATION)
):
    print
    "Directory was copied"
else:

    try:
        shutil.rmtree(DESTINATION)
    except OSError as e:
        print
        e.strerror

    shutil.copytree(SOURCE, DESTINATION)
