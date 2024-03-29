import pyttsx3 as pyt


class Convert:

    def __init__(self, path):
        self.engine = pyt.init()
        with open(path, "r") as file:
            self.file = file.read()

    def say(self):
        self.engine.say(self.file)
        self.engine.runAndWait()


if __name__ == "__main__":
    convert = Convert("test")
    convert.say()
