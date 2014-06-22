#!/usr/bin/env python2
import datetime
import sys
import os
from subprocess import check_output

esc = chr(27)
save_pos = esc+"[s"
restore_pos = esc+"[u"
upper_left = esc+"[1;0H"
inverse = esc+"[7m"
restore = esc+"[0m"
erase_to_end_of_line = esc+"[K"
CACHE_FILE = "/tmp/update_cache"
time_to_update = False

twelve_hours_ago = datetime.datetime.now() - datetime.timedelta(hours=12)

def modification_date(filename):
    # This function stolen from 
    # http://stackoverflow.com/questions/2502833/store-output-of-subprocess-popen-call-in-a-string
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

if not os.path.exists(CACHE_FILE) or modification_date(CACHE_FILE) < twelve_hours_ago:
    time_to_update = True

updates = None

def write_message(msg):
    sys.stdout.write(save_pos)
    sys.stdout.write(upper_left)
    # sys.stdout.write(inverse)
    sys.stdout.write(msg)
    sys.stdout.write(erase_to_end_of_line)
    sys.stdout.write(restore_pos)
    # sys.stdout.write(restore)
    sys.stdout.flush()

def and_join(_list):
    if len(_list) <= 1:
        return "".join(_list)

    last = _list.pop()
    result = ", ".join(_list)+" and "+last
    return result

if time_to_update:
    write_message("Updating cache list ...")
    updates = check_output(["checkupdates"])
    updates = updates.strip()
    fp = open(CACHE_FILE, "w")
    fp.write(updates)
    fp.close()

if updates is None:
    updates = open(CACHE_FILE, "r").read()

packages = updates.split("\n")
packages_len = len(packages)

if packages_len > 0:
    write_message("%d updates.  Packages: %s" % (packages_len, and_join(packages)) )
else:
    write_message("%d updates." % (packages_len,))

