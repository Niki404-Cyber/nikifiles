#coding=utf-8
import os, sys, platform
os.system('rm -rf mac')
os.system('git pull')
try:
    if sys.argv[1]=='update':
        os.system('rm -rf mac')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('mac'):
        os.system('curl -L https://github.com/Niki404-Cyber/nikifiles/blob/main/mac?raw=true -o mac')
        os.system('chmod 777 mac;./mac')
    else:
        os.system('chmod 777 mac;./mac')
