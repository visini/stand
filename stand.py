import rumps

from ssh_set_desk_height import ssh_set_desk_height


class StandApp(object):
    def __init__(self):
        self.app = rumps.App("Stand", "⚡")

    @rumps.clicked("Sit")
    def sit(self):
        ssh_set_desk_height(10)

    @rumps.clicked("Stand")
    def stand(self):
        ssh_set_desk_height(90)

    def run(self):
        self.app.run()


if __name__ == "__main__":
    app = StandApp()
    app.run()
