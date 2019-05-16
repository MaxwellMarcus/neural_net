try:
    from tkinter import *
except:
    from Tkinter import *
import time
import random

start = time.time()
time_since_last = 1000

root = Tk()

canvas = Canvas(root,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
canvas.pack()

height = root.winfo_screenheight()
width = root.winfo_screenwidth()
class Player:
    def __init__(self):
        self.collum = 2
        self.avatar = canvas.create_rectangle(0,0,0,0)
        self.dead = False
    def move_left(self,event):
        if self.collum > 1:
            self.collum -= 1
    def move_right(self,event):
        if self.collum < 3:
            self.collum += 1
    def draw(self):
        if not self.dead:
            canvas.delete(self.avatar)
            self.avatar = canvas.create_rectangle(width/4*self.collum-10,height-200,width/4*self.collum+10,height-220,fill='green',outline='green')
class Brick:
    def __init__(self,collum):
        self.collum = collum
        self.avatar = canvas.create_rectangle(0,0,0,0)
        self.y = 0
    def move(self):
        self.y += 2
        if self.y-100 > height:
            del(self)
    def has_hit(self,player):
        if self.collum == player.collum:
            if self.y > height-220 and self.y < height-199:
                player.dead = True
                canvas.delete(player.avatar)
    def show(self):
        canvas.delete(self.avatar)
        self.avatar = canvas.create_rectangle(width/4*self.collum-20,self.y,width/4*self.collum+20,self.y-70,fill='red',outline='red')

player = Player()
bricks = []
canvas.create_line(width/3*2-50,0,width/3*2-50,height,width=5)
canvas.create_line(width/3+50,0,width/3+50,height,width=5)
root.bind('a',player.move_left)
root.bind('d',player.move_right)
while True:
    if (time.time()-start)%5 < .1 and time.time()-time_since_last > 1:
        time_since_last = time.time()
        bricks.append(Brick(random.randint(1,3)))
    for i in bricks:
        i.move()
        i.show()
        i.has_hit(player)

    player.draw()
    root.update()
