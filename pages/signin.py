from nicegui import ui

@ui.page("/signin")

def show_signin_page():
    #  Adding the fontawesome icons
    ui.add_head_html("<script src='https://kit.fontawesome.com/ccba89e5d4.js' crossorigin='anonymous'></script>")
     
    with ui.element("div").classes("w-full h-screen flex flex-row m-0 p-0 gap-0"):
        
        with ui.column().classes('w-1/2 h-full bg-white flex flex-col justify-center items-center p-4'):
            with ui.row().classes('items-center'):
                ui.label('Event').classes('text-2xl font-bold text-blue-500 mb-8')
                ui.label('Hive').classes('text-2xl font-bold text-pink-600 mb-8')

            ui.label('Sign In to Event Hive').classes('text-3xl font-bold text-grey-800 mb-8')

            # Input fields
            ui.input('YOUR EMAIL', placeholder='Enter your email').classes('w-3/4').props("outlined")
            ui.input('PASSWORD', placeholder='Enter your password', password=True, password_toggle_button=True).classes('w-3/4').props("outlined")
           
            ui.link('Forgot your password?', '#').classes('text-xs text-purple-600 no-underline hover:underline')

            ui.button('Sign In', icon='fa-solid fa-arrow-right-to-bracket').classes('w-1/4 text-white font-bold rounded-sm shadow').props("color=blue-500")
            ui.label('Or').classes('text-blue-500')
            ui.button('Sign in with Google', icon='fa-brands fa-google').classes("px-8").props("color=pink-600")

        with ui.element("div").classes("bg-[url('https://www.shutterstock.com/image-photo/crowd-young-people-dancing-night-260nw-213032347.jpg')] bg-cover bg-center flex flex-col w-1/2 h-full justify-center items-center"):
            with ui.column().classes("items-center"):
                ui.label("Hello Friend").classes("text-white text-4xl font-bold mb-4")
                ui.label("To keep connected with us provide us with your information").classes("text-white mb-4")
                # ui.button("Sign Up").classes("bg-transparent shadow-2xl shadow-white blur-[2px]").props("label=Sign")
                with ui.button(text=None).classes('relative px-4 flex items-center justify-center bg-transparent border-none'):
            
                    # The blurred overlay
                    ui.element('div').classes('absolute inset-0 backdrop-blur-sm bg-white/30')
            
                    # The text label (must be a separate element to avoid being blurred)
                    ui.label('Signin').classes('relative z-10 text-white font-semibold text-sm')
            
