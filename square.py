import tkinter as tk


class Square():

    def __init__(self, canvas, x1, y1, x2, y2, val):

        # Create the square
        self.id = canvas.create_rectangle(x1, y1, x2, y2, 
                                fill="white", outline="black", width=2)

        
        
        # Calculate the center of the square
        self.center_x = (x1 + x2) / 2
        self.center_y = (y1 + y2) / 2

        # Draw the value in the center
        canvas.create_text(self.center_x, self.center_y, text=str(val), font=("Arial", 14, "bold"), fill="black")

        # Store val
        self.val = val
        self.x1, self.x2 = x1,x2

    def swap_squares(square1, square2):
        speed = 10
        square1_final_dx = (square2.center_x - square1.center_x)
        square2_final_dx = (square1.center_x - square2.center_x)

        

        square1.canvas.move(square1.id, speed, 0)
        square2.canvas.move(square2.id, speed, 0)

        swap_squares(square1, square2)
        

        
