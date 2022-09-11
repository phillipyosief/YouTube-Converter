import os
import socket
import ctypes
from winreg import *

from flask import Flask, jsonify, redirect, request
from flask_cors import CORS

from server.youtube import YouTube
from server.web import Web

app = Flask(__name__)
CORS(app)

localip = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in
           [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]


@app.route('/install_extension')
def install_extension():
    pass


@app.route('/')
def index():
    return jsonify({"status": "working"})


def init_app():
    """
    Init of the App and the routes for the API
    """
    print("[+] Starting Server")
    print("[i] Listening on {}:{}".format("127.0.0.1", 5000))
    print("[i] Registering blueprints")

    bps = [YouTube, Web]
    for bp in bps:
        try:
            app.register_blueprint(bp)
            print("[i] Registered {}".format(bp.name))
        except Exception as e:
            print("[!] Error registering blueprint: {}".format(e))
            
            if bp is YouTube:
                ctypes.windll.user32.MessageBoxW(0, f'Your YouTube-Converter installation is broken!\n "Cannot register YouTube Blueprint"', "YouTube-Converter", 4)
                exit()
    
    print(app.url_map)


def main():
    """
    Main function of the app (with tray, etc.)
    """

    init_app()
    app.run(port=5000, debug=False)   # Flask server 


if __name__ == '__main__':
    main()
