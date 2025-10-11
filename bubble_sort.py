import tkinter as tk




class BubbleSort(tk.Tk):

    def __init__(self):
        
        super().__init__()

        # Config
        self.geometry("800x500")
        self.title("Algorithm Visualizer")
        canvas = tk.Canvas(self, bg="#2c2b3c")
        canvas.pack(fill=tk.BOTH, expand=True)

        canvas.create_rectangle(100, 212.5, 175, 287.5, fill="white", outline="black", width=2)





if __name__ == "__main__":
    app = BubbleSort()
    app.mainloop()

