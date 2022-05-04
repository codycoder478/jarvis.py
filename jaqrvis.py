import wolframalpha
client = wolframalpha.Client("KPEX8R-ETR24VPLRK")
import wikipedia

import PySimpleGUI as sg
sg.theme('DarkPurple')
layout =[[sg.Text('Enter a command'), sg.InputText()],[sg.Button('Ok'), sg.Button('Cancel')]]
window = sg.Window('PyDa', layout)

import pyttsx3
engine = pyttsx3.init()

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    try:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking("Wolfram Result: "+wolfram_res,"Wikipedia Result: "+wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        engine.say(wiki_res)
        sg.PopupNonBlocking(wiki_res)

    engine.runAndWait()

    print (values[0])


window.close()


def voicerecognition(self):
    sg.theme('DarkPurple')
    layout = [[sg.Button("Press and Speak"), sg.Button('Cancel')]]
    self.speechrecogwindow = sg.Window("Speech Recognition Assistant", layout)

    while True:
        event, values = self.speechrecogwindow.read()
        if event in (None, "Press and Speak"):
            self.speechrecogwindow.close()
            self.recog(self.r)
            break
        if event in (sg.WIN_CLOSED, 'Cancel'):
            self.speechrecogwindow.close()
            quit()

        def recog(self, rec_obj):
            while True:
                wolfram_res = None
                with self.mic as source:
                    print("Speak")
                    rec_obj.adjust_for_ambient_noise(source)
                    audio = rec_obj.listen(source)
                    try:
                        response = rec_obj.recognize_google(audio)
                    except(sr.UnknownValueError):
                        quit("Could not recognize")
                try:
                    wolfram_res = next(client.query(response).results).text
                    engine.say(wolfram_res)
                    engine.runAndWait()
                    layout = [[sg.Text(wolfram_res)], [sg.Button('Ok')]]
                    self.popup = sg.Window('Popup', layout)
                    while True:
                        event, values = self.popup.read()
                        if event in (sg.WIN_CLOSED, 'Ok'):
                            self.popup.close()
                            break
                    self.voicerecognition()
                except(StopIteration):
                    print("Could not find answer")
                    self.voicerecognition()

    if __name__ == "__main__":
        jarvis = Jarvis(sr.Microphone(), sr.Recognizer())

