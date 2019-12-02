import paramiko

ip = '192.168.11.15'
user = 'pi'
passwd = 'pi'
command = 'sudo python /boot/Pi_Eyes/eyes.py'
##command = 'sudo reboot'


client = paramiko.SSHClient()
client.load_system_host_keys()
##client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(ip, 22, user, passwd)
stdin, stdout, stderr = client.exec_command(command)

client.close()