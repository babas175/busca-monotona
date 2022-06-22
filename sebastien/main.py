from ast import Break
import math
import sys 
import time
import random 
import pandas as pd
import numpy as np

START_TEMP = 10
ALPHA = .95


file_list = ['dj38.tsp']
file_list1 = ['qa194.tsp']
file_list2 = ['uy734.tsp']
file_list3= ['wi29.tsp']
file_list4= ['zi929.tsp']

alpha_values = []
alpha_values.append(0)

vetor=[]
vetor1=[]
vetor2=[]
vetor3=[]
vetor4=[]

tempo1=[]
tempo2=[]
tempo3=[]
tempo4=[]
tempo5=[]

class Cidade:
    # Solucao inicial 
    def __init__(self,id,x,y):
        self.id = id
        self.x =x
        self.y =y
        self.visitado=False
        
    #funcao para calcular a distancia euclidiana entre os pontos 
def calculaDistanciaEuclidiana(cidade1, cidade2):
    x_distance= abs(cidade1.x - cidade2.x)
    y_distance= abs(cidade1.y - cidade2.y)
    return int(round(math.sqrt(x_distance * x_distance + y_distance * y_distance)))

# funcao para gerar aleatoriamente a solucao inicial a partir dos pontos no arquivo
def importaArquivo(Arquivo):
    with open (Arquivo, "r") as meuArquivo:
        
        Cidades=[]
        for linha in meuArquivo:
            numArray =[]
            LinhaNumero=linha.split()
            for num in LinhaNumero:
                numArray.append(float(num))
            Cidades.append(Cidade(numArray[0], numArray[1], numArray[2]))
        random.shuffle(Cidades)
    return Cidades


    # funcao para computar a matriz de distancia entre os pontos
def calculateTotalDistance(route):
    
    tot = 0
    for idx in range(0, len(route)-1):
        tot += calculaDistanciaEuclidiana(route[idx], route[idx+1])
    tot += calculaDistanciaEuclidiana(route[len(route)-1], route[0])
    
    return tot


# buscar de vizinho mais proximo
def findVizinhoProximo(v, route):
    
    shortestEdgeLength = 99999999999
    closestNeighbor = None
    for c in route:
        if c.id != v.id:
            distance =calculaDistanciaEuclidiana(v, c)
            if shortestEdgeLength > distance:
                closestNeighbor = c
                shortestEdgeLength = distance
                
    return closestNeighbor      

def vizinhoProximo(route):
    new_route = []
    current_city = route.pop(0)
    new_route.append(current_city)
    while route != []:
        next = findVizinhoProximo(current_city, route)
        current_city = next
        route.remove(next)
        new_route.append(current_city)
        
    return new_route

#funcao para percorrer a vizinhança
def BLPM2opt(route, i, k):
    new_route = []
   
    for i in range(0, i):
        new_route.append(route[i])
    
   
    for i in range(k, i-1, -1):
        new_route.append(route[i])
    
 
    for i in range(k+1, len(route)):
        new_route.append(route[i])
    
    return new_route

#funcao para gerar solucao que vai chama as outras funcoes com as regras de vizinhança
def buscarSolucao(s, timeAvailable):       
    improvement = True
    start = time.time()
    end = start + timeAvailable
    while improvement: 
        improvement = False
        best_distance = calculateTotalDistance(s)
        i = 1
        while i < len(s):
            for k in range(i+1, len(s)):
                new_route = BLPM2opt(s, i, k)
                new_distance = calculateTotalDistance(new_route)
                if new_distance < best_distance:
                    s = new_route
                    best_distance = new_distance
                    improvement = True
                    i = 1
                if time.time() > end:
                    return s
            else:
                i += 1   

    return s  


vetor=[]


def printTour(s):
  
    print("Distance1: " + str(calculateTotalDistance(s)))

 
 
def Repetir_meu_código(vezes):
     for v in range(vezes):
        for file in file_list:
    
            for alpha in alpha_values:
                start = time.time()
                totalTime = 0.02
                tempo1.append(totalTime*100)
                s = importaArquivo(file)

                print("\nSoluçao Inicial")  
                printTour(s)

                greedy = vizinhoProximo(s)
                s = importaArquivo(file)

                print("\nDEPOIS DO PASSE DO VIZINHO MAIS PRÓXIMO")  
                printTour(greedy)

                if calculateTotalDistance(greedy) < calculateTotalDistance(s):
                    s = greedy
                else:
                    print("Greedy solution discarded.")
                    Break

                timeAvailable = totalTime - (time.time() - start)
                s = buscarSolucao(s, timeAvailable)
                
                print('melhor solucao' + str(vetor.append(calculateTotalDistance(s))))
        
                print("\ndepois do BLPM2opt ")  
                printTour(s)
                
                end = time.time()
                timeElapsed = end - start
                print("TIME: %f" % timeElapsed)
      
Repetir_meu_código(10) # Repetir 10 vezes

def Repetir_meu_código(vezes):
     for v in range(vezes):
        for file in file_list1:
    
            for alpha in alpha_values:
                start = time.time()
                totalTime = 0.11
                tempo2.append(totalTime*100)
                s = importaArquivo(file)

                print("\nSoluçao Inicial")  
                printTour(s)

                greedy = vizinhoProximo(s)
                s = importaArquivo(file)

                print("\nDEPOIS DO PASSE DO VIZINHO MAIS PRÓXIMO")  
                printTour(greedy)

                if calculateTotalDistance(greedy) < calculateTotalDistance(s):
                    s = greedy
                else:
                    print("Greedy solution discarded.")
                    Break

                timeAvailable = totalTime - (time.time() - start)
                s = buscarSolucao(s, timeAvailable)
                
                print('melhor solucao' + str(vetor1.append(calculateTotalDistance(s))))
        
                print("\ndepois do BLPM2opt ")  
                printTour(s)
                
                end = time.time()
                timeElapsed = end - start
                print("TIME: %f" % timeElapsed)
      
Repetir_meu_código(10) # Repetir 10 vezes

def Repetir_meu_código(vezes):
     for v in range(vezes):
        for file in file_list2:
    
            for alpha in alpha_values:
                start = time.time()
                totalTime = 0.02
                tempo3.append(totalTime*100)
                s = importaArquivo(file)

                print("\nSoluçao Inicial")  
                printTour(s)

                greedy = vizinhoProximo(s)
                s = importaArquivo(file)

                print("\nDEPOIS DO PASSE DO VIZINHO MAIS PRÓXIMO")  
                printTour(greedy)

                if calculateTotalDistance(greedy) < calculateTotalDistance(s):
                    s = greedy
                else:
                    print("Greedy solution discarded.")
                    Break

                timeAvailable = totalTime - (time.time() - start)
                s = buscarSolucao(s, timeAvailable)
                
                print('melhor solucao' + str(vetor2.append(calculateTotalDistance(s))))
        
                print("\ndepois do BLPM2opt ")  
                printTour(s)
                
                end = time.time()
                timeElapsed = end - start
                print("TIME: %f" % timeElapsed)
      
Repetir_meu_código(10) # Repetir 10 vezes

def Repetir_meu_código(vezes):
     for v in range(vezes):
        for file in file_list3:
    
            for alpha in alpha_values:
                start = time.time()
                totalTime = 0.44
                tempo4.append(totalTime*100)
                s = importaArquivo(file)

                print("\nSoluçao Inicial")  
                printTour(s)

                greedy = vizinhoProximo(s)
                s = importaArquivo(file)

                print("\nDEPOIS DO PASSE DO VIZINHO MAIS PRÓXIMO")  
                printTour(greedy)

                if calculateTotalDistance(greedy) < calculateTotalDistance(s):
                    s = greedy
                else:
                    print("Greedy solution discarded.")
                    Break

                timeAvailable = totalTime - (time.time() - start)
                s = buscarSolucao(s, timeAvailable)
                
                print('melhor solucao' + str(vetor3.append(calculateTotalDistance(s))))
        
                print("\ndepois do BLPM2opt ")  
                printTour(s)
                
                end = time.time()
                timeElapsed = end - start
                print("TIME: %f" % timeElapsed)
      
Repetir_meu_código(10) # Repetir 10 vezes

def Repetir_meu_código(vezes):
     for v in range(vezes):
        for file in file_list4:
    
            for alpha in alpha_values:
                start = time.time()
                totalTime = 0.56
                tempo5.append(totalTime*100)
                s = importaArquivo(file)

                print("\nSoluçao Inicial")  
                printTour(s)

                greedy = vizinhoProximo(s)
                s = importaArquivo(file)

                print("\nDEPOIS DO PASSE DO VIZINHO MAIS PRÓXIMO")  
                printTour(greedy)

                if calculateTotalDistance(greedy) < calculateTotalDistance(s):
                    s = greedy
                else:
                    print("Greedy solution discarded.")
                    Break

                timeAvailable = totalTime - (time.time() - start)
                s = buscarSolucao(s, timeAvailable)
                
                print('melhor solucao' + str(vetor4.append(calculateTotalDistance(s))))
        
                print("\ndepois do BLPM2opt ")  
                printTour(s)
                
                end = time.time()
                timeElapsed = end - start
                print("TIME: %f" % timeElapsed)
      
Repetir_meu_código(10) # Repetir 10 vezes




instancia=['Djibouti','Qatar','Uruguay','Western Sahara', 'Zimbabwe']
autoria=['Sebastien','Sebastien','Sebastien','Sebastien','Sebastien']
algoritmo=['BLPM2opt','BLPM2opt','BLPM2opt','BLPM2opt','BLPM2opt']
q_medio=[]
q_desvio=[]
t_medio=[]

print("djibouti=",vetor)
print(q_medio.append(round(np.average(vetor))))
print(q_desvio.append(round(np.std(vetor))))
print(t_medio.append(round(np.average(tempo1))))

print("qatar=",vetor1)
print(q_medio.append(round(np.average(vetor1))))
print(q_desvio.append(round(np.std(vetor1))))
print(t_medio.append(round(np.average(tempo2))))

print("Western Sahara=",vetor2)
print(q_medio.append(round(np.average(vetor2))))
print(q_desvio.append(round(np.std(vetor2))))
print(t_medio.append(round(np.average(tempo3))))

print("Uruguay=",vetor3)
print(q_medio.append(round(np.average(vetor3))))
print(q_desvio.append(round(np.std(vetor3))))
print(t_medio.append(round(np.average(tempo4))))

print("zimbabwe=",vetor4)
print(q_medio.append(round(np.average(vetor4))))
print(q_desvio.append(round(np.std(vetor4))))
print(t_medio.append(round(np.average(tempo5))))

ds=pd.DataFrame(zip(instancia,autoria,algoritmo,q_medio,q_desvio,t_medio),columns=['instancia','autoria','algoritmo','q_medio','q_desvio','t_medio'])
print(ds)


ds.to_csv('resultados.csv', encoding='utf-8', index=False)
