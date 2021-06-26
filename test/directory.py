
# I will be using paramike module . It will help me to execute remote shell commands.
# http://www.fabfile.org/

import paramiko
import os
import subprocess
import sys

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("computer_name", username="username", password="password", allow_agent = False)

def add_user():
# Ask for the input
username = input("Enter Username ")
password = 123445

def mkdir(folder_absolute_path):
    """
    creates new folder
    """
run('mkdir {0}'.format(folder_absolute_path))




    











