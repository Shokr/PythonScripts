"""
Compare 2 Directories and list the files not in sync (file names only)

"""

import os.path
from collections import Counter


def get_tree(d):
    retList = []
    os.chdir(d)
    for path, dirs, files in os.walk("."):
        for fn in files:
            retList.append(os.path.join(path, fn))
    os.chdir("..")
    return retList


def compare_director(d1, d2):
    not_found = []
    co = Counter(get_tree(d1))
    co.update(get_tree(d2))
    for w in co.most_common():
        if w[1] != 2:
            not_found.append(w[0])
    return not_found


print("Missing files are:\n", "\n".join(compare_director("./Dir2", "./Dir1")))
