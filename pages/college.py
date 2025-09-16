from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer

@ui.page("/college")

def show_college_page():
    ui.label("This is the College page")