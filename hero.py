# coding:utf-8
import getch
import map

KEY_CTRL_C = 3
KEY_W = 119
KEY_A = 97
KEY_S = 115
KEY_Z = 122
class Hero:
    def __init__(self, x ,y ,icon = "^",is_movable,draw_map):  #マップクラスにあるヒーローに関わるメソッドを受け取るために引数にメソッドを定義
        self.x = x
        self.y = y
        self.icon = icon
        self.is_movable = is_movable
        self.draw_map = draw_map
    def run(self):
        print('-----------------')
        print("w:up,a:left,s:right,z:down")
        print("ctrl-c:quit")
        print("-----------------")
        self.draw_map()


        while(True):
            key = ord(getch.getch()) #ord関数で入力したキーボードを数値化して扱う
            if key == KEY_CTRL_C:
                print("bye")
                break
            elif key == KEY_W: #is_movableで確認してから
                self.icon = '^'
                if(self.is_movable(self.x,self.y-1)):self.y -= 1
            elif key == KEY_A:
                self.icon = '<'
                if(self.is_movable(self.x-1,self.y)):self.x -= 1
            elif key == KEY_S:
                self.icon = '>'
                if(self.is_movable(self.x+1,self.y)):self.x += 1
            elif key == KEY_Z:
                self.icon = 'v'
                if(self.is_movable(self.x,self.y+1)):self.y += 1
            elif key == KEY_D:
                message = self.talk()
            else:
                continue
    def talk(self):
        message = ''
        if self.icon == '^':
            message = self.get_message(self.x,self.y-1)
            #上を向いているのでx軸は同じだけどメッセージとして受け取るべき場所の座標は向いてる方に一つズレたところ
        elif self.icon == '<':
            message = self.get_message(self.x-1,self.y)
        elif self.icon == '>':
            message = self.get_message(self.x+1,self.y)
        elif self.icon == 'v':
            message = self.get_message(self.x,self.y+1)
        return message
    self.draw_map(message)
