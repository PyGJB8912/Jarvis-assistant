import speech_recognition as sr
import gtts


class Write:
    def write(self, text, directory, lang):
        tts = gtts.gTTS(text=text, lang=lang, slow=False)
        tts.save(directory)


class Read:
    def read_file(self, file, lang):
        rec_vocale = sr.Recognizer()
        with sr.AudioFile(file) as src:
            audio = rec_vocale.record(src)

        try:
            text = rec_vocale.recognize_google(audio, language=lang)
            return text

        except sr.UnknownValueError:
            return "UnknownValueError"

        except sr.RequestError:
            return "Request Error"

    def getMicInput(self, lang):
        rec_vocale = sr.Recognizer()

        with sr.Microphone() as source:
            rec_vocale.adjust_for_ambient_noise(source)
            audio = rec_vocale.listen(source)

        try:
            command = rec_vocale.recognize_google(audio, language=lang)
            return command

        except sr.UnknownValueError:
            return "UnknownValueError"

        except sr.RequestError:
            return "Request Error"
