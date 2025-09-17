from nicegui import ui 



def show_footer():

    ui.add_head_html('<script src="https://kit.fontawesome.com/ccba89e5d4.js" crossorigin="anonymous"></script>')

    with ui.element("div").classes("w-full bg-blue-800 items-center justify-center px-10 py-5"):
        with ui.row().classes("items-center justify-center text-4xl font-bold mb-4"):
            ui.label("Event").classes("text-white")
            ui.label("Hive").classes("text-pink-400")

        with ui.row().classes("items-center justify-center text-white mb-8 gap-0"):
            ui.input(placeholder="Enter your mail").props("outlined").classes("bg-white w-64")
            ui.button("Subscribe").props("color=pink-400").classes("px-20 py-4")

        ui.html("<hr>").classes("mt-16")

        with ui.element("div").classes("flex flex-row justify-between text-white px-4 py-8 items-center text-center"):
            with ui.row():
                ui.label("English")
                ui.label("French")
                ui.label("Russian")

            with ui.row().classes("text-white text-xl"):
                ui.html('<i class="fa-brands fa-facebook"></i>').classes("hover:text")
                ui.html('<i class="fa-brands fa-instagram"></i>')
                ui.html('<i class="fa-brands fa-twitter"></i>')

            with ui.row():
                ui.html("<p>© Copyright 2025 | Emmanuella Dodoo | All Rights Reserved</p>")

