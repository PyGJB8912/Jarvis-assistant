from jarvis import read_write as rw
import os


def hello():
    text = "bonjour jean"

    write = rw.Write()
    write.write(text=text, directory="/home/hacker-man/Bureau/Jarvis/sounds/hello.mp3", lang="fr-FR")

    os.system("mpg123 " + "/home/hacker-man/Bureau/Jarvis/sounds/hello.mp3")


class Commands:
    def __init__(self, command, type):
        self.command = command
        self.type = type

        # the list of all commands
        self.commands = {"Hello": hello()}

        # the definition of the commands
        self.defintions = {}

    def search(self):
        if self.type == "command":
            function = self.commands[self.command]
            function()

        elif self.type == "help":
            definition = self.commands[self.defintions]
            return definition
