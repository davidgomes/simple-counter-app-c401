from nicegui import ui, app

def create():
    @ui.page('/')
    def index():
        # Add custom CSS for pink theme
        ui.add_head_html('''
        <style>
            .pink-theme {
                background: linear-gradient(135deg, #fce4ec, #f8bbd9);
                min-height: 100vh;
            }
            .pink-counter {
                color: #ad1457;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
            }
            .pink-button {
                background: #e91e63 !important;
                color: white !important;
                border: none !important;
                box-shadow: 0 4px 8px rgba(233, 30, 99, 0.3) !important;
                transition: all 0.3s ease !important;
            }
            .pink-button:hover {
                background: #c2185b !important;
                transform: translateY(-2px) !important;
                box-shadow: 0 6px 12px rgba(233, 30, 99, 0.4) !important;
            }
            .pink-title {
                color: #880e4f;
                text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
            }
        </style>
        ''')
        
        # Initialize counter in user storage to persist across page reloads
        if 'counter' not in app.storage.user:
            app.storage.user['counter'] = 0
        
        # Create the main container with pink theme
        with ui.column().classes('pink-theme items-center justify-center min-h-screen gap-8 p-8'):
            ui.label('Counter').classes('text-5xl font-bold text-center pink-title').mark('title')
            
            # Counter display
            counter_display = ui.label().classes('text-8xl font-bold pink-counter text-center').mark('counter_display')
            
            # Button container
            with ui.row().classes('gap-6 mt-4'):
                decrement_btn = ui.button('-', 
                    icon='remove'
                ).classes('text-3xl px-12 py-6 rounded-full pink-button').mark('decrement_btn')
                
                increment_btn = ui.button('+', 
                    icon='add'
                ).classes('text-3xl px-12 py-6 rounded-full pink-button').mark('increment_btn')
        
        def update_display():
            """Update the counter display with current value"""
            counter_display.set_text(str(app.storage.user['counter']))
        
        def increment():
            """Increment counter and update display"""
            app.storage.user['counter'] += 1
            update_display()
        
        def decrement():
            """Decrement counter and update display"""
            app.storage.user['counter'] -= 1
            update_display()
        
        # Connect button handlers
        increment_btn.on_click(increment)
        decrement_btn.on_click(decrement)
        
        # Initial display update
        update_display()