import tkinter as tk
import time


CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserApp:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()

        self.eraser = None
        self.create_grid()

        # Bind Mouse movement to erase function
        self.canvas.bind("<Motion>", self.eraser_objects)
        self.canvas.bind("<Button-1>", self.create_eraser)

    def create_grid(self):
        """Creates a grid of blue squares"""
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                self.canvas.create_rectangle(
                    col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue"
                )

    def create_eraser(self, event):
        if self.eraser is None:
            self.eraser = self.canvas.create_rectangle(
                event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE, fill="white"
            )

    def eraser_objects(self, event):
        """Erases objects under the eraser by changing their color to yellow"""
        if self.eraser:
            self.canvas.coords(
                self.eraser,
                event.x,
                event.y,
                event.x + ERASER_SIZE,
                event.y + ERASER_SIZE,
            )

            overlapping = self.canvas.find_overlapping(
                event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE
            )

            for obj in overlapping:
                if obj != self.eraser:
                    self.canvas.itemconfig(obj, fill="pink")

if __name__ == '__main__':   
    root = tk.Tk()
    root.title("Eraser Canvas App")
    app = EraserApp(root)
    root.mainloop()