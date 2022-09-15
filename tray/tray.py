import threading
import webbrowser
from infi.systray import SysTrayIcon
import ctypes

from main import close

from resources.variables import Product, Assets
from app.backend import interaction

from app.run import start_app


def close_sys(systray):
    close()


def download_addon_firefox(systray):
    webbrowser.open_new_tab("https://addons.mozilla.org/en-US/firefox/addon/youtube-converter")


def download_addon_chrome(systray):
    ctypes.windll.user32.MessageBoxW(0,
                                     f'Chrome is not supported yet! Because YouTube-Converter is not published on the Chrome Web Store yet.',
                                     Product.Name, 0)


menu_options = (('Report a bug', Assets.Icons.Bug, interaction.report_a_bug),
                ('Request a feature', Assets.Icons.GitHub, interaction.request_a_feature),
                ('Download addon', Assets.Icons.Download,
                 (('Firefox', Assets.Icons.Firefox, download_addon_firefox),
                  ('Chrome', Assets.Icons.Chrome, download_addon_chrome),
                  ))
                )


def start(systray: None):
    systray = SysTrayIcon(Assets.Icons.icon, Product.Name, menu_options)
    systray.start()
