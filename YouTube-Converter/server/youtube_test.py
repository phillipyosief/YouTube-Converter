import unittest
from unittest.main import main
import requests


class TestYoutube(unittest.TestCase):
    def convert(type, url):
        r = requests.get('http://127.0.0.1:2222/YouTube/convert', headers={'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', "type": "mp3"})

        print(r.text)


if __name__ == '__main__':
    one = input("[i] YouTube Tester\n"
          "[i] Functions to test:\n"
          "    1. Convert")
    if one == "1":
        url = input("[i] Enter the URL of the video you want to convert: ")
        if url == "":
            TestYoutube.convert("mp3", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        else:
            TestYoutube.convert("mp3", url)
    else:
        print("[!] Invalid input")
