from dearpygui.dearpygui import *

from app.backend import interaction

from app.ui import About


def show():
    with viewport_menu_bar():
        width, height, channels, data = load_image('resources/app/icon.png')
        with texture_registry():
            image = add_static_texture(width, height, data)
        size = 17

        add_image(image, width=size, height=size)

        with menu(label="YouTube-Converter"):
            add_menu_item(label="About", callback=About.show)
            add_separator()
            add_menu_item(label="GitHub", callback=interaction.GitHub)
            add_menu_item(label="Website", callback=interaction.Website)
            add_separator()
            add_menu_item(label="Exit", callback=stop_dearpygui)

        add_spacer(width=505)
        with menu(label="?"):
            add_menu_item(label="Report a bug", callback=interaction.report_a_bug)
            add_menu_item(label="Request a feature", callback=interaction.request_a_feature)
            add_separator()
            add_menu_item(label="Quickstart", callback=interaction.Quickstart)
            add_menu_item(label="Support", callback=interaction.Support)

        add_menu_item(label='_', callback=minimize_viewport)
        add_menu_item(label='X', callback=stop_dearpygui)
