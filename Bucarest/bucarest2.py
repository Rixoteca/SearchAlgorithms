from mapa import MapaRumania
class Ciudad:
    def __init__(self, nombre, distanciab):
        self.nombre = nombre
        self.distanciab = distanciab
        self.vecinos = []
        self.frm = None 
        self.path = []

bucarest = Ciudad("Bucarest", 0)
giurgiu = Ciudad("Giurgiu", 77)
urziceni = Ciudad("Urziceni", 80)
vaslui = Ciudad("Vaslui", 199)
hirsova = Ciudad("Hirsova", 151)
eforie = Ciudad("Eforie", 161)
pitesti = Ciudad("Pitesti", 100)
rimnicu_vilcea = Ciudad("Rimnicu Vilcea", 193)
craiova = Ciudad("Craiova", 160)
fagaras = Ciudad("Fagaras", 211)
sibiu = Ciudad("Sibiu", 253)
arad = Ciudad("Arad", 366)
timisoara = Ciudad("Timisoara", 329)
lugoj = Ciudad("Lugoj", 244)
mehadia = Ciudad("Mehadia", 241)
dobreta = Ciudad("Dobreta", 242)
oradea = Ciudad("Oradea", 380)
iasi = Ciudad("Iasi", 226)
neamt = Ciudad("Neamt", 234)
zerind = Ciudad("Zerind", 374)

#[ciudad,distancia para llegar del vecino que viene, f(x),g(x),camino que se lleva para llegar]
bucarest.vecinos = [[pitesti, 101, 0, 0, []], [giurgiu, 90, 0, 0, []], [urziceni, 85, 0, 0, []], [fagaras, 211, 0, 0, []]]
pitesti.vecinos = [[bucarest, 101, 0, 0, []], [rimnicu_vilcea, 97, 0, 0, []], [craiova, 138, 0, 0, []]]
rimnicu_vilcea.vecinos = [[pitesti, 97, 0, 0, []], [sibiu, 80, 0, 0, []], [craiova, 146, 0, 0, []]]
craiova.vecinos = [[pitesti, 138, 0, 0, []], [rimnicu_vilcea, 146, 0, 0, []], [dobreta, 120, 0, 0, []]]
fagaras.vecinos = [[bucarest, 211, 0, 0, []], [sibiu, 99, 0, 0, []]]
sibiu.vecinos = [[rimnicu_vilcea, 80, 0, 0, []], [fagaras, 99, 0, 0, []], [arad, 140, 0, 0, []], [oradea, 151, 0, 0, []]]
arad.vecinos = [[sibiu, 140, 0, 0, []], [timisoara, 118, 0, 0, []], [zerind, 75, 0, 0, []]]
timisoara.vecinos = [[arad, 118, 0, 0, []], [lugoj, 111, 0, 0, []]]
lugoj.vecinos = [[timisoara, 111, 0, 0, []], [mehadia, 70, 0, 0, []]]
mehadia.vecinos = [[lugoj, 70, 0, 0, []], [dobreta, 75, 0, 0, []]]
dobreta.vecinos = [[craiova, 120, 0, 0, []], [mehadia, 75, 0, 0, []]]
giurgiu.vecinos = [[bucarest, 90, 0, 0, []]]
urziceni.vecinos = [[bucarest, 85, 0, 0, []], [hirsova, 98, 0, 0, []], [vaslui, 142, 0, 0, []]]
hirsova.vecinos = [[urziceni, 98, 0, 0, []], [eforie, 86, 0, 0, []]]
eforie.vecinos = [[hirsova, 86, 0, 0, []]]
vaslui.vecinos = [[urziceni, 142, 0, 0, []], [iasi, 92, 0, 0, []]]
iasi.vecinos = [[vaslui, 92, 0, 0, []], [neamt, 87, 0, 0, []]]
neamt.vecinos = [[iasi, 87, 0, 0, []]]
oradea.vecinos = [[sibiu, 151, 0, 0, []], [zerind, 71, 0, 0, []]]
zerind.vecinos= [[oradea, 71, 0, 0, []], [arad,75,0, 0, []]]

visitados = []
def a_estrella(F):
    if not F:
        print("No hay mas que explorar")
    else:
        E_A=F.pop(0)
        print(E_A)
        print(F)
        visitados.append(E_A[0])
        if GoalTest(E_A[0]):
            E_A[4].append(E_A[0].nombre)
            print("Distancia recorrida: ", E_A[3])
            print("Ruta: ",E_A[4])
            mapa= MapaRumania(E_A[4])
            print("Se llegó a la meta")
            return
        else:
            OS=Expand(E_A)
            OS=Evaluate(OS)
            F=F+OS
            F.sort(key=lambda x: x[2])
            a_estrella(F)

def GoalTest(ciudad):
    return ciudad==bucarest
    
def Expand(ciudad):
    vecinos = ciudad[0].vecinos
    aux=[]
    for c in range(len(ciudad[0].vecinos)):
        if vecinos[c][0] not in visitados:
            vecinos[c][3]=ciudad[3]+vecinos[c][1]
            vecinos[c][4]+=ciudad[4]
            vecinos[c][4].append(ciudad[0].nombre)
            aux.append(vecinos[c])
    return aux

def Evaluate(ciudades):
    for i in range(len(ciudades)):
        ciudades[i][2]=ciudades[i][0].distanciab+ciudades[i][1]+ciudades[i][3]
    return ciudades



visitados =[]
F=[[lugoj,0,0,0,[]]]
a_estrella(F)