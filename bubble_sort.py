import tkinter as tk




class BubbleSort(tk.Tk):

    def __init__(self):
        
        super().__init__()

        # Config
        self.geometry("800x500")
        canvas = tk.Canvas(self, bg="brown")
        canvas.pack(fill=tk.BOTH, expand=True)





if __name__ == "__main__":
    app = BubbleSort()
    app.mainloop()

