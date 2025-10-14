import tkinter as tk


class Square():

    def __init__(self, canvas, x1, y1, x2, y2, val):

        # Create the square
        self.id = canvas.create_rectangle(x1, y1, x2, y2, 
                                fill="white", outline="black", width=2)

        
        
        # Calculate the center of the square
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2

        # Draw the value in the center
        canvas.create_text(center_x, center_y, text=str(val), font=("Arial", 14, "bold"), fill="black")

        # Store val
        self.val = val


    def swap_squares(square1, square2):
        

        
