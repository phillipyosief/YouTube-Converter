from winreg import *


class Product:
    Name = "YouTube-Converter"
    Version = "0.0.3"
    Author = "philliphqs"


class Tag:
    ImageChildWindow = "ImageChildWindow"
    PrimaryWindow = "PrimaryWindow"


class Path:
    with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
        Downloads = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
        Music = QueryValueEx(key, 'My Music')[0]


class URL:
    GitHub = "https://github.com/philliphqs/YouTube-Converter"
    Website = "https://philliphqs.github.io"

    Quickstart = "https://github.com/philliphqs/YouTube-Converter/#Installation"
    Support = "https://philliphqs.github.io/support.html#faq"


class Assets:
    class Icons:
        Download = "resources/icons/download.ico"
        Icon = "resources/Icon-1024.ico"
        Firefox = "resources/icons/firefox.ico"
        Chrome = "resources/icons/chrome.ico"
        cover = "resources/icons/cover.png"
        icon = "resources/app/icon.ico"
        Bug = "resources/icons/bug.ico"
        Feature = "resources/icons/feature.ico"
        GitHub = "resources/icons/github.ico"

    class Images:
        Background = "resources/icons/background.png"
