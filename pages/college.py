from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer

@ui.page("/college")

# def show_college_page():
#     ui.label("This is the College page")

def show_college_page():
    """Render the trending colleges page with responsive, centered cards."""
    
    with ui.column().classes("w-full px-6 sm:px-1 lg:px-24 py-12 gap-6 items-start"):
        # Heading
        ui.html('''
            <h2 style="
                font-family: 'Roboto', sans-serif;
                font-weight: 700;
                font-size: 36px;
                line-height: 42px;
                margin: 0;
                spacing: 0;
            ">
                Trending <span style="color:#7848F4;">Colleges</span>
            </h2>
        ''')
        # College data
        colleges = [
            {
                "name": "Harvard University",
                "location": "Cambridge, Massachusetts, UK",
                "image": "/assets/colleges/havard.jpg",
                "rating": "4.8",
                "exclusive": True,
            },
            {
                "name": "Stanford University",
                "location": "Stanford, California",
                "image": "/assets/colleges/stanford.jpg",
                "rating": "4.9",
                "exclusive": True,
            },
            {
                "name": "Nanyang University",
                "location": "Nanyang Ave, Singapore",
                "image": "/assets/colleges/nanyang.jpg",
                "rating": "4.7",
                "exclusive": False,
            },
        ]

        # Responsive, centered grid
        with ui.element("div").classes(
            "grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-10 justify-center"
        ):
            for college in colleges:
                with ui.card().classes(
                    "flex flex-col justify-between w-full max-w-[386px] shadow-lg rounded-xl overflow-hidden mx-auto"
                ):
                    # Card image section
                    with ui.element("div").classes(
                        "relative h-[332px] w-full flex items-end justify-between bg-gray-100 rounded-t-l"
                    ):
                        ui.image(college["image"]).classes(
                            "h-full w-full object-contain rounded-t-l"
                        )

                        # Rating badge
                        with ui.element("div").classes(
                            "absolute top-4 left-4 bg-white rounded-full px-3 py-1 flex items-center shadow-md"
                        ):
                            ui.icon("star").classes("text-yellow-400 mr-1")
                            ui.label(college["rating"]).classes("text-sm font-medium")

                        # Exclusive badge
                        if college["exclusive"]:
                            with ui.element("div").classes(
                                "absolute top-4 right-4 bg-deep-purple text-white "
                                "rounded-full px-4 py-2 text-xs font-semibold tracking-wide"
                            ):
                                ui.label("EXCLUSIVE")

                    # College name
                    with ui.element("div").classes("p-5 text-center"):
                        ui.label(college["name"]).classes(
                            "text-xl font-bold text-gray-900"
                        )

                    # Footer with location and more button
                    with ui.element("div").classes(
                        "flex justify-between items-center px-5 pb-5"
                    ):
                        ui.label(college["location"]).classes("text-sm text-gray-600")
                        with ui.button(icon="more_horiz").classes(
                            "bg-gray-200 rounded-full w-12 h-12 right-1.5"
                        ):
                            pass

        # CTA button centered
        ui.button("Load more...").classes(
            "mt-12 px-10 py-3 bg-deep-purple hover:bg-purple-700 text-white "
            "rounded-md text-base font-medium mx-auto"
        )