import rumps
import threading
import subprocess
from pynput import keyboard


class MyApp(rumps.App):
    def __init__(self):
        super(MyApp, self).__init__("MyApp", icon="AI.png", quit_button=None)  # type: ignore
        self.thread = threading.Thread(target=self.run_script)
        self.thread.start()

    def run_script(self):
        subprocess.run([".venv/bin/python3.12", "listen_up.py"])

    @rumps.clicked("Quit")
    def quit(self, _):
        keyboard_controller = keyboard.Controller()
        # press and release cmd + alt + shift + ctrl + q
        keyboard_controller.press(keyboard.Key.cmd)
        keyboard_controller.press(keyboard.Key.alt)
        keyboard_controller.press(keyboard.Key.shift)
        keyboard_controller.press(keyboard.Key.ctrl)
        keyboard_controller.press("q")
        keyboard_controller.release("q")
        keyboard_controller.release(keyboard.Key.ctrl)
        keyboard_controller.release(keyboard.Key.shift)
        keyboard_controller.release(keyboard.Key.alt)
        keyboard_controller.release(keyboard.Key.cmd)

        self.thread.join()
        rumps.quit_application()


if __name__ == "__main__":
    MyApp().run()
