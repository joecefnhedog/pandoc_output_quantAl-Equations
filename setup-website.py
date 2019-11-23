import subprocess
#send a file to the raspberry pi (or any SBC) which is capable of installing relevant programs. This is neccessary every boot due to fruitOs (based on alpine linux) not remembering anything.

ipList = (["192.168.1.10"])#pi 3b+ running fruitOs

def send_files(sf):
    process1 = subprocess.Popen(["scp -o StrictHostKeyChecking=no -i /home/lunet/eljb13/Dropbox/rpi_testbed/ssh-key-for-fruit install-packages-pi.py root@" +ipList[sf]+":/root"], shell=True, stdout=subprocess.PIPE)
    process1.wait()
    process2 = subprocess.Popen(["scp -o StrictHostKeyChecking=no -i /home/lunet/eljb13/Dropbox/rpi_testbed/ssh-key-for-fruit priveleges-nginx-pi.py root@" +ipList[sf]+":/root"], shell=True, stdout=subprocess.PIPE)
    process2.wait()

#now the update has been sent, it is worth checking that this can be run remotely from this script.

def update_remotely(ur):
    process1 = subprocess.Popen(["ssh -i /home/lunet/eljb13/Dropbox/rpi_testbed/ssh-key-for-fruit root@" +ipList[ur]+" 'python3 install-packages-pi.py'"], shell=True, stdout=subprocess.PIPE)
    process1.wait()


def pandoc_tex_to_html():
    process1 = subprocess.Popen(["pandoc --mathjax -s -o index.html quantal_output_equations.tex"], shell=True, stdout=subprocess.PIPE)
    process1.wait()

    
    
def setup_nginx(sn):
    process1 = subprocess.Popen(["ssh -i /home/lunet/eljb13/Dropbox/rpi_testbed/ssh-key-for-fruit root@" +ipList[sn]+" 'python3 priveleges-nginx-pi.py'"], shell=True, stdout=subprocess.PIPE)
    process1.wait()
    process2 = subprocess.Popen(["scp -o StrictHostKeyChecking=no -i /home/lunet/eljb13/Dropbox/rpi_testbed/ssh-key-for-fruit nginx.conf root@" +ipList[sn]+":/etc/nginx"], shell=True, stdout=subprocess.PIPE)
    process2.wait()
    process3 = subprocess.Popen(["scp -o StrictHostKeyChecking=no -i /home/lunet/eljb13/Dropbox/rpi_testbed/ssh-key-for-fruit index.html root@" +ipList[sn]+":/www"], shell=True, stdout=subprocess.PIPE)
    process3.wait()
    process4 = subprocess.Popen(["ssh -i /home/lunet/eljb13/Dropbox/rpi_testbed/ssh-key-for-fruit root@" +ipList[sn]+" 'rc-service nginx start'"], shell=True, stdout=subprocess.PIPE)
    process4.wait()
    process5 = subprocess.Popen(["ssh -i /home/lunet/eljb13/Dropbox/rpi_testbed/ssh-key-for-fruit root@" +ipList[sn]+" 'nginx -t'"], shell=True, stdout=subprocess.PIPE)
    process5.wait()
    process6 = subprocess.Popen(["ssh -i /home/lunet/eljb13/Dropbox/rpi_testbed/ssh-key-for-fruit root@" +ipList[sn]+" 'python3 priveleges-nginx-pi.py'"], shell=True, stdout=subprocess.PIPE)
    process6.wait()
    process7 = subprocess.Popen(["ssh -i /home/lunet/eljb13/Dropbox/rpi_testbed/ssh-key-for-fruit root@" +ipList[sn]+" 'rc-service nginx start'"], shell=True, stdout=subprocess.PIPE)
    process7.wait()
    process8 = subprocess.Popen(["ssh -i /home/lunet/eljb13/Dropbox/rpi_testbed/ssh-key-for-fruit root@" +ipList[sn]+" 'nginx -t'"], shell=True, stdout=subprocess.PIPE)
    process8.wait()


pandoc_tex_to_html()    
send_files(0)
update_remotely(0)
setup_nginx(0)
