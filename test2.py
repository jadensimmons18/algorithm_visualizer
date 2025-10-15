import tkinter as tk
import time

class Box:
    def __init__(self, canvas, x, y, size, value, tag):
        self.canvas = canvas
        self.value = value
        self.tag = tag

        self.rect = canvas.create_rectangle(
            x, y, x + size, y + size, fill="lightblue", tags=tag
        )
        self.text = canvas.create_text(
            x + size / 2, y + size / 2, text=str(value), font=("Arial", 16), tags=tag
        )

    def move(self, dx, dy):
        self.canvas.move(self.tag, dx, dy)

    def get_position(self):
        return self.canvas.coords(self.rect)

def animate_swap(canvas, box1, box2, duration=1.0, fps=60):
    x1_start, _, x1_end, _ = box1.get_position()
    x2_start, _, x2_end, _ = box2.get_position()

    distance = x2_start - x1_start
    frames = int(duration * fps)
    dx = distance / frames

    for i in range(frames):
        box1.move(dx, 0)
        box2.move(-dx, 0)
        canvas.update()
        time.sleep(1 / fps)

def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=400, height=200, bg="white")
    canvas.pack()

    # Create two boxes
    box1 = Box(canvas, 50, 80, 60, 3, "box1")
    box2 = Box(canvas, 200, 80, 60, 7, "box2")

    # Button to trigger swap animation
    tk.Button(root, text="Swap Boxes", command=lambda: animate_swap(canvas, box1, box2)).pack()

    root.mainloop()

if __name__ == "__main__":
    main()
