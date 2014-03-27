# going off of http://dtucker.co.uk/hack/ssh-for-python-in-search-of-api-perfection.html
from sys import argv
import paramiko
import getpass

script, ip, usr = argv

#print "%s" % ip

# prompts user for password
pw = getpass.getpass()

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
client.connect(ip, username=usr, password=pw)

# alternative to using getpass, just configure the password as it's set below:
# client.connect("192.168.1.6", username="itadmin", password="password")

stdn, stdout, stderr = client.exec_command('sudo touch /User/%s/Desktop/virus_inject') % usr
for line in stdout:
    print line.strip ('\n')
#stdn, stdout, stderr = client.exec_command('ls -ltr')
#for line in stdout:
#    print line.strip ('\n')
client.close()