import tkinter as tk

class Tablero:
    def __init__(self, N, M, WIDTH, HEIGHT):
        self.N = N
        self.M = M
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

    def dibujar_tablero(self, coords_bloqueadas, coords_meta):
        # Dibujar las casillas del tablero
        for i in range(self.N):
            for j in range(self.M):
                x0 = i*self.WIDTH
                y0 = j*self.HEIGHT
                x1 = x0 + self.WIDTH
                y1 = y0 + self.HEIGHT
                if (i, j) in coords_bloqueadas:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill="red")
                elif (i,j) in coords_meta:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
                else:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill="white")
    def dibujar_caminos(self,index=0):
        if index <len(self.coords_camino):
            self.camino=self.coords_camino[index]
            x0=self.camino[0]*self.WIDTH
            y0 = self.camino[1]*self.HEIGHT
            x1 = x0 + self.WIDTH
            y1 = y0 + self.HEIGHT
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="green")
            self.root.after(50,self.dibujar_caminos,index+1)
    def dibujar(self, coords_bloqueadas, coords_camino, coords_meta):
        # Crear la ventana y el canvas
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=self.N*self.WIDTH, height=self.M*self.HEIGHT)
        self.canvas.pack()
        self.coords_camino=coords_camino
        # Dibujar el tablero con las coordenadas bloqueadas y el camino especificado
        self.dibujar_tablero(coords_bloqueadas, coords_meta)
        self.root.after(0,self.dibujar_caminos)
        # Iniciar el bucle
        self.root.mainloop()