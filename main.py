from jarvis import read_write as rw
from jarvis import commands
import os


def question(lang):
    while True:
        reader = rw.Read()
        question = reader.getMicInput(lang=lang)

        if question is not None:
            break

    command = commands.Commands(command=question, type="command")
    command.search()


def call(lang):
    reader = rw.Read()
    question = reader.getMicInput(lang)
    if "Jarvis" in question:
        print("Hello Jarvis!")
        os.system("mpg123 " + "/home/hacker-man/Bureau/Jarvis/confirmation-sound.mp3")
        return True

    else:
        return False


def main():
    while True:
        called = call(lang="fr-FR")
        if called == True:
            break

    question("fr-FR")


if __name__ == "__main__":
    main()
