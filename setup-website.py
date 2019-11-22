#send a file to the raspberry pi (or any SBC) which is capable of installing relevant programs. This is neccessary every boot due to fruitOs (based on alpine linux) not remembering anything.

import subprocess

ipList = (["192.168.1.10"])#pi 3b+ running fruitOs

def send_update(u):
    process1 = subprocess.Popen(["scp -o StrictHostKeyChecking=no -i /home/lunet/eljb13/Dropbox/rpi_testbed/ssh-key-for-fruit install-packages-pi.py root@" +ipList[u]+":/root"], shell=True, stdout=subprocess.PIPE)
    process1.wait()

#now the update has been sent, it is worth checking that this can be run remotely from this script.

    
send_update(0)
