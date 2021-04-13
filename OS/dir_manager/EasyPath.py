import os.path
from collections import Counter
import time

from pprint import pprint


def get_user_path():
    return os.path.expanduser('~')


def get_current_path():
    return os.path.abspath(os.getcwd())


def get_tree(directory):
    """
    Get Folder Tree.
    """
    retList = []
    os.chdir(directory)
    for path, dirs, files in os.walk("."):
        for fn in files:
            retList.append(os.path.join(path, fn))
    os.chdir("..")
    return retList


def compare_director(directory1, directory2):
    """
    Compare 2 Directories and list the files not in sync.
    """

    not_found = []
    co = Counter(get_tree(directory1))
    co.update(get_tree(directory2))
    for w in co.most_common():
        if w[1] != 2:
            not_found.append(w[0])
    return not_found


def get_dir_info(directory):
    """
    Get all meta-data about directory.
    """
    DIR_INFO = {"directory": "%s" % os.getcwd(),
                "directory_size": "%s" % os.path.getsize(directory),
                "directory_permissions": "%s" % oct(os.stat(directory).st_mode),
                "directory_owner": "%s" % oct(os.stat(directory).st_uid),
                "directory_device": "%s" % oct(os.stat(directory).st_dev),
                "created_at": "%s" % time.ctime(os.path.getctime(directory)),
                "last_modified": "%s" % time.ctime(os.path.getmtime(directory)),
                "last_accessed": "%s" % time.ctime(os.path.getatime(directory))}
    return DIR_INFO


def get_directory_files_form_oldest_to_newest(directory):
    """
    Get Ordered list of directory files.
    """
    os.chdir(directory)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    return files


def get_latest_file(directory):
    """
    Get lastest file in directory.
    """
    return max(get_tree(directory))


def look_in_directory(directory, file_to_find):
    """
    Loop through the current directory for the file, if the current item
       is a directory, it recusively looks through that folder
    """

    # Loop over all the items in the directory
    for f in os.listdir(directory):
        # Uncomment the line below to see how the files/folders are searched
        # print "Looking in " + directory

        # If the item is a file check to see if it is what we are looking
        # for, if it is, print that we found it and return true
        if os.path.isfile(os.path.join(directory, f)):
            if f == file_to_find:
                print("Found file: " + os.path.join(directory, f))
                return True

        # If the item is a directory, we recursivley look through that
        # directory if it is found, we again return true
        if os.path.isdir(os.path.join(directory, file_to_find)):
            if look_in_directory(os.path.join(directory, f)):
                return True


def open_in_browser(path):
    """
    Open directory in web browser.
    """
    import webbrowser
    return webbrowser.open(path)


def get_full_path(path):
    """
    Get file full path.
    """
    if path.isfile:
        return os.path.abspath(path)
    else:
        return path


if __name__ == '__main__':
    print("Hello to Folder Middleware :) ")

    # # we will look for the file recursively
    # directory = "."
    # file_to_find = 'hi.txt'
    #
    # # Start looking in the home directory (~)
    # # If it is not found, ie it did not return True, tell the user it was "Not
    # # Found"
    # if not look_in_directory(directory, file_to_find):
    #     print("Not Found")

    # print("All by modified oldest to newest:",
    #       get_directory_files_form_oldest_to_newest("."))
    #
    # print("The Latest File:- ", max(get_tree(".")))
    #
    # print("get_dir_info:- ")
    # pprint(get_dir_info("."))
    #
    # print("Sys User Path:-  ", get_user_path())
    # print("Current Path:- ", get_current_path())
    # print("Folder Tree:- ", get_tree(get_current_path()))

    # print("Missing files are:")
    # print(compare_director("/var",
    #                        "/tmp"))
