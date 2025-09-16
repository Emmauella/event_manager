from nicegui import ui

def show_navbar():
    with ui.row():
        ui.link("signup" , "/signup")
        ui.link("signin" , "/signin")
        ui.link("Create Event" , "/create_event")
        ui.link("event" , "/event")


  
