import tkinter as tk
import random
from square import Square
from square import swap_squares


class Main(tk.Tk):

    def __init__(self):

        super().__init__()

        # Config
        self.geometry("800x500")
        self.title("Algorithm Visualizer")
        canvas = tk.Canvas(self, bg="#2c2b3c")
        canvas.pack(fill=tk.BOTH, expand=True)

        # Generate the squares with random values
        x1 = 10  # Initiate x1 at position 20
        y1 = 220
        x2 = 70  # Initiate x2 at position 80
        y2 = 280
        squares = []
        for i in range(10):
            squares.append(Square(canvas, x1, y1, x2,
                           y2, random.randint(1, 99)))
            x1 += 80
            x2 += 80


        in_order = False  # assume it's not sorted yet
        while not in_order:
            in_order = True  # assume it's sorted until proven otherwise

            for i in range(len(squares) - 1):
                if squares[i].val > squares[i+1].val:
                    swap_squares(squares[i], squares[i+1])
                    # swap the two
                    tmp = squares[i].val
                    squares[i].val = squares[i+1].val
                    squares[i+1].val = tmp

                    in_order = False  # found a swap, so it's not sorted yet
        
        for i in squares:
            print(i.val)


if __name__ == "__main__":
    app = Main()
    app.mainloop()
