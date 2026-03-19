import time
import tkinter as tk
from threading import Thread

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
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill = "red")
                elif (i,j) in coords_meta:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill = "blue")
                else:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill = "white")

    def dibujar_camino(self, coords_camino, color):
        for i in range(len(coords_camino)):
            x0 = coords_camino[i][0] * self.WIDTH
            y0 = coords_camino[i][1] * self.HEIGHT
            x1 = x0 + self.WIDTH
            y1 = y0 + self.HEIGHT
            time.sleep(0.1)
            self.canvas.create_rectangle(x0, y0, x1, y1, fill = color)
            self.root.update()

    def dibujar(self, coords_bloqueadas, coords_camino1, coords_camino2,coords_camino3, coords_camino4, coords_meta):
        # Crear la ventana y el canvas
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=self.N * self.WIDTH, height=self.M * self.HEIGHT)
        self.canvas.pack()

        # Dibujar el tablero con las coordenadas bloqueadas
        self.dibujar_tablero(coords_bloqueadas, coords_meta)

        # Dibujar el primer camino en un hilo
        t1 = Thread(target = self.dibujar_camino, args = (coords_camino1, "green"))
        t1.start()

        # Dibujar el segundo camino en otro hilo
        t2 = Thread(target = self.dibujar_camino, args = (coords_camino2, "yellow"))
        t2.start()

        t3 = Thread(target = self.dibujar_camino, args = (coords_camino3, "gray"))
        t3.start()

        t4 = Thread(target = self.dibujar_camino, args = (coords_camino4, "magenta"))
        t4.start()

        # Iniciar el bucle
        self.root.mainloop()