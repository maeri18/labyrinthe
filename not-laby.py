from typing import Tuple
from typing import List
from graphics import *
win=GraphWin()
Coord = Tuple[int, int] #coordonnees du pion
Dir = str # "N" ou "S" ou "E" ou "O"
Chemin = List[Dir]
Case=Tuple[bool,bool,bool,bool,str]
Laby=List[List[Case]]
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

#deplacement selon un itineraire
def deplace_chemin(c:Coord,ch:Chemin)->Coord:
    if ch==[]:
        return c
    else :
        return deplace_chemin(deplace(c,ch[0]),ch[1:])

def dessine_laby(la:Laby):
    """ dessine un labyrinthe laby"""
    la_im : win 
    n:bool
    e:bool
    s:bool
    o:bool
    rond:str
    c:int=len(la)
    j:int=0
    i:int=0
    a:List[Case]
    b:Case
    for a in la:
        d:int = len(a)
        j=0
        for b in a:
            n,e,s,o,rond= b
            if n == False:
                p1 = Point(-1+i*2/c, -1+(j+1)*2/d)
                p2 = Point(-1+(i+1)*2/c, -1+(j+1)*2/d)
                line=Line(p1,p2)
                line.draw(la_im)
            if e == False:
                p1 = Point(-1+(i+1)*2/c, -1+(j+1)*2/d)
                p2 = Point( -1+(i+1)*2/c, -1+j*2/d)
                line=Line(p1,p2)
                line.draw(la_im)
            if s == False:
                p1 = Point(-1+i*2/c, -1+j*2/d)
                p2 = Point(-1+(i+1)*2/c, -1+j*2/d)
                line=Line(p1,p2)
                line.draw(la_im)
            if o == False:
                p1 = Point(-1+(i)*2/c, -1+(j+1)*2/d)
                p2 = Point(-1+(i)*2/c, -1+j*2/d)
                line=Line(p1,p2)
                line.draw(la_im)
            if rond=="ENTREE":
                c1=((-1+i*2/c)+2/(4*c)+(-1+(i+1)*2/c)-2/(4*c))/2
                c2=((-1+(j+1)*2/d)-2/(4*d)+(-1+j*2/d)+2/(4*d))/2
                centre=Point(c1,c2)
                rayon=math.sqrt(((-1+i*2/c)+2/(4*c)-c1)**2,((-1+(j+1)*2/d)-2/(4*d)-c2)**2)
                cercle = Circle(centre,rayon)
                cercle.draw(la_im)
                cercle.setFill("white")
            if rond == "SORTIE":
                c1=((-1+i*2/c)+2/(4*c)+(-1+(i+1)*2/c)-2/(4*c))/2
                c2=((-1+(j+1)*2/d)-2/(4*d)+(-1+j*2/d)+2/(4*d))/2
                centre=Point(c1,c2)
                rayon=math.sqrt(((-1+i*2/c)+2/(4*c)-c1)**2,((-1+(j+1)*2/d)-2/(4*d)-c2)**2)
                cercle = Circle(centre,rayon)
                cercle.draw(la_im)
                cercle.setFill("white")
            j=j+1
        i=i+1


