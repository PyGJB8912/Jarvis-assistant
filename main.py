from jarvis import read_write as rw
from jarvis import commands
import os


def main():
    reader = rw.Read()
    question = reader.getMicInput("fr-FR")
    if "Jarvis" in question:
        print("Hello Jarvis!")
        os.system("mpg123 " + "/home/hacker-man/Bureau/Jarvis/confirmation-sound.mp3")


if __name__ == "__main__":
    main()
