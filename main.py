from typing import Tuple
from typing import List
from graphics import *
import pyautogui

Coord = Tuple[int, int] #coordonnees du pion
Dir = str # "N" ou "S" ou "E" ou "O"
Chemin = List[Dir]
Case=Tuple[bool,bool,bool,bool,str]
Laby=List[List[Case]]
laby1 : Laby = [[(True,True,False,False,""),(False,False,True,False,"ENTREE")],[(True,False,False,True,""),(False,False,True,False,"SORTIE")]]
laby3 : Laby = [[(True, True, False, False, ''), (False, False, True, False, ''), (False, True, False, False, ''), (True, False, False, False, ''), (True, True, True, False, ''), (True, False, True, False, ''), (True, True, True, False, ''), (True, False, True, False, ''), (True, False, True, False, ''), (True, False, True, False, ''), (False, False, True, False, ''), (True, True, False, False, ''), (True, False, True, False, ''), (False, True, True, False, ''), (False, True, False, False, ''), (True, False, False, False, ''), (False, True, True, False, ''), (False, True, False, False, ''), (False, True, False, False, ''), (False, True, False, False, 'ENTREE')], [(True, False, False, True, ''), (False, True, True, False, ''), (True, True, False, True, ''), (True, False, True, False, ''), (True, False, True, True, ''), (False, False, True, False, ''), (False, False, False, True, ''), (True, False, False, False, ''), (True, True, True, False, ''), (True, True, True, False, ''), (True, False, True, False, ''), (True, True, True, True, ''), (False, False, True, False, ''), (False, True, False, True, ''), (False, True, False, True, ''), (True, False, False, False, ''), (True, False, True, True, ''), (False, True, True, True, ''), (False, True, False, True, ''), (False, True, False, True, '')], [(True, True, False, False, ''), (True, True, True, True, ''), (True, False, True, True, ''), (True, True, True, False, ''), (True, False, True, False, ''), (False, True, True, False, ''), (True, False, False, False, ''), (False, True, True, False, ''), (False, False, False, True, ''), (False, True, False, True, ''), (True, False, False, False, ''), (True, True, True, True, ''), (False, False, True, False, ''), (True, False, False, True, ''), (False, True, True, True, ''), (True, False, False, False, ''), (False, True, True, False, ''), (True, False, False, True, ''), (False, True, True, True, ''), (False, True, False, True, '')], [(False, True, False, True, ''), (True, False, False, True, ''), (False, False, True, False, ''), (True, False, False, True, ''), (False, True, True, False, ''), (False, False, False, True, ''), (False, True, False, False, ''), (True, True, False, True, ''), (False, False, True, False, ''), (True, True, False, True, ''), (False, True, True, False, ''), (False, True, False, True, ''), (False, True, False, False, ''), (True, False, False, False, ''), (False, True, True, True, ''), (True, True, False, False, ''), (True, True, True, True, ''), (True, False, True, False, ''), (False, True, True, True, ''), (False, True, False, True, '')], [(True, False, False, True, ''), (True, True, True, False, ''), (False, False, True, False, ''), (True, False, False, False, ''), (False, True, True, True, ''), (True, True, False, False, ''), (True, False, True, True, ''), (False, True, True, True, ''), (True, False, False, False, ''), (False, False, True, True, ''), (False, False, False, True, ''), (True, True, False, True, ''), (True, False, True, True, ''), (False, True, True, False, ''), (True, True, False, True, ''), (False, False, True, True, ''), (False, True, False, True, ''), (False, True, False, False, ''), (False, False, False, True, ''), (False, True, False, True, '')], [(True, False, False, False, ''), (True, True, True, True, ''), (False, False, True, False, ''), (True, False, False, False, ''), (True, False, True, True, ''), (True, True, True, True, ''), (False, True, True, False, ''), (False, False, False, True, ''), (True, True, False, False, ''), (False, False, True, False, ''), (False, True, False, False, ''), (False, False, False, True, ''), (True, False, False, False, ''), (False, False, True, True, ''), (False, True, False, True, ''), (False, True, False, False, ''), (True, False, False, True, ''), (True, True, True, True, ''), (False, False, True, False, ''), (False, True, False, True, '')], [(True, False, False, False, ''), (True, True, True, True, ''), (True, False, True, False, ''), (False, False, True, False, ''), (True, False, False, False, ''), (False, True, True, True, ''), (False, False, False, True, ''), (False, True, False, False, ''), (False, True, False, True, ''), (True, False, False, False, ''), (False, True, True, True, ''), (False, True, False, False, ''), (True, True, False, False, ''), (False, False, True, False, ''), (False, False, False, True, ''), (True, True, False, True, ''), (False, False, True, False, ''), (False, True, False, True, ''), (True, True, False, False, ''), (False, True, True, True, '')], [(True, True, False, False, ''), (True, False, True, True, ''), (False, False, True, False, ''), (True, True, False, False, ''), (True, False, True, False, ''), (False, True, True, True, ''), (False, True, False, False, ''), (False, True, False, True, ''), (False, True, False, True, ''), (True, True, False, False, ''), (True, False, True, True, ''), (False, False, True, True, ''), (False, True, False, True, ''), (True, False, False, False, ''), (False, True, True, False, ''), (True, False, False, True, ''), (True, True, True, False, ''), (True, False, True, True, ''), (False, True, True, True, ''), (False, False, False, True, '')], [(False, False, False, True, ''), (True, True, False, False, ''), (False, True, True, False, ''), (False, False, False, True, ''), (True, False, False, False, ''), (True, False, True, True, ''), (False, True, True, True, ''), (False, True, False, True, ''), (False, True, False, True, ''), (False, True, False, True, ''), (True, False, False, False, ''), (False, True, True, False, ''), (False, True, False, True, ''), (False, True, False, False, ''), (True, True, False, True, ''), (False, False, True, False, ''), (True, False, False, True, ''), (False, True, True, False, ''), (True, False, False, True, ''), (False, True, True, False, '')], [(False, True, False, False, ''), (False, True, False, True, ''), (True, False, False, True, ''), (False, True, True, False, ''), (True, False, False, False, ''), (True, True, True, False, ''), (True, False, True, True, ''), (True, False, True, True, ''), (True, False, True, True, ''), (False, False, True, True, ''), (True, False, False, False, ''), (True, False, True, True, ''), (False, True, True, True, ''), (True, False, False, True, ''), (False, True, True, True, ''), (False, True, False, False, ''), (True, False, False, False, ''), (False, True, True, True, ''), (True, True, False, False, ''), (False, False, True, True, '')], [(True, False, False, True, ''), (False, True, True, True, ''), (True, False, False, False, ''), (True, True, True, True, ''), (True, False, True, False, ''), (True, True, True, True, ''), (True, False, True, False, ''), (False, True, True, False, ''), (False, True, False, False, ''), (False, True, False, False, ''), (True, False, False, False, ''), (False, True, True, False, ''), (True, False, False, True, ''), (True, False, True, False, ''), (True, False, True, True, ''), (False, True, True, True, ''), (True, True, False, False, ''), (False, False, True, True, ''), (True, False, False, True, ''), (False, True, True, False, '')], [(True, False, False, False, ''), (True, False, True, True, ''), (False, False, True, False, ''), (True, False, False, True, ''), (False, True, True, False, ''), (False, True, False, True, ''), (True, False, False, False, ''), (True, False, True, True, ''), (True, False, True, True, ''), (True, False, True, True, ''), (True, False, True, False, ''), (False, False, True, True, ''), (True, True, False, False, ''), (False, True, True, False, ''), (True, True, False, False, ''), (True, True, True, True, ''), (False, True, True, True, ''), (True, False, False, False, ''), (False, True, True, False, ''), (False, False, False, True, '')], [(False, True, False, False, ''), (True, False, False, False, ''), (True, True, True, False, ''), (False, True, True, False, ''), (False, True, False, True, ''), (True, False, False, True, ''), (True, False, True, False, ''), (True, False, True, False, ''), (True, False, True, False, ''), (True, True, True, False, ''), (True, True, True, False, ''), (False, False, True, False, ''), (False, False, False, True, ''), (True, True, False, True, ''), (False, False, True, True, ''), (False, True, False, True, ''), (True, False, False, True, ''), (False, True, True, False, ''), (True, False, False, True, ''), (False, True, True, False, '')], [(False, True, False, True, ''), (True, False, False, False, ''), (False, False, True, True, ''), (False, True, False, True, ''), (True, False, False, True, ''), (True, True, True, False, ''), (False, True, True, False, ''), (True, True, False, False, ''), (True, True, True, False, ''), (False, True, True, True, ''), (True, False, False, True, ''), (False, True, True, False, ''), (True, False, False, False, ''), (True, True, True, True, ''), (False, True, True, False, ''), (True, False, False, True, ''), (False, False, True, False, ''), (True, False, False, True, ''), (False, False, True, False, ''), (False, True, False, True, '')], [(True, False, False, True, ''), (True, False, True, False, ''), (True, True, True, False, ''), (False, True, True, True, ''), (False, True, False, False, ''), (False, False, False, True, ''), (False, True, False, True, ''), (False, False, False, True, ''), (False, False, False, True, ''), (False, True, False, True, ''), (False, True, False, False, ''), (False, True, False, True, ''), (True, False, False, False, ''), (False, False, True, True, ''), (True, False, False, True, ''), (True, False, True, False, ''), (True, True, True, False, ''), (False, False, True, False, ''), (True, True, False, False, ''), (False, False, True, True, '')], [(True, True, False, False, ''), (True, False, True, False, ''), (False, False, True, True, ''), (False, False, False, True, ''), (False, True, False, True, ''), (True, False, False, False, ''), (True, True, True, True, ''), (False, False, True, False, ''), (False, True, False, False, ''), (False, False, False, True, ''), (True, False, False, True, ''), (True, True, True, True, ''), (True, False, True, False, ''), (True, True, True, False, ''), (False, False, True, False, ''), (False, True, False, False, ''), (True, True, False, True, ''), (False, True, True, False, ''), (False, True, False, True, ''), (False, True, False, False, '')], [(True, False, False, True, ''), (True, True, True, False, ''), (False, False, True, False, ''), (False, True, False, False, ''), (True, True, False, True, ''), (False, False, True, False, ''), (True, False, False, True, ''), (True, True, True, False, ''), (False, False, True, True, ''), (True, True, False, False, ''), (False, False, True, False, ''), (True, False, False, True, ''), (False, True, True, False, ''), (True, True, False, True, ''), (False, True, True, False, ''), (True, True, False, True, ''), (False, True, True, True, ''), (True, False, False, True, ''), (False, False, True, True, ''), (False, True, False, True, '')], [(False, True, False, False, ''), (True, False, False, True, ''), (True, True, True, False, ''), (False, False, True, True, ''), (False, True, False, True, ''), (True, True, False, False, ''), (True, True, True, False, ''), (True, True, True, True, ''), (True, False, True, False, ''), (False, False, True, True, ''), (False, True, False, False, ''), (False, True, False, False, ''), (False, False, False, True, ''), (False, False, False, True, ''), (True, True, False, True, ''), (False, True, True, True, ''), (True, False, False, True, ''), (True, True, True, False, ''), (True, True, True, False, ''), (False, False, True, True, '')], [(True, False, False, True, ''), (False, True, True, False, ''), (True, False, False, True, ''), (True, True, True, False, ''), (False, False, True, True, ''), (False, False, False, True, ''), (False, False, False, True, ''), (True, True, False, True, ''), (True, False, True, False, ''), (False, False, True, False, ''), (True, False, False, True, ''), (True, False, True, True, ''), (True, True, True, False, ''), (True, True, True, False, ''), (False, False, True, True, ''), (False, False, False, True, ''), (True, False, False, False, ''), (False, False, True, True, ''), (False, True, False, True, ''), (False, True, False, False, '')], [(True, False, False, False, 'SORTIE'), (True, False, True, True, ''), (True, False, True, False, ''), (True, False, True, True, ''), (True, False, True, False, ''), (True, False, True, False, ''), (True, False, True, False, ''), (True, False, True, True, ''), (True, False, True, False, ''), (True, False, True, False, ''), (False, False, True, False, ''), (True, False, False, False, ''), (False, False, True, True, ''), (True, False, False, True, ''), (False, False, True, False, ''), (True, False, False, False, ''), (True, False, True, False, ''), (True, False, True, False, ''), (True, False, True, True, ''), (False, False, True, True, '')]]

#deplacement du pion
def deplace (c:Coord, d:Dir) -> Coord:
    a,b=c
    if d == "N":
        return (a,b+1)
    elif d == "E":
        return (a+1,b)
    elif d == "S":
        return (a,b-1)
    elif d =="O":
        return (a-1,b)
def deplace_possible(la:Laby, c:Coord, d:str)->bool:
    """
Teste si le deplacement depuis la case c dans la direction d est possible dans le labyrinthe la"""
    x,y=c
    if y> len(la) or x>len(la[0]) or y<0 or x<0:#permet de s'assure que x est dans le labyrinthe
        return False
    n,e,s,o,_=la[x][y]
    return (n and d=="N") or (e and d=="E") or (s and d=="S") or (o and d=="O")
#deplacement selon un itineraire
def deplace_chemin(c:Coord,ch:Chemin)->Coord:
    if ch==[]:
        return c
    else :
        return deplace_chemin(deplace(c,ch[0]),ch[1:])

def dessine_laby(la:Laby,haut:int, larg:int,pion:Coord)->None:
    """Precondition : haut>10 and larg>10"""
    win = GraphWin("mon labii",larg,haut)
    n:bool
    e:bool
    s:bool
    o:bool
    rond:str
    c:int=len(la)
    j:int=0
    i:int=0
    k:int
    a:int
    b:Case
    bordure = 50
    larg1=larg-2*bordure
    haut1=haut-2*bordure
    xpion,ypion=pion
    for a in range(len(la)):
        d:int = len(la[a])
        i=0
        for k in range(d):
            n,e,s,o,rond= la[a][k]
            if n == False:
                p1 = Point(bordure+j*larg1/d,haut-(bordure+(i+1)*haut1/c))
                p2 = Point(bordure+(j+1)*larg1/d,haut-(bordure+(i+1)*haut1/c))
                line=Line(p1,p2)
                line.draw(win)
            if e == False:
                p1 = Point(bordure+(j+1)*larg1/d,haut-(bordure+(i+1)*haut1/c))
                p2 = Point(bordure+(j+1)*larg1/d,haut-(bordure+i*haut1/c))
                line=Line(p1,p2)
                line.draw(win)
            if s == False:
                p1 = Point(bordure+j*larg1/d,haut-(bordure+i*haut1/c))
                p2 = Point(bordure+(j+1)*larg1/d,haut-(bordure+i*haut1/c))
                line=Line(p1,p2)
                line.draw(win)
            if o == False:
                p1 = Point(bordure + j * larg1 / d, haut-(bordure + (i + 1) * haut1 / c))
                p2 = Point(bordure + j * larg1 / d, haut-(bordure + i * haut1 / c))
                line=Line(p1,p2)
                line.draw(win)
            if rond=="ENTREE":
                c1 = (bordure+j*larg1/d + bordure+(j+1)*larg1/d)/2
                c2 = (bordure+(i+1)*haut1/c + bordure+i*haut1/c)/2
                centre = Point(c1, haut-c2)
                rayon = min((larg1/d)/2,(haut1/c)/2)
                cercle = Circle(centre,rayon-15)
                cercle.draw(win)
                cercle.setFill("white")
            elif rond == "SORTIE":
                c1 = (bordure + j * larg1 / d + bordure + (j + 1) * larg1 / d) / 2
                c2 = (bordure + (i + 1) * haut1 / c + bordure + i * haut1 / c) / 2
                centre = Point(c1,  haut-c2)
                rayon = min((larg1 / d) / 2, (haut1 / c) / 2)
                cercle = Circle(centre, rayon - 15)
                cercle.draw(win)
                cercle.setFill("black")
            if k==ypion and a==xpion:
                c1 = (bordure + j * larg1 / d + bordure + (j + 1) * larg1 / d) / 2
                c2 = (bordure + (i + 1) * haut1 / c + bordure + i * haut1 / c) / 2
                centre = Point(c1, haut - c2)
                rayon = min((larg1 / d) / 2, (haut1 / c) / 2)
                cercle = Circle(centre, rayon - 15)
                cercle.draw(win)
                cercle.setFill("pink")

            i=i+1
        j=j+1

    #win.getMouse()# pause for click in window
    #time.sleep(0.3)
    #win.close()


def find_enter(la:Laby)->Coord:
    for a in range(len(la)):
        for b in range(len(la[a])):
            _,_,_,_,use=la[a][b]
            if use=="ENTREE":
                return(a,b)
def find_exit(la:Laby)->Coord:
    for a in range(len(la)):
        for b in range(len(la[a])):
            _,_,_,_,use=la[a][b]
            if use=="SORTIE":
                return(a,b)

def main():
    la=laby3
    pion:Coord=find_enter(la)
    exit:Coord=find_exit(la)
    #dessine_laby(la, 500, 1000, pion)
    larg = 1000
    haut = 500
    win = GraphWin("mon labii", larg, haut)
    n: bool
    e: bool
    s: bool
    o: bool
    rond: str
    c: int = len(la)
    j: int = 0
    i: int = 0
    k: int
    a: int
    b: Case
    bordure = 50
    larg1 = larg - 2 * bordure
    haut1 = haut - 2 * bordure
    xpion, ypion = pion
    for a in range(len(la)):
        d: int = len(la[a])
        i = 0
        for k in range(d):
            n, e, s, o, rond = la[a][k]
            if n == False:
                p1 = Point(bordure + j * larg1 / d, haut - (bordure + (i + 1) * haut1 / c))
                p2 = Point(bordure + (j + 1) * larg1 / d, haut - (bordure + (i + 1) * haut1 / c))
                line = Line(p1, p2)
                line.draw(win)
            if e == False:
                p1 = Point(bordure + (j + 1) * larg1 / d, haut - (bordure + (i + 1) * haut1 / c))
                p2 = Point(bordure + (j + 1) * larg1 / d, haut - (bordure + i * haut1 / c))
                line = Line(p1, p2)
                line.draw(win)
            if s == False:
                p1 = Point(bordure + j * larg1 / d, haut - (bordure + i * haut1 / c))
                p2 = Point(bordure + (j + 1) * larg1 / d, haut - (bordure + i * haut1 / c))
                line = Line(p1, p2)
                line.draw(win)
            if o == False:
                p1 = Point(bordure + j * larg1 / d, haut - (bordure + (i + 1) * haut1 / c))
                p2 = Point(bordure + j * larg1 / d, haut - (bordure + i * haut1 / c))
                line = Line(p1, p2)
                line.draw(win)
            if rond == "ENTREE":
                c1 = (bordure + j * larg1 / d + bordure + (j + 1) * larg1 / d) / 2
                c2 = (bordure + (i + 1) * haut1 / c + bordure + i * haut1 / c) / 2
                centre = Point(c1, haut - c2)
                rayon = min((larg1 / d) / 2, (haut1 / c) / 2)
                cercle = Circle(centre, rayon - 15)
                cercle.draw(win)
                cercle.setFill("white")
            elif rond == "SORTIE":
                c1 = (bordure + j * larg1 / d + bordure + (j + 1) * larg1 / d) / 2
                c2 = (bordure + (i + 1) * haut1 / c + bordure + i * haut1 / c) / 2
                centre = Point(c1, haut - c2)
                rayon = min((larg1 / d) / 2, (haut1 / c) / 2)
                cercle = Circle(centre, rayon - 15)
                cercle.draw(win)
                cercle.setFill("black")
            if k == ypion and a == xpion:
                c1 = (bordure + j * larg1 / d + bordure + (j + 1) * larg1 / d) / 2
                c2 = (bordure + (i + 1) * haut1 / c + bordure + i * haut1 / c) / 2
                centre = Point(c1, haut - c2)
                rayon = min((larg1 / d) / 2, (haut1 / c) / 2)
                cercle = Circle(centre, rayon - 15)
                cercle.draw(win)
                cercle.setFill("pink")

            i = i + 1
        j = j + 1
    jeu:str='1'
    while jeu!='0':
        jeu=str(input("jouez\n"))

        if jeu=='a' or jeu=='A':
            if deplace_possible(la, pion, 'O'):
                pion=deplace(pion,'O')
            else:
                print("Deplacement impossible")
        elif jeu=='s' or jeu=='S':
            if deplace_possible(la, pion, 'S'):
                pion=deplace(pion,'S')
            else:
                print("Deplacement impossible")

        elif jeu=='w' or jeu=='W':
            if deplace_possible(la, pion, 'N'):
                pion = deplace(pion, 'N')
            else:
                print("Deplacement impossible")
        elif jeu=='d' or jeu=='D':
            if deplace_possible(la, pion, 'E'):
                pion = deplace(pion, 'E')
            else:
                print("Deplacement impossible")
        win.close()
        #dessine_laby(la,500,1000,pion)
        larg=1000
        haut=500
        win = GraphWin("mon labii", larg, haut)
        n: bool
        e: bool
        s: bool
        o: bool
        rond: str
        c: int = len(la)
        j: int = 0
        i: int = 0
        k: int
        a: int
        b: Case
        bordure = 50
        larg1 = larg - 2 * bordure
        haut1 = haut - 2 * bordure
        xpion, ypion = pion
        for a in range(len(la)):
            d: int = len(la[a])
            i = 0
            for k in range(d):
                n, e, s, o, rond = la[a][k]
                if n == False:
                    p1 = Point(bordure + j * larg1 / d, haut - (bordure + (i + 1) * haut1 / c))
                    p2 = Point(bordure + (j + 1) * larg1 / d, haut - (bordure + (i + 1) * haut1 / c))
                    line = Line(p1, p2)
                    line.draw(win)
                if e == False:
                    p1 = Point(bordure + (j + 1) * larg1 / d, haut - (bordure + (i + 1) * haut1 / c))
                    p2 = Point(bordure + (j + 1) * larg1 / d, haut - (bordure + i * haut1 / c))
                    line = Line(p1, p2)
                    line.draw(win)
                if s == False:
                    p1 = Point(bordure + j * larg1 / d, haut - (bordure + i * haut1 / c))
                    p2 = Point(bordure + (j + 1) * larg1 / d, haut - (bordure + i * haut1 / c))
                    line = Line(p1, p2)
                    line.draw(win)
                if o == False:
                    p1 = Point(bordure + j * larg1 / d, haut - (bordure + (i + 1) * haut1 / c))
                    p2 = Point(bordure + j * larg1 / d, haut - (bordure + i * haut1 / c))
                    line = Line(p1, p2)
                    line.draw(win)
                if rond == "ENTREE":
                    c1 = (bordure + j * larg1 / d + bordure + (j + 1) * larg1 / d) / 2
                    c2 = (bordure + (i + 1) * haut1 / c + bordure + i * haut1 / c) / 2
                    centre = Point(c1, haut - c2)
                    rayon = min((larg1 / d) / 2, (haut1 / c) / 2)
                    cercle = Circle(centre, rayon - 15)
                    cercle.draw(win)
                    cercle.setFill("white")
                elif rond == "SORTIE":
                    c1 = (bordure + j * larg1 / d + bordure + (j + 1) * larg1 / d) / 2
                    c2 = (bordure + (i + 1) * haut1 / c + bordure + i * haut1 / c) / 2
                    centre = Point(c1, haut - c2)
                    rayon = min((larg1 / d) / 2, (haut1 / c) / 2)
                    cercle = Circle(centre, rayon - 15)
                    cercle.draw(win)
                    cercle.setFill("black")
                if k == ypion and a == xpion:
                    c1 = (bordure + j * larg1 / d + bordure + (j + 1) * larg1 / d) / 2
                    c2 = (bordure + (i + 1) * haut1 / c + bordure + i * haut1 / c) / 2
                    centre = Point(c1, haut - c2)
                    rayon = min((larg1 / d) / 2, (haut1 / c) / 2)
                    cercle = Circle(centre, rayon - 15)
                    cercle.draw(win)
                    cercle.setFill("pink")

                i = i + 1
            j = j + 1

        if pion==exit:
            print("WIN")
            break




main()

