import rumps
import subprocess


class CpuTemperature(object):
    def __init__(self):
        self.config = {
            "app_name": "MacOS CPU Temperature",
            "start": "Check CPU Temperature",
            "pause": "Pause Timer",
            "interval": 100,
        }
        self.app = rumps.App(self.config["app_name"])
        self.timer = rumps.Timer(self.on_tick, 3)
        self.interval = self.config["interval"]
        self.set_up_menu()
        self.start_pause_button = rumps.MenuItem(
            title=self.config["start"], callback=self.start_timer
        )
        self.app.menu = [self.start_pause_button]

    def set_up_menu(self):
        self.timer.count = 0
        self.app.title = "🌡"

    def on_tick(self, sender):
        # init count
        sender.count = 1
        current_temp = subprocess.check_output(["./osx-cpu-temp", "-F"]).decode(
            "utf-8", "ignore"
        )[:5]
        self.app.title = "🌡 " + current_temp + "° F"
        sender.count += 1

    def start_timer(self, sender):
        if sender.title.lower().startswith(("check", "continue")):
            if sender.title == self.config["start"]:
                self.timer.count = 0
                self.timer.end = self.interval
            self.start_pause_button.set_callback(None)
            self.timer.start()
        else:
            sender.title = self.config["continue"]

    def run(self):
        self.app.run()


if __name__ == "__main__":
    app = CpuTemperature()
    app.run()
