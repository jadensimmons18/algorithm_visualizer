import tkinter as tk
from square import Square

class BubbleSort(tk.Tk):

    def __init__(self):

        super().__init__()

        # Config
        self.geometry("800x500")
        self.title("Algorithm Visualizer")
        canvas = tk.Canvas(self, bg="#2c2b3c")
        canvas.pack(fill=tk.BOTH, expand=True)
        
        # Generate the squares with random values
        x1 = 20 # Initiate x1 at position 20
        y1 = 220
        x2 = 80 # Initiate x2 at position 80
        y2 = 280
        squares = []
        for i in range(10):
            squares.append(Square(canvas,x1, y1, x2,y2))
            x1 += 80
            x2 += 80



if __name__ == "__main__":
    app = BubbleSort()
    app.mainloop()
