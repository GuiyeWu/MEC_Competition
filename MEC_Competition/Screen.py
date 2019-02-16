import pygame
import sys
from pygame.locals import *
from transfervoice import *
from gtts import gTTS

class Board:
    def __init__(self,x,y):
        pygame.init()
        self.screen = pygame.display.set_mode((x,y),pygame.DOUBLEBUF)
        self.xcoord = x
        self.ycoord = y
        self.WHITE = [255,255,255]
        self.BLACK = [0,0,0]
        self.RED = [255,0,0]
        self.font = pygame.font.SysFont('Arial', 70)
        self.font1 = pygame.font.SysFont('Arial', 35)
        self.running = True
        self.KeyboardTop = ["Q","W","E","R","T","Y","U","I","O","P"]
        self.KeyboardMid = ["A","S","D","F","G","H","J","K","L"]
        self.KeyboardBot = ["Z","X","C","V","B","N","M"]
        self.Keyboard = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"," "]
        self.letters = []
        self.count = 0
        self.count2 = 0
        self.sentence = ""
        self.keyWid = self.xcoord/12

    def on_init(self):
        pygame.init()
        keyWid = self.xcoord/12
        keyHei = self.ycoord/8
        self.screen.fill(self.WHITE)
        pygame.draw.rect(self.screen, self.BLACK, [self.xcoord/15, self.ycoord/3.3, (self.xcoord-2*self.xcoord/15), self.ycoord/10], 1)
        pygame.draw.rect(self.screen, self.BLACK, [self.xcoord/15+(self.xcoord-2*self.xcoord/15)/3, self.ycoord/3.3, (self.xcoord-2*self.xcoord/15)/3, self.ycoord/10], 1)
        #output textbox
        pygame.draw.rect(self.screen, self.BLACK, [self.xcoord/15, self.ycoord/15, self.xcoord-2*self.xcoord/15, self.ycoord/5], 1)
        #Emergency
        pygame.draw.rect(self.screen, self.RED, [self.xcoord/15, self.ycoord/3+3*(self.ycoord/8 +self.ycoord/120), self.xcoord/10, self.ycoord/6], 0)       
        #Enter
        pygame.draw.rect(self.screen, self.BLACK, [self.xcoord/15+9*(keyWid+self.xcoord/1000), self.ycoord/3+3*(self.ycoord/8 +self.ycoord/120), self.xcoord/10, self.ycoord/6], 1)
        self.screen.blit(self.font1.render("ENTER",True,self.BLACK),(self.xcoord/15+9*(keyWid+self.xcoord/1000), self.ycoord/3+3*(self.ycoord/8 +self.ycoord/40)))
        #Space
        pygame.draw.rect(self.screen, self.BLACK, [self.xcoord/15+3.5*(keyWid+self.xcoord/1000), self.ycoord/3+4*(self.ycoord/8 +self.ycoord/120), (self.xcoord-2*self.xcoord/15)/3, self.ycoord/10], 1)
        self.screen.blit(self.font1.render("Space",True,self.BLACK),(self.xcoord/15+4.8*(keyWid+self.xcoord/1000), self.ycoord/3+4*(self.ycoord/8 +self.ycoord/120)))

        for i in range(10):
            pygame.draw.rect(self.screen, self.BLACK, [self.xcoord/12+i*(keyWid+self.xcoord/1000), self.ycoord/3+keyHei, keyWid, keyHei], 1)
            self.screen.blit(self.font.render(self.KeyboardTop[i],True,self.BLACK),(self.xcoord/12+keyWid/4+i*(keyWid+self.xcoord/1000), self.ycoord/3+(keyHei+self.ycoord/250)))
            self.letters.append(pygame.rect.Rect(self.xcoord/12+i*(keyWid+self.xcoord/1000), self.ycoord/3+keyHei, keyWid, keyHei))
        for i in range(9):
            pygame.draw.rect(self.screen, self.BLACK, [self.xcoord/8+i*(keyWid+self.xcoord/1000), self.ycoord/3+2*(keyHei+self.ycoord/200), keyWid, keyHei], 1)
            self.screen.blit(self.font.render(self.KeyboardMid[i],True,self.BLACK),(self.xcoord/8+keyWid/4+i*(keyWid+self.xcoord/1000), self.ycoord/3+2*(keyHei+self.ycoord/250)))
            self.letters.append(pygame.rect.Rect(self.xcoord/8+i*(keyWid+self.xcoord/1000), self.ycoord/3+2*(keyHei+self.ycoord/200), keyWid, keyHei))
        for i in range(7):
            pygame.draw.rect(self.screen, self.BLACK, [self.xcoord/4.8+i*(keyWid+self.xcoord/1000), self.ycoord/3+3*(keyHei+self.ycoord/150), keyWid, keyHei], 1)
            self.screen.blit(self.font.render(self.KeyboardBot[i],True,self.BLACK),(self.xcoord/4.8+keyWid/4+i*(keyWid+self.xcoord/1000), self.ycoord/3+3*(keyHei+self.ycoord/250)))
            self.letters.append(pygame.rect.Rect(self.xcoord/4.8+i*(keyWid+self.xcoord/1000), self.ycoord/3+3*(keyHei+self.ycoord/150), keyWid, keyHei))
        self.letters.append(pygame.rect.Rect(self.xcoord/15+3.5*(self.keyWid+self.xcoord/1000), self.ycoord/3+4*(self.ycoord/8 +self.ycoord/120), (self.xcoord-2*self.xcoord/15)/3, self.ycoord/10))
        pygame.display.flip()
        

    def on_event(self,event):
        if event.type == pygame.QUIT  or (event.type == KEYUP and event.key == K_ESCAPE):
            self.running = False
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                r = pygame.rect.Rect(pygame.mouse.get_pos(),(1,1))
                for i in range(27):
                    rct = self.letters[i]
                    letter = self.Keyboard[i]
                    enter = pygame.rect.Rect(self.xcoord/15+9*(self.keyWid+self.xcoord/1000), self.ycoord/3+3*(self.ycoord/8 +self.ycoord/120), self.xcoord/10, self.ycoord/6)
                    emergency = pygame.rect.Rect(self.xcoord/15, self.ycoord/3+3*(self.ycoord/8 +self.ycoord/120), self.xcoord/10, self.ycoord/6)
                    if rct.colliderect(r):
                        self.screen.blit(self.font1.render(letter,True,self.BLACK),(self.xcoord/15+self.count*20, self.ycoord/15+self.count2*25, self.xcoord-2*self.xcoord/15, self.ycoord/5))
                        self.sentence += letter
                        self.count += 1
                        pygame.display.flip()
                    if enter.colliderect(r):
                        transfer.tovoice(self,self.sentence)
                        self.count = 0
                        self.count2 += 1
                        break
                    if emergency.colliderect(r):
                        transfer.urgentvoice()
                        break
                                             
   
    
    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        transfer.initial(self)
        if self.on_init() == False:
            self.running = False
        
        while(self.running):
            for event in pygame.event.get():
                self.on_event(event)
            
        self.on_cleanup()

if __name__ == "__main__":
    theBoard = Board(1000,600)
    theBoard.on_execute()
    

