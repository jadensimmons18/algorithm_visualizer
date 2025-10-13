import tkinter as tk


class Square():

    def __init__(self, canvas, x1, y1, x2, y2, val):
        canvas.create_rectangle(x1, y1, x2, y2,
                                fill="white", outline="black", width=2)
        
        # Calculate the center of the square
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2

        # Draw the value in the center
        canvas.create_text(center_x, center_y, text=str(val), font=("Arial", 14), fill="black")

        # Store val and position
        self.val = val
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

        
