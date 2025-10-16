import tkinter as tk
import random

# Practice with animating a square


class TestSquare():

    def __init__(self, canvas, x1, y1, x2, y2, tag):

        # Create the square
        self.id = canvas.create_rectangle(
            x1, y1, x2, y2, fill="lightblue", outline="black", width=2, tags=(tag,))

        # Assign the tag
        self.tag = tag

        # Assign canvas
        self.canvas = canvas

        # Calculate the center of the square
        self.center_x = (x1 + x2) / 2
        self.center_y = (y1 + y2) / 2

        # Create the value
        self.val = random.randint(1, 99)

        # Draw the value in the center
        canvas.create_text(self.center_x, self.center_y, text=str(
            self.val), font=("Arial", 14, "bold"), fill="black", tags=(tag,))


    def animate(self,dx):
        self.canvas.move(self.tag, 10, 0)
        self.canvas.after(60, self.animate,dx)


def main():

    # Config
    root = tk.Tk()
    canvas = tk.Canvas(root, width=800, height=500, bg="white")
    canvas.pack()

    # Create squares
    square1 = TestSquare(canvas, 375, 225, 425, 275, "square1")
    square2 = TestSquare(canvas,445,225,495,275, "square2")

    # Calculate dx (Total Distance)
    dx =  square2.center_x - square1.center_x

    # Animate
    square1.animate(dx)
    square2.animate(-dx)

    # Main Loop
    root.mainloop()


if __name__ == "__main__":
    main()
