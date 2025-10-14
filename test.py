import tkinter as tk
import time


class Animator:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=700, height=300, bg="white")
        self.canvas.pack(fill="both", expand=True)

        # create a rectangle and a text label grouped by tag "box"
        self.box = self.canvas.create_rectangle(
            10, 120, 60, 170, fill="skyblue", tags=("box",))
        self.label = self.canvas.create_text(
            35, 145, text="Move", tags=("box",))
        self.target = self.canvas.create_oval(
            600, 120, 640, 160, outline="red")

        # animation state
        self.running = False
        self.after_id = None # Stores the is that after() returns

        # Creates variable that will automatically link to widgets like slider
        self.speed = tk.DoubleVar(value=200.0)

        controls = tk.Frame(root)  # The frame for the buttons
        controls.pack(fill="x", pady=6)
        tk.Button(controls, text="Start", command=self.start).pack(
            side="left", padx=4)  # Start button
        self.pause_button = tk.Button(
            controls, text="Pause", command=self.toggle_pause, state="disabled")  # Pause button
        self.pause_button.pack(side="left", padx=4)
        tk.Button(controls, text="Reset", command=self.reset).pack(
            side="left", padx=4)  # Reset button
        tk.Label(controls, text="Speed (px/s):").pack(side="left", padx=(12, 4))
        tk.Scale(controls, from_=20, to=1000, orient="horizontal", variable=self.speed,
                 length=200).pack(side="left")  # Creates the actual slider

        # movement target (absolute x coordinate)
        self.target_x = 620
        # initial position
        self.reset()

    def reset(self):
        # place box back at start and stop animation
        self.canvas.coords(self.box, 10, 120, 60, 170) # places the box at (x1,y1) = (10,120) and (x2,y2) = (60,170)
        self.canvas.coords(self.label, 35, 145) # Places the label inside of the box at (x1,y1) = (35,145)
        self.running = False 
        if self.after_id: 
            self.root.after_cancel(self.after_id) # cancel the delay 
            self.after_id = None # Reset the after() id to none
        self.pause_button.config(text="Pause", state="disabled") # Disables the pause/resume button once reset

    def start(self):
        if self.running: # If its already running then do nothing when the start button is pressed
            return
        self.running = True
        self.pause_button.config(state="normal") # Enables the pause/resume button
        # time tracking for time-based movement
        self.last_time = time.time() # Creates a variable to keep track of the time
        self._animate() # Calls the animate function

    def toggle_pause(self):
        if self.running:
            # pause: cancel scheduled callback but keep position
            self.running = False
            if self.after_id:
                self.root.after_cancel(self.after_id)
                self.after_id = None
            self.pause_button.config(text="Resume")
        else:
            # resume
            self.running = True
            self.last_time = time.time()
            self._animate()
            self.pause_button.config(text="Pause")

    def _get_box_center(self):
        x0, y0, x1, y1 = self.canvas.coords(self.box)
        return ((x0 + x1)/2, (y0 + y1)/2)

    def _animate(self):
        """Internal animation step — moves toward target using time-based speed."""
        now = time.time()
        dt = now - self.last_time
        self.last_time = now

        speed = self.speed.get()  # pixels per second
        dx = speed * dt           # how many pixels to move this frame

        cx, cy = self._get_box_center()
        # move right until the center reaches target_x
        if cx + dx >= self.target_x:
            # snap to target and stop
            # compute exact final dx
            final_dx = self.target_x - cx
            self.canvas.move("box", final_dx, 0)
            self.running = False
            self.pause_button.config(state="disabled")
            self.after_id = None
            return
        else:
            self.canvas.move("box", dx, 0)

        # schedule next frame ~16 ms (about 60 FPS). using 16-33 ms is typical.
        self.after_id = self.root.after(16, self._animate)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Canvas Animation Example")
    Animator(root)
    root.mainloop()
