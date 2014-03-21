import paramiko
client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
client.connect("192.168.1.6", username="itadmin", password="Columbia456")
stdn, stdout, stderr = client.exec_command('ifconfig en0')
for line in stdout:
    print line.strip ('\n')
stdn, stdout, stderr = client.exec_command('ls -ltr')
for line in stdout:
    print line.strip ('\n')
client.close()