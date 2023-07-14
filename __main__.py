from typing import Tuple
from typing import List
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()
larg = 1000
haut = 1000
Coord = Tuple[int, int] #coordonnees du pion
Dir = str # "N" ou "S" ou "E" ou "O"
Chemin = List[Dir]
Case=Tuple[bool,bool,bool,bool,str]
Laby=List[List[Case]]
laby1 : Laby = [[(True,True,False,False,""),(False,False,True,False,"ENTREE")],[(True,False,False,True,""),(False,False,True,False,"SORTIE")]]
laby3 : Laby = [[(True, True, False, False, ''), (False, False, True, False, ''), (False, True, False, False, ''), (True, False, False, False, ''), (True, True, True, False, ''), (True, False, True, False, ''), (True, True, True, False, ''), (True, False, True, False, ''), (True, False, True, False, ''), (True, False, True, False, ''), (False, False, True, False, ''), (True, True, False, False, ''), (True, False, True, False, ''), (False, True, True, False, ''), (False, True, False, False, ''), (True, False, False, False, ''), (False, True, True, False, ''), (False, True, False, False, ''), (False, True, False, False, ''), (False, True, False, False, "ENTREE")], [(True, False, False, True, ''), (False, True, True, False, ''), (True, True, False, True, ''), (True, False, True, False, ''), (True, False, True, True, ''), (False, False, True, False, ''), (False, False, False, True, ''), (True, False, False, False, ''), (True, True, True, False, ''), (True, True, True, False, ''), (True, False, True, False, ''), (True, True, True, True, ''), (False, False, True, False, ''), (False, True, False, True, ''), (False, True, False, True, ''), (True, False, False, False, ''), (True, False, True, True, ''), (False, True, True, True, ''), (False, True, False, True, ''), (False, True, False, True, '')], [(True, True, False, False, ''), (True, True, True, True, ''), (True, False, True, True, ''), (True, True, True, False, ''), (True, False, True, False, ''), (False, True, True, False, ''), (True, False, False, False, ''), (False, True, True, False, ''), (False, False, False, True, ''), (False, True, False, True, ''), (True, False, False, False, ''), (True, True, True, True, ''), (False, False, True, False, ''), (True, False, False, True, ''), (False, True, True, True, ''), (True, False, False, False, ''), (False, True, True, False, ''), (True, False, False, True, ''), (False, True, True, True, ''), (False, True, False, True, '')], [(False, True, False, True, ''), (True, False, False, True, ''), (False, False, True, False, ''), (True, False, False, True, ''), (False, True, True, False, ''), (False, False, False, True, ''), (False, True, False, False, ''), (True, True, False, True, ''), (False, False, True, False, ''), (True, True, False, True, ''), (False, True, True, False, ''), (False, True, False, True, ''), (False, True, False, False, ''), (True, False, False, False, ''), (False, True, True, True, ''), (True, True, False, False, ''), (True, True, True, True, ''), (True, False, True, False, ''), (False, True, True, True, ''), (False, True, False, True, '')], [(True, False, False, True, ''), (True, True, True, False, ''), (False, False, True, False, ''), (True, False, False, False, ''), (False, True, True, True, ''), (True, True, False, False, ''), (True, False, True, True, ''), (False, True, True, True, ''), (True, False, False, False, ''), (False, False, True, True, ''), (False, False, False, True, ''), (True, True, False, True, ''), (True, False, True, True, ''), (False, True, True, False, ''), (True, True, False, True, ''), (False, False, True, True, ''), (False, True, False, True, ''), (False, True, False, False, ''), (False, False, False, True, ''), (False, True, False, True, '')], [(True, False, False, False, ''), (True, True, True, True, ''), (False, False, True, False, ''), (True, False, False, False, ''), (True, False, True, True, ''), (True, True, True, True, ''), (False, True, True, False, ''), (False, False, False, True, ''), (True, True, False, False, ''), (False, False, True, False, ''), (False, True, False, False, ''), (False, False, False, True, ''), (True, False, False, False, ''), (False, False, True, True, ''), (False, True, False, True, ''), (False, True, False, False, ''), (True, False, False, True, ''), (True, True, True, True, ''), (False, False, True, False, ''), (False, True, False, True, '')], [(True, False, False, False, ''), (True, True, True, True, ''), (True, False, True, False, ''), (False, False, True, False, ''), (True, False, False, False, ''), (False, True, True, True, ''), (False, False, False, True, ''), (False, True, False, False, ''), (False, True, False, True, ''), (True, False, False, False, ''), (False, True, True, True, ''), (False, True, False, False, ''), (True, True, False, False, ''), (False, False, True, False, ''), (False, False, False, True, ''), (True, True, False, True, ''), (False, False, True, False, ''), (False, True, False, True, ''), (True, True, False, False, ''), (False, True, True, True, '')], [(True, True, False, False, ''), (True, False, True, True, ''), (False, False, True, False, ''), (True, True, False, False, ''), (True, False, True, False, ''), (False, True, True, True, ''), (False, True, False, False, ''), (False, True, False, True, ''), (False, True, False, True, ''), (True, True, False, False, ''), (True, False, True, True, ''), (False, False, True, True, ''), (False, True, False, True, ''), (True, False, False, False, ''), (False, True, True, False, ''), (True, False, False, True, ''), (True, True, True, False, ''), (True, False, True, True, ''), (False, True, True, True, ''), (False, False, False, True, '')], [(False, False, False, True, ''), (True, True, False, False, ''), (False, True, True, False, ''), (False, False, False, True, ''), (True, False, False, False, ''), (True, False, True, True, ''), (False, True, True, True, ''), (False, True, False, True, ''), (False, True, False, True, ''), (False, True, False, True, ''), (True, False, False, False, ''), (False, True, True, False, ''), (False, True, False, True, ''), (False, True, False, False, ''), (True, True, False, True, ''), (False, False, True, False, ''), (True, False, False, True, ''), (False, True, True, False, ''), (True, False, False, True, ''), (False, True, True, False, '')], [(False, True, False, False, ''), (False, True, False, True, ''), (True, False, False, True, ''), (False, True, True, False, ''), (True, False, False, False, ''), (True, True, True, False, ''), (True, False, True, True, ''), (True, False, True, True, ''), (True, False, True, True, ''), (False, False, True, True, ''), (True, False, False, False, ''), (True, False, True, True, ''), (False, True, True, True, ''), (True, False, False, True, ''), (False, True, True, True, ''), (False, True, False, False, ''), (True, False, False, False, ''), (False, True, True, True, ''), (True, True, False, False, ''), (False, False, True, True, '')], [(True, False, False, True, ''), (False, True, True, True, ''), (True, False, False, False, ''), (True, True, True, True, ''), (True, False, True, False, ''), (True, True, True, True, ''), (True, False, True, False, ''), (False, True, True, False, ''), (False, True, False, False, ''), (False, True, False, False, ''), (True, False, False, False, ''), (False, True, True, False, ''), (True, False, False, True, ''), (True, False, True, False, ''), (True, False, True, True, ''), (False, True, True, True, ''), (True, True, False, False, ''), (False, False, True, True, ''), (True, False, False, True, ''), (False, True, True, False, '')], [(True, False, False, False, ''), (True, False, True, True, ''), (False, False, True, False, ''), (True, False, False, True, ''), (False, True, True, False, ''), (False, True, False, True, ''), (True, False, False, False, ''), (True, False, True, True, ''), (True, False, True, True, ''), (True, False, True, True, ''), (True, False, True, False, ''), (False, False, True, True, ''), (True, True, False, False, ''), (False, True, True, False, ''), (True, True, False, False, ''), (True, True, True, True, ''), (False, True, True, True, ''), (True, False, False, False, ''), (False, True, True, False, ''), (False, False, False, True, '')], [(False, True, False, False, ''), (True, False, False, False, ''), (True, True, True, False, ''), (False, True, True, False, ''), (False, True, False, True, ''), (True, False, False, True, ''), (True, False, True, False, ''), (True, False, True, False, ''), (True, False, True, False, ''), (True, True, True, False, ''), (True, True, True, False, ''), (False, False, True, False, ''), (False, False, False, True, ''), (True, True, False, True, ''), (False, False, True, True, ''), (False, True, False, True, ''), (True, False, False, True, ''), (False, True, True, False, ''), (True, False, False, True, ''), (False, True, True, False, '')], [(False, True, False, True, ''), (True, False, False, False, ''), (False, False, True, True, ''), (False, True, False, True, ''), (True, False, False, True, ''), (True, True, True, False, ''), (False, True, True, False, ''), (True, True, False, False, ''), (True, True, True, False, ''), (False, True, True, True, ''), (True, False, False, True, ''), (False, True, True, False, ''), (True, False, False, False, ''), (True, True, True, True, ''), (False, True, True, False, ''), (True, False, False, True, ''), (False, False, True, False, ''), (True, False, False, True, ''), (False, False, True, False, ''), (False, True, False, True, '')], [(True, False, False, True, ''), (True, False, True, False, ''), (True, True, True, False, ''), (False, True, True, True, ''), (False, True, False, False, ''), (False, False, False, True, ''), (False, True, False, True, ''), (False, False, False, True, ''), (False, False, False, True, ''), (False, True, False, True, ''), (False, True, False, False, ''), (False, True, False, True, ''), (True, False, False, False, ''), (False, False, True, True, ''), (True, False, False, True, ''), (True, False, True, False, ''), (True, True, True, False, ''), (False, False, True, False, ''), (True, True, False, False, ''), (False, False, True, True, '')], [(True, True, False, False, ''), (True, False, True, False, ''), (False, False, True, True, ''), (False, False, False, True, ''), (False, True, False, True, ''), (True, False, False, False, ''), (True, True, True, True, ''), (False, False, True, False, ''), (False, True, False, False, ''), (False, False, False, True, ''), (True, False, False, True, ''), (True, True, True, True, ''), (True, False, True, False, ''), (True, True, True, False, ''), (False, False, True, False, ''), (False, True, False, False, ''), (True, True, False, True, ''), (False, True, True, False, ''), (False, True, False, True, ''), (False, True, False, False, '')], [(True, False, False, True, ''), (True, True, True, False, ''), (False, False, True, False, ''), (False, True, False, False, ''), (True, True, False, True, ''), (False, False, True, False, ''), (True, False, False, True, ''), (True, True, True, False, ''), (False, False, True, True, ''), (True, True, False, False, ''), (False, False, True, False, ''), (True, False, False, True, ''), (False, True, True, False, ''), (True, True, False, True, ''), (False, True, True, False, ''), (True, True, False, True, ''), (False, True, True, True, ''), (True, False, False, True, ''), (False, False, True, True, ''), (False, True, False, True, '')], [(False, True, False, False, ''), (True, False, False, True, ''), (True, True, True, False, ''), (False, False, True, True, ''), (False, True, False, True, ''), (True, True, False, False, ''), (True, True, True, False, ''), (True, True, True, True, ''), (True, False, True, False, ''), (False, False, True, True, ''), (False, True, False, False, ''), (False, True, False, False, ''), (False, False, False, True, ''), (False, False, False, True, ''), (True, True, False, True, ''), (False, True, True, True, ''), (True, False, False, True, ''), (True, True, True, False, ''), (True, True, True, False, ''), (False, False, True, True, '')], [(True, False, False, True, ''), (False, True, True, False, ''), (True, False, False, True, ''), (True, True, True, False, ''), (False, False, True, True, ''), (False, False, False, True, ''), (False, False, False, True, ''), (True, True, False, True, ''), (True, False, True, False, ''), (False, False, True, False, ''), (True, False, False, True, ''), (True, False, True, True, ''), (True, True, True, False, ''), (True, True, True, False, ''), (False, False, True, True, ''), (False, False, False, True, ''), (True, False, False, False, ''), (False, False, True, True, ''), (False, True, False, True, ''), (False, True, False, False, '')], [(True, False, False, False, 'SORTIE'), (True, False, True, True, ''), (True, False, True, False, ''), (True, False, True, True, ''), (True, False, True, False, ''), (True, False, True, False, ''), (True, False, True, False, ''), (True, False, True, True, ''), (True, False, True, False, ''), (True, False, True, False, ''), (False, False, True, False, ''), (True, False, False, False, ''), (False, False, True, True, ''), (True, False, False, True, ''), (False, False, True, False, ''), (True, False, False, False, ''), (True, False, True, False, ''), (True, False, True, False, ''), (True, False, True, True, ''), (False, False, True, True, '')]]
screen = pygame.display.set_mode((larg,haut))
screen.fill((255,255,255))
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

def dessine_laby(la:Laby,haut:int, larg:int,pion:Coord, latepion : Coord)->None:
    """Precondition : haut>10 and larg>10"""
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
    global screen
    p1 : Coord
    p2 : Coord
    bordure = 50
    centre : Coord
    larg1=larg-2*bordure
    haut1=haut-2*bordure
    xpion,ypion=pion
    latex, latey = latepion
    for a in range(len(la)):
        d:int = len(la[a])
        i=0
        for k in range(d):
            n,e,s,o,rond= la[a][k]
            if n == False:
                p1 = (bordure+j*larg1/d,haut-(bordure+(i+1)*haut1/c))
                p2 = (bordure+(j+1)*larg1/d,haut-(bordure+(i+1)*haut1/c))
                pygame.draw.line(screen, (0,0,0),p1,p2,1)
            if e == False:
                p1 = (bordure+(j+1)*larg1/d,haut-(bordure+(i+1)*haut1/c))
                p2 = (bordure+(j+1)*larg1/d,haut-(bordure+i*haut1/c))
                pygame.draw.line(screen, (0,0,0),p1,p2,1)
            if s == False:
                p1 = (bordure+j*larg1/d,haut-(bordure+i*haut1/c))
                p2 = (bordure+(j+1)*larg1/d,haut-(bordure+i*haut1/c))
                pygame.draw.line(screen, (0,0,0),p1,p2,1)
            if o == False:
                p1 = (bordure + j * larg1 / d, haut-(bordure + (i + 1) * haut1 / c))
                p2 = (bordure + j * larg1 / d, haut-(bordure + i * haut1 / c))
                pygame.draw.line(screen, (0,0,0),p1,p2,1)
            if k== latey and a == latex:
                c1 = (bordure + j * larg1 / d + bordure + (j + 1) * larg1 / d) / 2
                c2 = (bordure + (i + 1) * haut1 / c + bordure + i * haut1 / c) / 2
                centre =(c1, haut - c2)
                rayon = min((larg1 / d) / 2, (haut1 / c) / 2)
                pygame.draw.circle(screen,(200,255,200),centre,rayon - 15)
            if k==ypion and a==xpion:
                c1 = (bordure + j * larg1 / d + bordure + (j + 1) * larg1 / d) / 2
                c2 = (bordure + (i + 1) * haut1 / c + bordure + i * haut1 / c) / 2
                centre =(c1, haut - c2)
                rayon = min((larg1 / d) / 2, (haut1 / c) / 2)
                pygame.draw.circle(screen,(255, 182, 193),centre,rayon - 15)
            if rond=="ENTREE":
                c1 = (bordure+j*larg1/d + bordure+(j+1)*larg1/d)/2
                c2 = (bordure+(i+1)*haut1/c + bordure+i*haut1/c)/2
                centre = (c1, haut-c2)
                rayon = min((larg1/d)/2,(haut1/c)/2)
                pygame.draw.circle(screen,(255, 16, 240),centre,rayon - 15)
            if rond == "SORTIE":
                c1 = (bordure + j * larg1 / d + bordure + (j + 1) * larg1 / d) / 2
                c2 = (bordure + (i + 1) * haut1 / c + bordure + i * haut1 / c) / 2
                centre = (c1,  haut-c2)
                rayon = min((larg1 / d) / 2, (haut1 / c) / 2)
                pygame.draw.circle(screen,(255, 0, 0),centre,rayon - 15)
         
           
            pygame.draw.line(screen, (0,0,0),p1,p2,1)
            
            i=i+1
        j=j+1
    pygame.display.flip()

   


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
    late : Coord = pion
    global screen
    
    
    jeu:bool=True
    while jeu:
        #jeu=str(input("jouez\n"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jeu = False
                break
            elif event.type == KEYDOWN:
                late = pion
                if event.key == K_LEFT:
                    if deplace_possible(la, pion, 'O'):
                        pion=deplace(pion,'O')
                    else:
                        print("Deplacement impossible")
                elif event.key == K_DOWN:
                    if deplace_possible(la, pion, 'S'):
                        pion=deplace(pion,'S')
                    else:
                        print("Deplacement impossible")

                elif event.key == K_UP:
                    if deplace_possible(la, pion, 'N'):
                        pion = deplace(pion, 'N')
                    else:
                        print("Deplacement impossible")
                elif event.key == K_RIGHT:
                    if deplace_possible(la, pion, 'E'):
                        pion = deplace(pion, 'E')
                    else:
                        print("Deplacement impossible")
       
        dessine_laby(la,1000,1000,pion,late)
        

        if pion==exit:
            print("WIN")
            break
    
main()

