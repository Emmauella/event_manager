from nicegui import ui
from components.navbar import show_navbar
import requests
from utils.api import base_url

# from components.footer import show_footer

_event_image = None


def _handle_image_upload(event):
    global _event_image
    _event_image = event.content


def _post_event(data, files):
    response = requests.post(f"{base_url}/events", data=data, files=files)
    print(response.status_code, response.content)
    if response.status_code == 200:
        ui.notify(message="Event added Successfully!", type="Postitve")
        return ui.navigate.to("/")
    elif response.status_code == 422:
        return ui.notify(message="Please ensure all input are filled!", type="negative")

    # print(response.status_code)


@ui.page("/create_event")

# --- REUSABLE EVENT FORM COMPONENT ---
def show_create_event():
    show_navbar()
    with ui.column().classes(
        "w-full max-w-4xl mx-auto p-8 my-10 bg-blue-100 rounded-xl shadow-lg"
    ):
        ui.label("Create Event").classes(
            "text-3xl font-bold text-center text-pink-600 mb-8"
        )

        with ui.row().classes("w-full flex-wrap gap-4"):
            # Left column for inputs
            with ui.column().classes("flex-1 min-w-[300px] space-y-4"):
                ui.label("Event Title").classes("text-base font-semibold text-gray-700")
                event_title = ui.input(placeholder="Event Title").classes(
                    "w-full rounded-lg border-2 border-gray-200 p-3"
                )

                ui.label("Event Venue").classes("text-base font-semibold text-gray-700")
                event_venue = ui.input(placeholder="Event Venue").classes(
                    "w-full rounded-lg border-2 border-grey p-3"
                )

                # Start and End Date
                with ui.row().classes("w-full gap-4"):
                    with ui.column().classes("flex-1"):
                        ui.label("Start date").classes(
                            "text-base font-semibold text-gray-700"
                        )
                        event_start_date = (
                            ui.input(placeholder="Start date")
                            .props("type=date")
                            .classes("w-full rounded-lg border-2 border-gray-200 p-3")
                        )

                    with ui.column().classes("flex-1"):
                        ui.label("End date").classes(
                            "text-base font-semibold text-gray-700"
                        )
                        event_end_date = (
                            ui.input(placeholder="End date")
                            .props("type=date")
                            .classes("w-full rounded-lg border-2 border-gray-200 p-3")
                        )

                # Start and End Time
                with ui.row().classes("w-full gap-4"):
                    with ui.column().classes("flex-1"):
                        ui.label("Start time").classes(
                            "text-base font-semibold text-gray-700"
                        )
                        event_start_time = (
                            ui.input(placeholder="Start time")
                            .props("type=time")
                            .classes("w-full rounded-lg border-2 border-gray-200 p-3")
                        )

                    with ui.column().classes("flex-1"):
                        ui.label("End time").classes(
                            "text-base font-semibold text-gray-700"
                        )
                        event_end_time = (
                            ui.input(placeholder="End time")
                            .props("type=time")
                            .classes("w-full rounded-lg border-2 border-gray-200 p-3")
                        )

            # Right column for description and image
            with ui.column().classes("flex-1 min-w-[300px] space-y-4"):
                ui.label("Event Description").classes(
                    "text-base font-semibold text-gray-700"
                )
                event_description = ui.textarea(placeholder="Type here...").classes(
                    "w-full h-32 rounded-lg border-2 border-gray-200 p-3"
                )

                ui.label("Event Image").classes("text-base font-semibold text-gray-700")
                ui.upload(
                    label="Event Image",
                    on_upload=_handle_image_upload,
                ).classes("w-full rounded-lg border-2 border-gray-200 p-3").props(
                    "color=pink"
                )

        # Create Event Button
        ui.button(
            "Create Event",
            on_click=lambda: _post_event(
                data={
                    "title": event_title.value,
                    "venue": event_venue.value,
                    "start_time": event_start_time.value,
                    "end_time": event_end_time.value,
                    "start_date": event_start_date.value,
                    "end_date": event_end_date.value,
                    "description": event_description.value,
                },
                files={"image": _event_image},
            ),
        ).classes(
            "w-full bg-indigo-600 text-white rounded-lg p-4 mt-8 font-semibold hover:bg-indigo-700 transition-colors"
        )
        

# --- CREATE EVENT PAGE ---
@ui.page("/new_event")
def show_create_event_page():
    show_create_event()  # reuse the form here

    # --- RUN APP (only if testing this file directly) ---

    ui.run(title="Event Hive - Create Event", reload=True)
