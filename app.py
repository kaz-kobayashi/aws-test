# app.py
from nicegui import ui

@ui.page('/')
def main_page():
    ui.label('Hello from NiceGUI on AWS App Runner!')
    ui.button('Click me!', on_click=lambda: ui.notify('Button clicked!'))

ui.run(host='0.0.0.0', port=8080)