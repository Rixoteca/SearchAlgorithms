visitados = []
def CalcularAtaques(lista):
    length = len(lista)
    Ataques = 0
    for i in range(length-1):
        for j in range(i+1,length):
            if(lista[i]==lista[j]):
                Ataques+=2
            elif((abs(i-j)-abs(lista[i]-lista[j]))==0):
                Ataques+=2
    return Ataques

def GoalTest(lista):
    Numero_Ataques = CalcularAtaques(lista)
    if(Numero_Ataques==0):
        return True
    else:
        return False

def P_F(F,limite):
    if len(F)<0:
        print("No hay solucion")
        return
    edo_act = F[0][0]
    nvl_act = F[0][1]
    visitados.append(edo_act)
    print("Edo_act ",edo_act," Nivel ",nvl_act)
    F.pop(0)

    if(GoalTest(edo_act)):
        print("Goal test ",edo_act, "Nivel: ", nvl_act)
        return
    elif nvl_act<limite:
        offSpring = expandir(edo_act,nvl_act)
        F = offSpring + F
    P_F(F,limite)

    
def expandir(edo_act,nvl_act):
    offSpring = []
    n = len(edo_act)
    nvl_act = nvl_act+1
    for i in range(n):
        offAux = edo_act.copy()
        if (offAux[i]<n):
            offAux[i]=offAux[i]+1
            valorAux = [offAux,nvl_act]
            if offAux not in visitados:
                offSpring.append(valorAux)
    return offSpring

P_F([[[1, 1, 1,1],0]],6)


