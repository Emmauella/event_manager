from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer
from components.event_card import show_event_card
import requests
from utils.api import base_url


@ui.page("/event")

def show_event_page():
    
    ui.label("This is the event page")
from nicegui import ui


def show_event_page():
  show_navbar()
    # Render header at the top level
  from nicegui import ui
import random

# Some random Unsplash image categories for variety
HERO_IMAGES = [
    "https://static.vecteezy.com/system/resources/previews/026/846/193/non_2x/a-magical-waterfall-in-a-wonderfully-fantastic-flowering-landscape-banner-made-with-generative-ai-photo.jpg",
    # "https://loveincorporated.blob.core.windows.net/contentimages/gallery/32a644e7-50ab-4435-9e12-5013eea5382f-crater-lake-maroon-bells-usa.jpg",
   ]

MAP_IMAGES = [
    "https://img.freepik.com/free-photo/top-view-globe-world-map_23-2148909590.jpg",
    "https://img.freepik.com/free-photo/top-view-globe-world-map_23-2148909590.jpg",

]

@ui.page('/event')
def show_event_page():
    show_navbar()
    event_id = ui.context.client.request.query_params.get("id")
    response = requests.get(f"{base_url}/events/{event_id}")
    if response.status_code==200:
        json_data = response.json()
        event = json_data["data"]
    
        hero_image = random.choice(HERO_IMAGES)
        map_image = random.choice(MAP_IMAGES)

        # === PAGE CONTAINER ===
        with ui.element('div').classes(
            'max-w-[1320px] mx-auto mt-[40px] bg-white rounded-[10px] shadow-lg overflow-hidden'
        ):
            # === HERO SECTION ===
            with ui.column().classes(
                f" bg-[url('{event["image"]})] bg-cover bg-center rounded-t-[10px] overflow-hidden relative h-[600px]"
            ):
                # Overlay
                ui.element('div').classes('absolute inset-0 bg-black/50')

                # Back Button
                with ui.element('a').classes(
                    'absolute top-[30px] left-[30px] flex items-center gap-2 px-4 py-2 '
                    'bg-blue-700 text-white rounded shadow-md cursor-pointer hover:bg-pink-700'
                ):
                    ui.icon('arrow_back').classes('text-white')
                    ui.label('Back').classes('text-white text-[16px]')

                # HERO TEXT
                with ui.element('div').classes(
                    'absolute top-[150px] left-[60px] max-w-[600px] flex flex-col gap-6'
                ):
                    ui.label(text=event["title"]).classes(
                        'text-[64px] font-bold text-white leading-tight drop-shadow-lg'
                    )
                    ui.label('IIIT Sonepat').classes(
                        'text-[36px] font-bold text-white drop-shadow'
                    )
                    ui.label(text=event["description"]).classes('text-white text-[16px] leading-relaxed max-w-[550px]')
                    # View Map link
                    with ui.element('div').classes(
                        'flex items-center gap-2 text-white mt-2 underline cursor-pointer'
                    ):
                        ui.icon('place')
                        ui.label('View map').classes('text-[18px]')

                # EVENT INFO CARD (Right Side)
                with ui.element('div').classes(
                    'absolute top-[140px] right-[60px] w-[385px] bg-white rounded-[10px] shadow-xl p-6 flex flex-col gap-6'
                ):
                    ui.label('Date & Time').classes('text-[24px] font-bold text-blue-600')
                    ui.separator().classes('bg-blue-200')
                    ui.label('Saturday, March 18 2023, 9.30PM').classes('text-pink-700 text-[18px]')
                    ui.label('Add to calendar').classes('text-blue-500 text-[16px] cursor-pointer')
                    ui.separator().classes('bg-blue-200')

                    # Signup Buttons
                    with ui.element('div').classes('flex flex-col gap-3 mt-2'):
                        ui.button('Book Now').classes(
                            'w-full text-white rounded-[5px] py-3 hover:bg-blue-400'
                        )
                        ui.button('Program Promoter').classes(
                            'w-full text-white rounded-[5px] py-3 bg-pink-500 hover:bg-blue-300'
                        )

                    ui.label('No Refunds').classes('text-center text-blue-600 text-[16px] mt-2')

            # === MAIN CONTENT BELOW HERO ===
            with ui.element('section').classes(
                'p-10 bg-blue-100 grid grid-cols-1 md:grid-cols-3 gap-[40px]'
            ):
                # LEFT COLUMN
                with ui.element('div').classes('md:col-span-2 flex flex-col gap-[40px]'):
                    # Description
                    with ui.element('div').classes('flex flex-col gap-4'):
                        ui.label('Description').classes('text-[28px] font-bold text-pink-400')
                        ui.label(
                            'This workshop introduced participants to the world of 3D modeling. '
                            'It was designed for both beginners and advanced learners, covering everything '
                            'from the basics of Blender to rendering competitions.'
                        ).classes('text-black text-[18px] leading-relaxed')

                    # Hours
                        with ui.element('div').classes('flex flex-col gap-4'):
                            ui.label('Hours').classes('text-[28px] font-bold text-black')

                    with ui.element('div').classes('flex items-center gap-2 text-[18px]'):
                        ui.label('Weekdays hour:').classes('text-blue-700')
                        ui.label('7PM - 10PM').classes('text-black font-semibold')

                    with ui.element('div').classes('flex items-center gap-2 text-[18px]'):
                        ui.label('Sunday hour:').classes('text-blue-700')
                        ui.label('7PM - 10PM').classes('text-black font-semibold')

                    # Organizer Contact
                    with ui.element('div').classes('flex flex-col gap-4'):
                        ui.label('Organizer Contact').classes('text-[28px] font-bold text-pink-400')
                        ui.label(
                            'Please go to www.emma11@.com and refer the FAQ section for more detail.'
                        ).classes('text-blue-700 text-[18px] leading-relaxed')

                # RIGHT SIDEBAR
                with ui.element('div').classes('flex flex-col gap-[40px]'):
                    # Location
                    with ui.element('div').classes(
                        'flex flex-col gap-4 bg-white p-4 rounded-[10px] shadow'
                    ):
                        ui.label('Event Location').classes('text-[24px] font-bold text-black')
                        ui.element('div').classes(
                            f"w-full h-[220px] rounded-[10px] bg-[url('{map_image}')] bg-cover"
                        )
                        ui.label('Dream world wide in Jakarta').classes(
                            'text-[20px] font-semibold text-black'
                        )
                        ui.label(
                            'Dummy location model by RSU... generates more realistic dummy locations.'
                        ).classes('text-pink-700 text-[16px] leading-relaxed')

                    # Tags
                    with ui.element('div').classes(
                        'flex flex-col gap-3 bg-white p-4 rounded-[10px] shadow'
                    ):
                        ui.label('Tags').classes('text-[24px] font-bold text-black')
                        with ui.element('div').classes('flex flex-wrap gap-2'):
                            for tag in ['Design', '3D', 'Workshop', 'Blender',]:
                                ui.label(tag).classes(
                                    'px-4 py-1.5 bg-blue-400 rounded text-[14px]'
                                )

                    # Share
                    with ui.element('div').classes(
                    'flex flex-col gap-3 bg-white p-4 rounded-[10px] shadow'
                ):
                        ui.label('Share with friends').classes('text-[24px] font-bold text-blue-600')

                    with ui.element('div').classes('flex gap-4'):
                        with ui.element('a').props('href=https://facebook.com target=_blank'):
                            ui.icon('fa-brands fa-facebook-f').classes('text-pink-500 text-[28px]')
                        with ui.element('a').props('href=https://linkedin.com target=_blank'):
                            ui.icon('fa-brands fa-linkedin-in').classes('text-[#0A66C2] text-[28px]')
                        with ui.element('a').props('href=https://twitter.com target=_blank'):
                            ui.icon('fa-brands fa-twitter').classes('text-[#1DA1F2] text-[28px]')
                        with ui.element('a').props('href=https://wa.me/123456789 target=_blank'):
                            ui.icon('fa-brands fa-whatsapp').classes('text-[#25D366] text-[28px]')
    elif response.status_code ==422:
        ui.label("Something went wrong!")  
        
    with ui.row().classes("flex flex-row justify-between w-full items-center"):
         ui.label("Other events you may like").classes("text-2xl text-blue-500 font-bold")
    with ui.grid(columns=3).classes("w-full"):
        for i in range(6):
            with ui.card():
                ui.image("/assets/unileed.jpg").classes("w-full h-40 object-cover")
                ui.button("Register").classes(
                    "w-full bg-blue-300 text-white py-2 rounded-ig"
                )
             
    show_footer()