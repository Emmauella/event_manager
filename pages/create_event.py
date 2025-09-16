from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer

@ui.page("/create_event")

# def show_create_event_page():
#     ui.label("This is the Create Event page")

# --- REUSABLE EVENT FORM COMPONENT ---
def show_create_event():
    with ui.column().classes('w-full max-w-4xl mx-auto p-8 my-10 bg-white rounded-xl shadow-lg'):
        ui.label('Create Event').classes('text-3xl font-bold text-center text-gray-800 mb-8')

        with ui.row().classes('w-full flex-wrap gap-4'):
            # Left column for inputs
            with ui.column().classes('flex-1 min-w-[300px] space-y-4'):
                ui.label('Event Title').classes('text-base font-semibold text-gray-700')
                ui.input(placeholder='Event Title').classes('w-full rounded-lg border-2 border-gray-200 p-3')

                ui.label('Event Venue').classes('text-base font-semibold text-gray-700')
                ui.input(placeholder='Event Venue').classes('w-full rounded-lg border-2 border-gray-200 p-3')
                
                # Start and End Date
                with ui.row().classes('w-full gap-4'):
                    with ui.column().classes('flex-1'):
                        ui.label('Start date').classes('text-base font-semibold text-gray-700')
                        ui.input(placeholder='Start date').classes('w-full rounded-lg border-2 border-gray-200 p-3')

                    with ui.column().classes('flex-1'):
                        ui.label('End date').classes('text-base font-semibold text-gray-700')
                        ui.input(placeholder='End date').classes('w-full rounded-lg border-2 border-gray-200 p-3')

                # Start and End Time
                with ui.row().classes('w-full gap-4'):
                    with ui.column().classes('flex-1'):
                        ui.label('Start time').classes('text-base font-semibold text-gray-700')
                        ui.input(placeholder='Start time').classes('w-full rounded-lg border-2 border-gray-200 p-3')
                    
                    with ui.column().classes('flex-1'):
                        ui.label('End time').classes('text-base font-semibold text-gray-700')
                        ui.input(placeholder='End time').classes('w-full rounded-lg border-2 border-gray-200 p-3')
            
            # Right column for description and image
            with ui.column().classes('flex-1 min-w-[300px] space-y-4'):
                ui.label('Event Description').classes('text-base font-semibold text-gray-700')
                ui.textarea(placeholder='Type here...').classes('w-full h-32 rounded-lg border-2 border-gray-200 p-3')
                
                ui.label('Event Image').classes('text-base font-semibold text-gray-700')
                ui.upload(label='Event Image', on_upload=lambda e: ui.notify(f'Uploaded {e.name}')).classes('w-full rounded-lg border-2 border-gray-200 p-3')

        # Create Event Button
        ui.button('Create event', on_click=lambda: ui.notify('Event created!')).classes('w-full bg-indigo-600 text-white rounded-lg p-4 mt-8 font-semibold hover:bg-indigo-700 transition-colors')


# --- CREATE EVENT PAGE ---
@ui.page('/new_event')
def show_create_event_page():
    show_create_event()  # reuse the form here


# --- RUN APP (only if testing this file directly) ---

    ui.run(title="Event Hive - Create Event", reload=True)