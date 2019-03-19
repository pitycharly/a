from TDA_grafos import* 
from TDA_PILA   import*


#ejercicio1
L = Grafo()

for n in range(1,6):
    ver = Vertice()
    ver.info = n
    insertar(L,ver)
    
arista = Arista()
arista.info = 2 #destino
pos = buscar(L,1)
insertar(pos,arista)

arista = Arista()
arista.info = 5 #destino
pos = buscar(L,1)
insertar(pos,arista)


arista = Arista()
arista.info = 4 #destino
pos = buscar(L,1)
insertar(pos,arista)

arista = Arista()
arista.info = 3 #destino
pos = buscar(L,2)
insertar(pos,arista)

arista = Arista()
arista.info = 5 #destino
pos = buscar(L,3)
insertar(pos,arista)

arista = Arista()
arista.info = 3 #destino
pos = buscar(L,4)
insertar(pos,arista)

arista = Arista()
arista.info = 5 #destino
pos = buscar(L,4)
insertar(pos,arista)

arista = Arista()
arista.info = 3
pos = buscar(L, 4)
insertar(pos, arista)






ori = L.cab
des = L.cab

pila = pila()

apila(pila,ori)
fin = False
lista = []
lista.append(ori.info)


while (not pilavacia(pila)) and (not fin):
    aux = desapilar(pila)    
    pos = buscar(aux,des.info)
    if (pos!=None):
        fin = True
    else:
        lar = aux.cab
        if(lar!=None):
            while(lar!=None and lar.info in lista):
                lar = lar.sig    
            if(lar!=None):
                apila(pila,aux)                
                aux = buscar(L,lar.info)
                apila(pila,aux)
                lista.append(lar.info)
                
                
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    