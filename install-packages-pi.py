import os
import time
import sys
import pwd
import grp
import subprocess

def update_packages_pipes():
	process1 = subprocess.Popen("apk update",shell=True, stdout=subprocess.PIPE)
        process1.wait()
        process2 = subprocess.Popen("apk add htop",shell=True, stdout=subprocess.PIPE)
        process2.wait()
        process3 = subprocess.Popen("apk add --update coreutils",shell=True, stdout=subprocess.PIPE)
        process3.wait()
        process4 = subprocess.Popen("apk add python",shell=True, stdout=subprocess.PIPE)
        process4.wait()
        process5 = subprocess.Popen("apk add nginx",shell=True, stdout=subprocess.PIPE)
        process5.wait()
        process6 = subprocess.Popen("apk add emacs",shell=True, stdout=subprocess.PIPE)
        process6.wait()
update_packages_pipes()
