from nicegui import ui


def show_event_card(event):
    with ui.card().on(
        type="click",
        handler=lambda: ui.navigate.to(f"/event?id={event["id"]}")
    ).classes("w-[30rem] h-[25rem] cursor-pointer"):
        ui.image(source=event["image"]).classes("w-full h-40 object-cover")
        ui.label(text=event["title"]).classes("text-bold text-2xl")
        ui.label(text=event["start_date"]).classes("text-bold text-blue-300 text-2xl")
        ui.label(text=event["venue"]).classes("text-bold text-2xl")
            