from dearpygui.dearpygui import *

from resources.variables import Product, Tag, Path


def show():
    with window(tag=Tag.PrimaryWindow):
        add_text("")  # Placeholder

        with group(horizontal=True):
            with child_window(tag=Tag.ImageChildWindow, width=150, height=150, border=False):
                width, height, channels, data = load_image('resources/app/icon.png')
                with texture_registry():
                    image = add_static_texture(width, height, data)
                size = 150

                add_image(image, width=size, height=size, parent=Tag.ImageChildWindow)
            with group(horizontal=False):
                with group(horizontal=True):
                    add_text('Path')
                    add_input_text(width=450, hint=Path.Downloads)

                    add_button(label='Browse', width=75)
                with group(horizontal=True):
                    add_text('URL ')
                    add_input_text(width=450)
                    add_combo(items=['mp3', 'mp4'], default_value='mp3', width=75)

                add_separator()

                add_button(label='Download', width=570)
    create_viewport(title=Product.Name,
                    width=750, height=430,
                    resizable=False,
                    decorated=False)
