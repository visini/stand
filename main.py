import rumps

from ssh_desk_handler import SSHDeskHandler

SEC_TO_MIN = 1


class StandApp(object):
    def __init__(self):

        self.timer = rumps.Timer(self.on_tick, 1)
        self.timer.stop()
        self.timer.count = 0
        self.interval = 5 * SEC_TO_MIN  #  5 Minutes

        self.app = rumps.App("Stand", "⚡")
        self.desk_handler = SSHDeskHandler()

        self.stand_button = rumps.MenuItem(
            title="↑ Stand", callback=lambda _: self.stand()
        )

        self.sit_button = rumps.MenuItem(
            title="↓ Sit", callback=lambda _: self.sit()
        )

        self.buttons = {}
        self.buttons_callback = {}

        for h, i in enumerate([5, 10, 15, 20, 25]):
            title = "Stand for " + str(i) + " Minutes"
            callback = lambda _, min=i: self.stand_for_n_mins(min)
            self.buttons["btn_" + str(i)] = rumps.MenuItem(
                title=title,
                callback=callback,
                key=str(h + 1),
            )
            self.buttons_callback[title] = callback

        self.stop_button = rumps.MenuItem(title="Stop Timer", callback=None)

        self.app.menu = [
            self.stand_button,
            self.sit_button,
            None,
            *self.buttons.values(),
            None,
            self.stop_button,
        ]

    def sit(self):
        self.desk_handler.down()

    def stand(self):
        self.desk_handler.up()

    def stand_for_n_mins(self, mins):
        # print("stand_for_n_mins:", mins)
        self.interval = mins * SEC_TO_MIN
        self.start_timer(self.interval)
        self.desk_handler.up()

    def on_tick(self, sender):
        time_left = sender.end - sender.count
        # print("on_tick, time_left", time_left)
        mins = time_left // 60 if time_left >= 0 else time_left // 60 + 1
        secs = time_left % 60 if time_left >= 0 else (-1 * time_left) % 60
        if mins == 0 and time_left < 0:
            rumps.notification(
                title="Stand",
                subtitle="Time is up! Have a seat :)",
                message="",
            )
            self.stop_timer()
            self.stop_button.set_callback(None)
        else:
            self.stop_button.set_callback(self.stop_timer)
            self.app.title = "⚡ {:2d}:{:02d}".format(mins, secs)
        sender.count += 1

    def start_timer(self, interval):
        # print("start_timer")
        self.timer.count = 0
        self.timer.end = interval
        self.timer.start()

    def stop_timer(self, sender=None):
        self.timer.stop()
        self.timer.count = 0
        self.app.title = "⚡"
        self.stop_button.set_callback(None)
        self.sit()

    def run(self):
        self.app.run()


if __name__ == "__main__":
    app = StandApp()
    app.run()
