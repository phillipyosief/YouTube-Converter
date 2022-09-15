from dearpygui.dearpygui import *

from resources.variables import Product, Tag

from app.ui import NavBar, Tags, Window

create_context()


def dragViewport():
    drag_deltas = get_mouse_drag_delta()
    viewport_current_pos = get_viewport_pos()
    set_viewport_pos([viewport_current_pos[0] + drag_deltas[0], viewport_current_pos[1] + drag_deltas[1]])


def start_app(systray: None):
    Window.show()
    NavBar.show()

    with handler_registry():
        add_mouse_drag_handler(callback=dragViewport)

    setup_dearpygui()
    show_viewport()
    set_primary_window(Tag.PrimaryWindow, True)
    start_dearpygui()
    destroy_context()


if __name__ == '__main__':
    start_app()
