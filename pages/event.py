from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer

@ui.page("/event")

def show_event_page():
    ui.label("This is the event page")
