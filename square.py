import tkinter as tk


class Square():

    def __init__(self, canvas, x1, y1, x2, y2):
        canvas.create_rectangle(x1, y1, x2, y2,
                                fill="white", outline="black", width=2)

        
