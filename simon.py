from pygame import *
from random import *
init()

w = 960
h = 720
win = display.set_mode((w,h))
display.set_caption("Cool Game")
font = font.SysFont("consolas", 44)
beep1 = mixer.Sound('simon/beep1.ogg')
beep2 = mixer.Sound('simon/beep2.ogg')
beep3 = mixer.Sound('simon/beep3.ogg')
beep4 = mixer.Sound('simon/beep4.ogg')

class GameSprite(sprite.Sprite):
    def __init__(self,filename,x,y):
        sprite.Sprite.__init__(self)
        self.image = image.load(filename)
        self.rect = self.image.get_rect(center=(x,y))
        self.x = x
        self.y = y
    def draw(self):
        win.blit(self.image,self.rect)
    def draw(self):
        win.blit(self.image,self.rect)
bg = GameSprite("simon/bg.png",w//2,h//2)
default = GameSprite("simon/default.png",w//2,h//2)
game = True

buttons = []
playerb = []
p = 0
frames = 5
extra = 10
step = 1 ### 1 - generate; 2 - show; 3 - click; 4 - check
level = 0
shownum = 0

def showme(what,frames,extra):
   global p,shownum
   if p < frames:
       p = p + 1
   else:
       if p == frames:
           if(what == 1): beep1.play()
           elif(what == 2): beep2.play()
           elif(what == 3): beep3.play()
           else: beep4.play()
       if p >= frames+extra:
           p = 0
           default.image = image.load("simon/default.png")
           shownum = shownum + 1
       else:
           p = p + 1
           default.image = image.load("simon/c"+str(what)+".png")

def drawtext(title):
    text = font.render(title, True, (0,255,0))
    wtext = text.get_width()
    htext = text.get_height()
    x = (w - wtext) // 2
    y = (h - htext) // 2	
    win.blit(text, (x, y))
      
while game:
    time.delay(15)
#    print(step)
    if step == 3 and shownum == level:
        title = "Click"
    else:
        title = str(level)
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN and step == 3:
            if shownum < level:
                if (mouse.get_pos()[0] < w//2 - 50) and (mouse.get_pos()[1] < h//2 - 50):
#                    print("TOPLEFT")
                    playerb.append(1)
                elif (mouse.get_pos()[0] > w//2 + 50) and (mouse.get_pos()[1] < h//2 - 50):
#                    print("TOPRIGHT")
                    playerb.append(2)
                elif (mouse.get_pos()[0] > w//2 + 50) and (mouse.get_pos()[1] > h//2 + 50):
#                    print("BOTTOMRIGHT")
                    playerb.append(3)
                elif (mouse.get_pos()[0] < w//2 - 50) and (mouse.get_pos()[1] > h//2 + 50):
#                    print("BOTTOMLEFT")
                    playerb.append(4)
            else:
                default.image = image.load("simon/default.png")
                shownum = 0
                step = step + 1

    win.fill((66,66,66))

    bg.draw()

    if step == 1:
       level = level + 1
       b = randint(1,4)
       buttons.append(b)
       step = step + 1
    if step == 2:
        if shownum < len(buttons):
            showme(buttons[shownum],frames,extra)
        else:
            shownum = 0
            step = step + 1
            playerb.clear()
    if step == 3 and len(playerb)>0:
       if shownum < len(playerb):
           showme(playerb[shownum],frames,extra)
    if step == 4:
       if buttons == playerb:
           step = 1
           print("NEXT LEVEL")
       else:
           print("YOU LOSE!!!")
           game = False
    default.draw()
    drawtext(title)
    display.update()

quit()
