from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer
from components.event_card import show_event_card
import requests
from utils.api import base_url


@ui.page("/")
def show_home_page():
    ui.query(".nicegui-content").classes("m-0 p-2 gap-0")
    show_navbar()

    # hero page
    with ui.element("main").classes("w-full h-screen px-10"):
        with ui.element("div").style("background-image:url(assets/img3.jpg)").classes(
            "w-full h-[80%] brightness-70 flex flex-col bg-no-repeat bg-black/60 bg-cover bg-center"
        ):

            with ui.column().classes(
                "relative z-10 w-full h-full flex justify-center items-center space-y-6 text-center font-poppin"
            ):
                ui.label("Made For Those").classes(
                    "text-bold items-center text-white uppercase"
                ).style("font-size:4rem;")
                ui.label("Who Do").classes(
                    "text-bold items-center self-center text-white uppercase"
                ).style("font-size: 4rem;")

                with ui.row().classes(
                    "absolute  bg-blue-800 rounded-xl gap-3 shadow-lg p-4 w-11/12 md:w-3/4 mx-auto flex justify-around flex -bottom-10 left-0 right-0"
                ):
                    with ui.column():

                        #   Event type select
                        with ui.column().classes():
                            Choose_Location = [
                                "Choose Location",
                                "Online",
                                "On Campus",
                                "Library",
                                "Private Venue",
                                "Cafe",
                                "City Center",
                                "Stadium",
                                "Auditorium",
                                "Conference Room",
                            ]
                            ui.select(
                                label="",
                                value="Choose Location",
                                options=Choose_Location,
                            ).props("dense outlined").classes("bg-white px-10")
                    with ui.column():
                        Choose_Event_Type = [
                            "Choose_Event_Type",
                            "Party",
                            "Meetup",
                            "Seminar",
                            "Workshop",
                            "Festival",
                            "Concert",
                            "Sports",
                            "Food & Drinks",
                        ]
                    ui.select(
                        label="", value="Choose_Event_Type", options=Choose_Event_Type
                    ).props("dense outlined").classes("bg-white px-10")
                    with ui.column():
                        Choose_Date = [
                            "Choose_Date",
                            "Today",
                            "Monday",
                            "Tuesday",
                            "Wednesday",
                            "Thursday",
                            "Friday",
                            "Saturday",
                            "Sunday",
                        ]
                    ui.select(label="", value="Choose_Date", options=Choose_Date).props(
                        "dense outlined"
                    ).classes("bg-white px-10")
                    ui.button(icon="search").classes(
                        "bg-deep-purple-600 text-white rounded-sm p-3 hover:bg-indigo-700"
                    )

    # upcoming event
    with ui.row().classes("h-full flex flex-row justify-between items-center"):
        ui.label("Upcoming Event").classes("text-4xl font-bold")
        with ui.row():
            ui.select(["Weekdays"])
            ui.select(["Event type"])
            ui.select(["Any category"])

    with ui.grid(columns=3).classes("w-full"):
        response = requests.get(f"{base_url}/events?limit=10")
        json_data = response.json()

        for event in json_data["data"]:
            show_event_card(event)

        # CTA button centered
    with ui.column().classes("items-center self-center"):
        ui.button("Load more...").classes(
            "mt-12 px-10 py-3 bg-pink hover:bg-blue-700 text-white "
            "rounded-md text-base font-medium mx-auto"
        )

    with ui.row().classes(
        "relative w-full h-[30%] mt-16  py-12 flex flex-row items-center justify-center"
    ):
        # with ui.element("div").classes('w-1/3 relative h-full'):
        ui.image("/assets/ierr.png")

    # with ui.column().classes("items-center w-1/3 justify-center text-center flex flex-col"):
    #     ui.label("Make your own event").classes("text-white text-3xl font-bold")
    #     ui.label("lorem ipsum dolor sit amet consectetur adipiscing elit").classes("justify-left text-white text-sm")
    #     ui.button("Create Events").classes("text-white justify-left bg-purple-200")

    # Brand Section
    with ui.element("div").classes("p-4 border-2 border-gray-300 rounded-md w-full"):
        ui.image("/assets/image1.png")

    # Trending colleges

    with ui.row().classes("flex flex-row justify-between w-full items-center"):
        ui.label("Trending College").classes("text-4xl text-blue-500 font-bold")
    with ui.grid(columns=3).classes("w-full"):
        for i in range(3):
            with ui.card():
                ui.image("/assets/unileed.jpg").classes("w-full h-40 object-cover")
                ui.button("Register").classes(
                    "w-full bg-blue-300 text-white py-2 rounded-ig"
                )

                # Our Blogs

    with ui.element("div").classes("p-4 border-2 border-white rounded-md"):
        with ui.row().classes("flex flex-row justify-between w-full items-center"):
            ui.label("Our blog").classes("text-4xl font-bold")

        # List of images (replace with your own image paths)
        images = ["/assets/vblog.jpg", "/assets/vlog1.png", "/assets/vlog2.jpg"]

        with ui.grid(columns=3).classes("w-screen gap-4"):
            for img in images:
                with ui.card():
                    ui.image(img).classes("w-full h-50 object-cover")
                    ui.button("Register").classes(
                        "w-full bg-blue-300 text-white py-2 rounded-lg"
                    )
    # with ui.element('div').classes('p-4 border-2 border-white rounded-md'):
    #  with ui.row().classes("flex flex-row justify-between w-full items-center"):
    #     ui.label("Our blog").classes("text-4xl font-bold")

    # with ui.grid(columns=3).classes("w-full"):
    #     for i in range(3):
    #         with ui.card():
    #             ui.image("/assets/vblog.jpg").classes("w-full h-40 object-cover")
    #             ui.button("Register").classes(
    #                 "w-full bg-blue-300 text-white py-2 rounded-ig"
    # )

    show_footer()
