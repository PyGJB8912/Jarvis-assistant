from jarvis import read_write as rw
import os
import datetime


def alarm():
    pass

def hello():
    text = "1 plus 1 égal 11 ! hahaha poisson d'avril"

    write = rw.Write()
    write.write(text=text, directory="/home/hacker-man/Bureau/Jarvis/sounds/hello.mp3", lang="fr-FR")

    os.system("mpg123 " + "/home/hacker-man/Bureau/Jarvis/sounds/hello.mp3")


def date():
    current_time = datetime.datetime.now().time()
    hour = current_time.hour
    minutes = current_time.minute

    text = f"Il est {hour} heure {minutes}"

    write = rw.Write()
    write.write(text=text, directory="/home/hacker-man/Bureau/Jarvis/sounds/date.mp3", lang="fr-FR")

    os.system("mpg123 " + "/home/hacker-man/Bureau/Jarvis/sounds/date.mp3")


class Commands:
    def __init__(self, command, type):
        self.command = command
        self.type = type

        # the list of all commands
        self.commands = {"Hello": hello,
                         "il est quelle heure": date}

        # the definition of the commands
        self.defintions = {}

    def search(self):
        if self.type == "command":
            function = self.commands[self.command]
            function()

        elif self.type == "help":
            definition = self.commands[self.definitions]
            return definition
