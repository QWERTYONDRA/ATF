import keyboard
import time

time.sleep(3) # Wait for 3 seconds to switch to Notepad

text = 'při přejímce zásilky školních potřeb jsme zjistili poškození přepravních beden. Značné poškození zásilky přešetřujeme společně s přepravcem. podle našeho názoru došlo k poškození nešetrnou manipulací při nakládání a vykládání zásilky. dopravce jako důvod poškození uvádí nedostatečné balení zásilky. další zprávu Vám zašleme poštou po sepsání protokolu o škodách. '
delay = 0.39
duration = 9 * 60 # 8 minutes in seconds

start_time = time.time()

while time.time() - start_time < duration:
    for char in text:
        if char.isupper(): # If the character is uppercase
            keyboard.press('Shift')
        keyboard.press(char)
        keyboard.release(char)
        if char.isupper(): # If the character is uppercase
            keyboard.release('Shift')
        time.sleep(delay)