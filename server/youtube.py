import ctypes
import os

from flask import Flask, blueprints, jsonify, request
from pytube import Playlist
from pytube import YouTube as YT
from pytube import exceptions

from datetime import datetime

YouTube = blueprints.Blueprint('YouTube', __name__, url_prefix='/YouTube')

module = {"name": "YouTube", "version": "0.0.2"}




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

    if type == 'mp4':
        try:
            yt = YT(url)
            print("[+] Video found")
            print("[+] Starting download")
            try:
                yt.streams.filter().get_highest_resolution().download(output_path=Downloads, filename=f"{yt.title}.{type}")
            except:
                # when windows have problems to save the file
                yt.streams.filter().get_highest_resolution().download(output_path=Downloads,
                                                                      filename=f"YouTube-Converter - Invalid file name.{type}")
            print("[+] Converted & Downloaded")



            resp = ctypes.windll.user32.MessageBoxW(0, f'"{yt.title}.{type}" downloaded do you want to open "{Downloads}"?',
                                                    "YouTube-Converter", 4)
            if resp == 6:
                os.system("start " + Downloads)
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
    elif type == 'mp3':
        try:
            yt = YT(url)
            print("[+] Video found")
            print("[+] Starting download")
            try:
                yt.streams.filter(only_audio=True).download(output_path=Downloads,
                                                                      filename=f"{yt.title}.{type}")
            except:
                # when windows have problems to save the file
                yt.streams.filter(only_audio=True).get_audio_only().download(output_path=Downloads,
                                                                      filename=f"YouTube-Converter - Invalid file name.{type}")
            print("[+] Converted & Downloaded")

            resp = ctypes.windll.user32.MessageBoxW(0,
                                                    f'"{yt.title}.{type}" downloaded do you want to open "{Downloads}"?',
                                                    "YouTube-Converter", 4)
            if resp == 6:
                os.system("start " + Downloads)
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