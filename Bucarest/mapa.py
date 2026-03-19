import tkinter as tk

# Definir ciudades y caminos
class MapaRumania: 
    cities = {
    "Arad": (68, 160),
    "Zerind": (100, 93),
    "Oradea": (140, 30),
    "Timisoara": (70, 290),
    "Lugoj": (200, 340),
    "Mehadia": (210, 400),
    "Dobreta": (200, 470),
    "Craiova": (360, 490),
    "Rimnicu Vilcea": (320, 290),
    "Sibiu": (280, 215),
    "Fagaras": (455, 230),
    "Pitesti": (480, 365),
    "Bucarest": (625, 425),
    "Giurgiu": (575, 520),
    "Urziceni": (720, 390),
    "Hirsova": (860, 390),
    "Eforie": (910, 480),
    "Vaslui": (820, 240),
    "Iasi": (750, 140),
    "Neamt": (630, 90)
    }
    def __init__(self, path) :
        self.path = path
        self.root = tk.Tk()
        self.root.title('Mapa de rumania')
        self.canvas = tk.Canvas(self.root, width=960, height=540)
        self.canvas.pack()
        self.lineas_ciudades()
        self.ciudades()
        self.ruta_corta()
        self.root.mainloop()

    #Lineas entre ciudades
    def lineas_ciudades(self):
        self.canvas.create_line(68, 160, 100, 93, fill = "black", width=3)
        self.canvas.create_line(100, 93, 140, 30, fill = "black", width=3)
        self.canvas.create_line(140, 30, 280, 215, fill = "black", width=3)
        self.canvas.create_line(280, 215, 455, 230, fill = "black", width=3)
        self.canvas.create_line(455, 230, 625, 425, fill = "black", width=3)
        self.canvas.create_line(625, 425, 720, 390, fill = "black", width=3)
        self.canvas.create_line(720, 390, 820, 240, fill = "black", width=3)
        self.canvas.create_line(820, 240, 750, 140, fill = "black", width=3)
        self.canvas.create_line(750, 140, 630, 90, fill = "black", width=3)
        self.canvas.create_line(68, 160, 280, 215, fill = "black", width=3)
        self.canvas.create_line(280, 215, 320, 290, fill = "black", width=3)
        self.canvas.create_line(320, 290, 480, 365, fill = "black", width=3)
        self.canvas.create_line(480, 365, 625, 425, fill = "black", width=3)
        self.canvas.create_line(625, 425, 575, 520, fill = "black", width=3)
        self.canvas.create_line(720, 390, 860, 390, fill = "black", width=3)
        self.canvas.create_line(68, 160, 70, 290, fill = "black", width=3)
        self.canvas.create_line(70, 290, 200, 340, fill = "black", width=3)
        self.canvas.create_line(200, 340, 210, 400, fill = "black", width=3)
        self.canvas.create_line(210, 400, 200, 470, fill = "black", width=3)
        self.canvas.create_line(200, 470, 360, 490, fill = "black", width=3)
        self.canvas.create_line(360, 490, 320, 290, fill = "black", width=3)
        self.canvas.create_line(360, 490, 480, 365, fill = "black", width=3)
        self.canvas.create_line(910, 480, 860, 390, fill = "black", width=3)
    #Puntos de ciudades y nombres
    def ciudades(self):
        for city, coords in self.cities.items():
            x, y = coords
            self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="red") # Crear punto para representar ciudad
            self.canvas.create_text(x+10, y+10, text=city, font=("Arial", 12)) # Crear etiqueta con el nombre de la ciudad

    def ruta_corta(self):
        for i in range(len(self.path)-1):
            ciudad_inicio = self.path[i]
            sig_ciudad = self.path[i+1]
            coord_ini = self.cities[ciudad_inicio]
            coord_sig = self.cities[sig_ciudad]
            self.canvas.create_line(coord_ini, coord_sig, fill="blue", width=3) # Crear línea para representar camino


