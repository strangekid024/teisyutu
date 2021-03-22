import getch

class Map:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.hero = Hero(3,3,self.is_movable,self.get_message,self.draw)
        self.townpeople = []
        self.townpeople.append(Townman(3,1,buyer,"what do u want?"))
        self.townpeople.append(Townman(2,1,k,"i am wating"))
        self.townpeople.append(Townman(1,1,k,"dont cross me"))
    def get message(self,x,y):#町人の隣の座標の場合メッセージを受け取ることができる
        for townman in townpeople:
            if x == townman.x and y == townman.y:
                return townman.message
            return 'daremoinai'
    def run(self):
        self.hero.run()
    def is_movable(self,x,y):
        if x < 0:
            return False
        elif self.width-1 < x:
            return False
        elif self.height-1 < y:
            return False
        elif y < 0:
            return False
        #町人と重ならないための判定
        for townman in self.townpeople:
            if x == townman.x and y == townman.y:
                return False
        return True
    def draw(self):
        characters = {}
        characters[(self.hero.x,self.hero.y)] = self.hero.icon
        characters[(townman.x,townman.y)] = townman.icon
    #画面に現在の状態を絵画する描くもののリストを作ってjoinでつなげて出力する
        def get_row(y):
            row_list = []
            row_list.append('|') #行の左端
            for x in range(0 ,self.width):
                if (x,y) in characters:
                    row_list.append(characters[(x,y)]) #x,yの座標にいるキャラを座標から辞書にアクセスしてアイコンを取り出すことで書いている
                else:
                    row_list.append('') #キャラいなかったら空白
            row_list.append('|\n') #横の長さ分１個１個のx軸を確かめたら右端に枠を描いて改行する
            return ".join(row_list)
        map_list = []
        map_list.append(' + {} + \n'.format('_'*self.width)) #一番上の枠
        for y in range(0,self.width):
            map_list.append(get_row(y)) #上で決めた横方向へのオブジェクトの展開をたて１行１行でやることでyoko*tateで二次元に展開している
        map_list.append(' + {} + \n'.format('_'*self.width))
        map_list.append('=============='+ '\n')
        map_list.append(message + '\n')
        map_list.append('=============='+ '\n')


        print(".join(map_list))

class Townman:
    def __init__(self,x,y,icon,message):
        self.x = x
        self.y = y
        self.icon = icon
        self.message = message