###################################################################simple bounce game##################################################

from tkinter import *
import random
import time
root =Tk()
root.title("BOUNCE")
root.resizable(0,0)##screen size fixed now

canvas=Canvas(root,width=500,height=500,bd=0,highlightthickness=0)##bd=border...highlighthickness is also related to border
canvas.pack()
root.update()
class ball:
    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        self.paddle=paddle
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,225,100)
        start=[-3,-2,-1,0,1,2,3]
        random.shuffle(start)
        self.x=start[0]
        self.y=-3
        self.canheight=500
        self.canwi=500
        self.hit_bottom=False



    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        
        if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                
                return True
            return False
        

    def draw(self):
        
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)##.coords return an array with x1,y1,x2,y2
        
        if pos[1]<=0:
            self.y=1
        if pos[3]>=500:
            self.hit_bottom=True
            canvas.create_text(245,100,text="GAME OVER")
            
        if pos[0]<=0:
            self.x=3
        if pos[2]>=500:
            self.x=-3
        if self.hit_paddle(pos)==True:
            self.y=-3
            
           
      

        
            

            
class paddle:
    def left(self,evt):
        self.x=-2

    def right(self,evt):
        self.x=2

        
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,450)
        self.x=0
        self.canvas.bind_all('<Left>',self.left)
        self.canvas.bind_all('<KeyPress-Right>',self.right)


    def draw(self):
         self.canvas.move(self.id,self.x,0)
         pos=self.canvas.coords(self.id)
         if pos[0]<0:
             self.x=2
         if pos[2]>500:
             self.x=-2
         
             
    
      
paddle=paddle(canvas,"pink")
ball=ball(canvas,paddle,"light green")

while 1:
    if ball.hit_bottom==False:
        ball.draw()
        paddle.draw()
    
    root.update()
    time.sleep(0.01)
    




root.mainloop()
