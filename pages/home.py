from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer


@ui.page("/")
def show_home_page():
    ui.query(".nicegui-content").classes("m-0 p-2 gap-0")
    show_navbar()
    # hero page
    with ui.element("main").classes("w-full h-screen px-10"):
        with ui.element("div").style("background-image:url(assets/img3.jpg)").classes(
            "w-full h-[80%] flex flex-col bg-no-repeat bg-black/80 bg-cover bg-center"
        ):
            with ui.column().classes(
                "items-center flex flex-col justify-center text-center bg-black/50 w-full h-full"
            ):
                ui.label("Made For Those").classes(
                    "text-bold items-center text-white uppercase"
                ).style("font-size:4rem;")
                ui.label("Who Do").classes(
                    "text-bold items-center self-center text-white uppercase"
                ).style("font-size: 4rem;")

    with ui.row().classes("bg-blue-800 p-4 gap-4 items-center justify-center"):
        with ui.column():

            #   Event type select
            ui.select(
                ["Select event type", "Conference", "Workshop", "Concert"],
                value="Select event type",
                with_input=True,
            ).props("Outlined dense").classes("w-1/4 bg-white rounded Ig text-grey-700")

        #  Location select

        #  Date/time input
        ui.input(label="Choose date and time").props("outlined dense").classes(
            "w-1/4 bg-white rounded-Ig text-grey-700"
        )

        # Search button
        ui.button(icon="search").classes(
            "bg-purple-600 text-white rounded-sm p-3 hover:bg-indigo-700"
            "hover:scale-105 transition-all shadow-Ig"
        )

        #     ui.select(
        #         [1,2,3], ).classes("w-60 bg-white",
        #     value="select event type",
        #     with_input=True,).props("outlined")

        # with ui.column():
        #     ui.label("Location").classes("text-white text-semi-bold")
        #     ui.select([1,2,3]).classes("w-60 bg-white").props("outlined")

        # with ui.column():
        #    ui.label("when").classes("text-white text-semi-bold")
        #    choose=ui.select([1,2,3]).classes("w-60 bg-white").props("outlined")

    # upcoming event
    with ui.row().classes("flex flex-row justify-between w-full items-center"):
        ui.label("Upcoming Event").classes("text-4xl font-bold")
        with ui.row():
            ui.select([1, 2, 3])
            ui.select([1, 2, 3])
            ui.select([1, 2, 3])
    with ui.grid(columns=3).classes("w-full"):
        for i in range(6):
            with ui.card():
                ui.image("/assets/iso.jpg").classes("w-full h-40 object-cover")
                ui.button("Register").classes(
                    "w-full bg-blue-300 text-white py-2 rounded-ig"
                )

    show_footer()
