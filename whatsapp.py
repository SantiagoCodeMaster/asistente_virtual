import webbrowser
import pyautogui as at
import time

def send_message(contacte,message):
    webbrowser.open(f"https://web.whatsapp.com/send?phone{contacte}&text={message}")
    time.sleep(8)
    at.press('enter')
    

