#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from config_file import ConfigFile

app = Flask(__name__)

conf = ConfigFile.instance()

adminmessage = conf.get_property('adminmessage')
admindata = conf.get_property('admindata')

@app.route("/")
def sendbirdtakehome():
#    return "Hello SendBird Takehome"
#    return adminmessage
    return admindata

if __name__ == "__main__":
    try:
        service_port=int(conf.get_property('service.port'))
    except ValueError:
        service_port=5000
        
    service_host = conf.get_property('service.host')
    service_debug = bool(conf.get_property('service.debug'))
    
    app.run(host=service_host, port=service_port, debug=service_debug)
