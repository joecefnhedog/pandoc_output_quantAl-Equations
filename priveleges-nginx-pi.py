import os
import time
import subprocess
def chownpython(path):
    for root, dirs, files in os.walk(path):
        for momo in dirs:
            os.chown(os.path.join(root, momo), 1000, 1000)
        for momo in files:
            os.chown(os.path.join(root, momo), 1000, 1000)

def nginx_setup():
    process1 = subprocess.Popen("adduser -D -g 'www' www",shell=True, stdout=subprocess.PIPE)
    process1.wait()
    process2 = subprocess.Popen("mkdir /www",shell=True, stdout=subprocess.PIPE)
    process2.wait()
    process3 = subprocess.Popen("rm /var/lib/nginx/run",shell=True, stdout=subprocess.PIPE)
    process3.wait()
    path1 = "/var/lib/nginx"
    chownpython(path1)
    path2 = "/www"
    chownpython(path2)


nginx_setup()
