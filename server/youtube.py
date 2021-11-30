import ctypes
import os
from winreg import *

from flask import Flask, blueprints, jsonify, request
from pytube import Playlist
from pytube import YouTube as YT
from pytube import exceptions
import pytube

YouTube = blueprints.Blueprint('YouTube', __name__, url_prefix='/YouTube')

module = {"name": "YouTube","version": "0.0.1"}

with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
    Downloads = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]

@YouTube.route('/', methods=['GET'])
def youtube_index():
    return jsonify({
        "module": module,
        "status": "working"}
        )



@YouTube.route('/convert', methods=['get'])
def youtube_convert():
    url = request.headers.get('url', 'ERROR:URL')
    type = request.headers.get('type', 'ERROR:TYPE')
    
    print("[+] Convert request received")
    print("[i] URL: " + url)
    print("[i] TYPE: " + type)
    print("[i] Path: " + Downloads)

    try:
        yt = YT(url)
        print("[+] Video found")
        print("[+] Starting download")
        yt.streams.filter().get_highest_resolution().download(output_path=Downloads, filename=f"{yt.title}.{type}")
        print("[+] Converted & Downloaded")

        resp = ctypes.windll.user32.MessageBoxW(0, f'"{yt.title}.{type}" downloaded do you want to open "{Downloads}"?', "YouTube-Converter", 4)
        if  resp == 6:
            os.system("start "+Downloads)
        else:
            pass  
        
    except Exception as e:
        print("[!] Error downloading: " + str(e))
        return jsonify({
            "module": module,
            "status": "error",
            "error": str(e)
            })
    except exceptions.RegexMatchError as e:
        print("[!] Error downloading: " + str(e))
        return jsonify({
            "module": module,
            "status": "Couldn't find video! Check URL!",
            "error": str(e)
            })
    except exceptions.VideoUnavailable as e:
        print("[!] Error downloading: " + str(e))
        return jsonify({
            "module": module,
            "status": "Video Unavailable!",
            "error": str(e)
            })

    return jsonify({
        "module": module,
        "function": {
            "name": "convert",
            "type": type,
            "url": url,
        },
        "status": "working"
        })
