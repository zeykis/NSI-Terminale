class ABR:
    def __init__(self,racine=None):
        self.racine=racine
class Noeud:
    def __init__(self,valeur,noeud_gauche=None,noeud_droit=None,noeud_pere=None):
        self.valeur=valeur
        self.gauche=noeud_gauche
        self.droit=noeud_droit
        self.pere=noeud_pere
def infixe(n):
    if n is not None:
        infixe(n.gauche)
        print(n.valeur,)
        infixe(n.droit)
    
def prefixe(n):
    if n is not None:
        print(n.valeur)
        prefixe(n.gauche)
        prefixe(n.droit)
def suffixe(n):
    if n is not None:
        suffixe(n.gauche)
        suffixe(n.droit) 
        print(n.valeur)
def maximum(n):
    while n.droit!=None:
        n=n.droit
    return n.valeur
def minimum(n):
    while n.gauche!=None:
        n=n.gauche
    return n.valeur

def maximum_recur(n):
    if n.droit == None:
        return n.valeur
    return maximum_recur(n.droit)

def minimum_recur(n):
    if n.gauche == None:
        return minimum_recur(n.gauche)
    
def successeur(n):
    if n.droit !=None:
        return(minimum(n.droit))
    else:
        y=n.pere
        while n!=None and n==y.droit:
            n=y
            y=n.pere
    return y.valeur

n7=Noeud(9)
n6=Noeud(5)
n4=Noeud(8,n6,n7)
n3=Noeud(30)
n2=Noeud(31,n3,None)
n1=Noeud(20,None,n2)
n5=Noeud(10,n4,n1)
arbre_0=ABR(n5)

n7.pere=n4
n6.pere=n4
n4.pere=n5
n3.pere=n2
n2.pere=n1
n1.pere=n5
## Parcours d'arbre
#infixe(n5)
#prefixe(n5)
#suffixe(n5)
#####################################################

def est_feuille(node):
    if node['g']=={} and node['d']=={}:
        return True
    else:
        return False
    
    
def bsearch(node,val):
    if node['root']==val:
        return True
    if node=={}:
        return False
    if val<node['root']:
        return bsearch(node['g'],val)
    else:
        return bsearch(node['d'],val)
    
    
def search(node,val):
    if node['root']==val:
        return True
    if node=={}:
        return False
    if node['root']>val:
        return bsearch(node['g'],val)
    else:
        return bsearch(node['d'],val)
    
    
def taille(node):
    if node=={}:
        return 0
    else:
        return 1 + taille(node['g'])+ taille(node['d'])

      
def hauteur(node):
    if node =={}:
        return -1
    if est_feuille(node):
        return 0
    else:
        h1=hauteur(node['g'])
        h2=hauteur(node['d'])
        return max(h1,h2)+1
    
    
def somme_valeurs(node):
    if node=={}:
        return 0
    return node['root']+somme_valeurs(node['g'])+somme_valeurs(node['d'])

  
def innernnode(node):
    cpt=0
    if est_feuille(node)==True:
        return 0
    else:
        cpt+=1
        cpt1=innernnode(node['g'])
        cpt2=innernnode(node['d'])
    return cpt+cpt1+cpt2+1
                    

node1={'root' : 5, 'g' : {}, 'd' : {} }
node2={'root' : 11, 'g' : {}, 'd' : {} }
node5={'root' : 15, 'g' : {}, 'd' : {} }
node3={'root' : 10, 'g' : node1, 'd' : node2 }
node4={'root' : 14, 'g' : node3, 'd' : node5 }
print (hauteur(node4))
print(search(node4,14))
print (taille(node4))
print (innernnode(node4))
#print(est_feuille(node1))
#print(est_feuille(node2))
#print(est_feuille(node3))
#print(est_feuille(node4))
#print(est_feuille(node5))    
def insert(B,z):
    y=None
    x=B.racine
    while x!=None:
        y=x
        if z.valeur < x.valeur:
            x=x.gauche
        else:
            x=x.droit
    z.pere=y
    if y==None:
        B.racine=z
    elif z.valeur < y.valeur:
        y.gauche=z
    else:
        y.droit=z
    return B

def creer_abr(A):
    n=Noeud(L[0])
    arbre=ABR(n)
    for i in range(1,len(A)):
        noeud=Noeud(L[i])
        insert(arbre,noeud)
    return arbre
           
L=[17,10,5,21,3,56]
print(creer_abr(L))
