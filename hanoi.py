from copy import *
import random
from turtle import *
from time import *
#Partie A : plateau de jeu de listes
def init(n):
    liste=[]
    while n>0:
        liste.append(n)
        n-=1
    plateau=[liste,[],[]]
    return plateau
def nbDisquqes(plateau,numtour):
    return len(plateau[numtour])
def disqueSup(plateau,numtour):
    x=plateau[numtour]
    maximum=0
    if plateau[numtour]==[]or not(0<numtour<2):
        return -1
    for i in x:
        if i>maximum:
            maximum=i
    return maximum
def posDisque(plateau,numdisque):
    for j in range(len(plateau)):
        if numdisque in plateau[j]:
            return j
def verifDepl(plateau,nt1,nt2):
    flag=True
    if plateau[nt1]==[] or (plateau[nt2]!=[] and disqueSup(plateau,nt1)>disqueSup(plateau,nt2)):
        flag=False
    return flag
def verifVictoire(plateau,n):
    if plateau[2]==[]:
        return True
    destination=[]
    for i in range(n,0,-1):
        destination.append(i)
    if plateau[0]==[] and plateau[1]==[] and plateau[2]==destination:
        return False
    return True
#partie B : graphisme avec Turtle
def dessinePlateau(n):
    speed(100000)
    setup(500,500)
    diametere=(40+((n-1)*30))+20 #longueur de plus grand disque + 20
    demi_diametere=diametere/2 #la longueuer de deux parties (debut et fin)
    up()
    goto(-300,-200)
    down()
    begin_fill()
    color("black","black")
    for i in range(2):
        forward((diametere*2)+(demi_diametere*2))
        right(90)
        forward(20)
        right(90)
    up()
    goto(-303+demi_diametere,-200)
    down()
    forward(6)
    left(90)
    forward((n+1)*20)
    left(90)
    forward(6)
    left(90)
    forward((n+1)*20)
    left(90)
    up()
    goto(-306+demi_diametere+diametere,-200)
    down()
    forward(6)
    left(90)
    forward((n+1)*20)
    left(90)
    forward(6)
    left(90)
    forward((n+1)*20)
    left(90)
    up()
    goto(-309+demi_diametere+(diametere*2),-200)
    down()
    forward(6)
    left(90)
    forward((n+1)*20)
    left(90)
    forward(6)
    left(90)
    forward((n+1)*20)
    left(90)
    end_fill()
def dessineDisque(nd,plateau,n):
    colors={1: '#205e7d', 2: '#051ef7', 3: '#1313e0', 4: '#8f4135', 5: '#9f1a50', 6: '#fdddb0', 7: '#db913b', 8: '#844240', 9: '#4dd040', 10: '#18ef4c', 11: '#6bfbb5', 12: '#9474e0',13:"#6F00FF",14:"#FF6700",15:"#733380",16:"#AD4379",17:"#FF33CC",18:"#6699CC",19:"#66FF66",20:"#BF4F51"}
    for i in range(len(plateau)):
        if nd in plateau[i]:
            indice_nd=plateau[i].index(nd)
            y=i
    diametere=(40+((n-1)*30))+20 #longueur de plus grand disque + 20
    diametere2=(40+((nd-1)*30))+20 #diametere de different disque dependant de leur indice
    demi_diametere=diametere/2 #la longueuer de deux parties (debut et fin)
    up()
    if y==0:
        goto(-300+demi_diametere,-200+(indice_nd*21))
    elif y==1:
        goto(-303+demi_diametere+diametere,-200+(indice_nd*21))
    else:
        goto(-306+demi_diametere+(diametere*2),-200+(indice_nd*21))
    down()
    for i in range(2):
        begin_fill()
        color(colors[nd],colors[nd])
        forward(diametere2/2)
        left(90)
        forward(20)
        left(90)
        forward(diametere2/2)
        end_fill()
def effaceDisque(nd, plateau, n):
    for i in range(len(plateau)):
        if nd in plateau[i]:
            indice_nd=plateau[i].index(nd)
            y=i
    diametere=(40+((n-1)*30))+20 #longueur de plus grand disque + 20
    diametere2=(40+((nd-1)*30))+20 #diametere de different disque dependant de leur indice
    demi_diametere=diametere/2 #la longueuer de deux parties (debut et fin)
    up()
    if y==0:
        goto(-300+demi_diametere,-200+(indice_nd*21))
    elif y==1:
        goto(-303+demi_diametere+diametere,-200+(indice_nd*21))
    else:
        goto(-306+demi_diametere+(diametere*2),-200+(indice_nd*21))
    down()
    for i in range(2):
        begin_fill()
        color("white","white")
        forward(diametere2/2)
        left(90)
        forward(20)
        left(90)
        forward(diametere2/2)
        end_fill()
    if indice_nd==0:
        begin_fill()
        color("black","black")
        up()
        goto(-300,-200)
        down()
        forward(diametere)
        end_fill()
    begin_fill()
    up()
    color("black","black")
    if y==0:
        goto(-303+demi_diametere,-200+(indice_nd*21))
    elif y==1:
        goto(-306+demi_diametere+diametere,-200+(indice_nd*21))
    else:
        goto(-309+demi_diametere+(diametere*2),-200+(indice_nd*21))
    down()
    for j in range(2):
        forward(6)
        left(90)
        forward(20)
        left(90)
    end_fill()
def dessineConfig(plateau, n):
    for i in range(1,n+1):
        dessineDisque(i,plateau,n)
def effaceTout(plateau,n):
    diametre=40+30*(n-1)
    up()
    goto(-300,-220)
    begin_fill()
    color("white")
    down()
    forward(3*diametre+80)
    left(90)
    forward(20*(n+2)+3)
    left(90)
    forward(3*diametre+80)
    left(90)
    forward(20*(n+2)+3)
    left(90)
    end_fill()
#partie C : interactions avec le joueur
def lireCoords(plateau):
    ntd=int(input("Tour de départ? "))
    while not(0<=ntd<=2) or plateau[ntd]==[] :
        if plateau[ntd]==[]:
            ntd=int(input("Invalide, tour vide.\nTour de départ? "))
        else:
            ntd=int(input("Invalide(pas entre 0 et 2).\nTour de départ? "))
    flag=True
    while flag:
        for i in range(len(plateau)):
            if i!=ntd:
                if plateau[i]==[]:
                    flag=False
                elif plateau[i]!=[] and plateau[i][-1]>plateau[ntd][-1]:
                    flag=False
        if flag:
            ntd=int(input("Invalide(choisissez une autre tour).\nTour de départ? "))
    nta=int(input("Tour d’arrivée? "))
    while (not(0<=nta<=2) or ntd==nta ) or (plateau[nta]!=[] and plateau[ntd][-1]>plateau[nta][-1]) :
        if nta==ntd:
            nta=int(input("Invalide,c'est le meme tour.\nTour d'arrivée? "))
        elif not(0<=nta<=2):
            nta=int(input("Invalide,(pas entre 0 et 2).\nTour d'arrivée? "))
        else:
            nta=int(input("Invalide, disque plus petit.\nTour d'arrivée? "))
    print("Je déplace le disque",plateau[ntd][-1],"de la tour",ntd,"à la tour",nta)
    return ntd,nta
def jouerUnCoup(plateau,n):
    x,y=lireCoords(plateau)
    plateau_new=deepcopy(plateau)
    plateau[y].append(plateau[x][-1])
    plateau[x].pop(-1)
    dessineDisque(plateau_new[x][-1],plateau,n)
    effaceDisque(plateau_new[x][-1],plateau_new,n)
    return plateau
def boucleJeu(plateau,n):
    nb_coups=1
    nb_coups_max=2**n
    plateau2=deepcopy(plateau)
    coups={0:plateau2}
    dessinePlateau(n)
    dessineConfig(plateau,n)
    print("Vous avez",nb_coups_max,"essais.")
    while verifVictoire(plateau,n) and nb_coups<nb_coups_max:
        print(coups)
        print("Coup numéro",nb_coups)
        jouerUnCoup(plateau,n)
        plateau3=deepcopy(plateau)
        coups[nb_coups]=plateau3
        nb_coups+=1
        if verifVictoire(plateau,n)==False:
            print("vous avez gagnez au bout de",nb_coups,"coups.\n")
            return True,nb_coups-1
        annuler_dernier_coup=input("Annuler dernier coup?(oui/non): ")
        if annuler_dernier_coup=="oui" :
            nb_coups-=1
            ntd,nta,maximum,avant_maximum=dernierCoup(coups)
            dessineDisque(coups[avant_maximum][ntd][-1],coups[avant_maximum],n)
            effaceDisque(coups[maximum][nta][-1],coups[maximum],n)
            plateau=deepcopy(coups[avant_maximum])
            annulerDernierCoup(coups)
    print("Vous avez perdu après",nb_coups_max,"coups.\n")
    return False,nb_coups-1
#Partie D: annulation de coups
def dernierCoup(coups):
    coups1=deepcopy(coups)
    maximum=0
    for i in coups:
        if i>maximum:
            maximum=i
    del coups1[maximum]
    avant_maximum=maximum-1
    ntd=0
    nta=0
    for i in range(3):
        if len(coups[avant_maximum][i])<len(coups[maximum][i]):
            nta=i
        elif len(coups[avant_maximum][i])>len(coups[maximum][i]):
            ntd=i
    return ntd,nta,maximum,avant_maximum
def annulerDernierCoup(coups):
    ntd,nta,maximum,avant_maximum=dernierCoup(coups)
    del coups[maximum]
    return coups

#Partie E: comparaison des scores et temps de jeu
def sauvScore(nom,nb_disques,nb_coups,dicJoueurs):
    if nom not in dicJoueurs:
        dicJoueurs[nom]={}
        dicJoueurs[nom][nb_disques]=[nb_coups]
    else:
        if nb_disques in dicJoueurs[nom]:
            dicJoueurs[nom][nb_disques].append(nb_coups)
        else:
            dicJoueurs[nom][nb_disques]=[nb_coups]
    return dicJoueurs
#def afficheScores(dicJoueurs):
#program principal
print("Bienvenue dans les Tours de Hanoi")
dicJoueurs={}
rejouer="oui"
while rejouer=="oui":
    nd=int(input("Combien de disques? "))
    plateau=init(nd)
    G_P,nb_coups=boucleJeu(plateau,nd)
    if G_P:
        print("Entrez le nom du joueur: ",end="")
        nom=input()
        print(sauvScore(nom,nd,nb_coups,dicJoueurs))
    rejouer=input("rejouer (oui/non)? ")
    effaceTout(plateau, nd)
print("Au revoir")
