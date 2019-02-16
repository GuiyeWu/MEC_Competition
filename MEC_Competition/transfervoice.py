from gtts import gTTS
import pygame

class transfer:
    def initial(self):
        ttsfirst = gTTS("Please enter you voice")
        ttsfirst.save("initial.mp3")
        pygame.mixer.music.load("initial.mp3")
        pygame.mixer.music.play()
    def tovoice(self,sent):
        self.sent = sent
        tts = gTTS(self.sent)
        tts.save("tovoice.mp3")
        pygame.mixer.music.load("tovoice.mp3")
        pygame.mixer.music.play()
    def urgentvoice():
        pygame.init()
        pygame.mixer.music.load("Emergency.mp3")
        pygame.mixer.music.play()
