import tkinter as tk

class ChessboardGUI:
    def __init__(self, size, queens):
        self.size = size
        self.queens = queens
        self.root = tk.Tk()
        self.root.title('Tablero de Ajedrez')
        self.root.geometry('1366x768')
        self.square_size = min(60, 600 // self.size)  # ajustar el tamaño de las casillas
        self.board_size = self.square_size * self.size
        self.canvas = tk.Canvas(self.root, width=self.board_size, height=self.board_size)
        self.canvas.pack()
        self.draw_board()
        self.draw_queens()
        self.root.mainloop()

    def draw_board(self):
        for row in range(self.size):
            for col in range(self.size):
                x1, y1 = col * self.square_size, row * self.square_size
                x2, y2 = x1 + self.square_size, y1 + self.square_size
                color = 'white' if (row + col) % 2 == 0 else 'gray'
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def draw_queens(self):
        for row, col in enumerate(self.queens):
            x = col * self.square_size + self.square_size // 2
            y = row * self.square_size + self.square_size // 2
            self.canvas.create_oval(x - self.square_size // 4, y - self.square_size // 4,
                                    x + self.square_size // 4, y + self.square_size // 4,
                                    fill='red')