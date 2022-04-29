import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(master=window, height=1920, width=600)
canvas.grid(row=0, column=0, sticky="nsew")

figures = {
    "square": {
        "map": [
            [
                {"value": 1, "position": {"x": 4, "y": 0}},
                {"value": 1, "position": {"x": 5, "y": 0}},
            ],
            [
                {"value": 1, "position": {"x": 4, "y": 1}},
                {"value": 1, "position": {"x": 5, "y": 1}},
            ],
        ]
    }
}
game_grid = [
    [
        canvas.create_rectangle(200 + 20 * i, j * 20, 200 + 20 * i + 20, j * 20 + 20)
        for j in range(20)
    ]
    for i in range(10)
]
square_map = figures["square"]["map"]
for i in square_map:
    for j in i:        
        canvas.itemconfig(
            game_grid[j["position"]["x"]][j["position"]["y"]], fill="black"
        )
window.mainloop()
