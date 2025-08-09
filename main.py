import os; os.environ.setdefault("PYGLET_HEADLESS","True")
import arcade

W,H=600,600; CELL=60
class App(arcade.Window):
    def __init__(self): super().__init__(W,H,"Grid"); self.cx=self.cy=0
    def on_draw(self):
        self.clear()
        for x in range(0,W+1,CELL): arcade.draw_line(x,0,x,H,arcade.color.GRAY)
        for y in range(0,H+1,CELL): arcade.draw_line(0,y,W,y,arcade.color.GRAY)
        arcade.draw_rectangle_outline(self.cx*CELL+CELL/2,self.cy*CELL+CELL/2,
                                      CELL,CELL,arcade.color.YELLOW,3)
    def on_key_press(self,key,mod):
        if key==arcade.key.RIGHT and self.cx< W//CELL-1: self.cx+=1
        if key==arcade.key.LEFT  and self.cx>0: self.cx-=1
        if key==arcade.key.UP    and self.cy< H//CELL-1: self.cy+=1
        if key==arcade.key.DOWN  and self.cy>0: self.cy-=1
if __name__=="__main__": arcade.run()
