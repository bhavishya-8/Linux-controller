import os

def date_command():
    os.system("start cmd") > os.system("date")
    # os.system("date")


def cal_command():
    os.system("cal")

def ssh_command(ip_address,command):
    ip = ip_address
    os.system(f"ssh -l root {ip} {command}")

def config_httpd():
    os.system("yum install httpd -y && systemctl start httpd --now")





def opt(y):	
		x = int(y)
		if x==1:
			os.system("clear")
			print("You have choosed 1 option")
			date_command()
		elif x==2:
			os.system("clear")
			print("You have choosed 2 option")
			cal_command()
		elif x==3:
			os.system("clear")
			print("You have choosed 3 option")
			ip_address = input("Enter the IP address: ")
			command = input("Enter the command: ")
			ssh_command(ip_address,command)
		elif x==4:
			os.system("clear")
			print("You have choosed to configure the HTTPD server, so you can connect to the IP address 172.16.89.160:80")
			config_httpd()
		elif x==5:
			os.system("clear")
			print("You have choosed 5 option")
			os.system("exit")
