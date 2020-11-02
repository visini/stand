import rumps

from ssh_desk_handler import SSHDeskHandler


class StandApp(object):
    def __init__(self):
        self.app = rumps.App("Stand", "⚡")
        self.desk_handler = SSHDeskHandler()

    @rumps.clicked("↑ Stand")
    def stand(self):
        self.desk_handler.up()

    @rumps.clicked("↓ Sit")
    def sit(self):
        self.desk_handler.down()

    def run(self):
        self.app.run()


if __name__ == "__main__":
    app = StandApp()
    app.run()