import os
import time

if(os.path.isdir('.')):
    print ("current directory : %s" % os.getcwd())
    print ("directory size :%s" % os.path.getsize('.'))
    print ("directory permissions :%s" % oct(os.stat('.').st_mode))
    print ("directory owner :%s" % oct(os.stat('.').st_uid))
    print ("directory device :%s" % oct(os.stat('.').st_dev))
    print ("created at: %s" % time.ctime(os.path.getctime('.')))
    print ("last modified: %s" % time.ctime(os.path.getmtime('.')))
    print ('Last accessed:', time.ctime(os.path.getatime('.')))