from tkinter import *
import random

GAME_WIDTH = 900
GAME_HEIGHT = 500
SPEED = 60
SPACE_SIZE = 20
BODY_PARTS = 3
SNAKE_COLOR = "#ADFF2F"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#1C1C1C"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []  
        self.squares = []  

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags="food")

def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score:{}". format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print('game over')
            return True

    return False

def restart_game():
    global snake
    global food
    global score
    global direction

    canvas.delete(ALL)
    label.config(text="Score: 0")
    score = 0
    direction = 'down'
    snake = Snake()
    food = Food()
    next_turn(snake, food)

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70),
                       text="GAME OVER", fill="red", tags="gameover")
    restart_button = Button(window, text="Restart", bg="white", command=restart_game)
    canvas.create_window(GAME_WIDTH//2, GAME_HEIGHT//2 + 70, window=restart_button)

def initial_screen():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70),
                       text="SNAKE GAME", fill="red")
    start_button = Button(window, text="PLAY", bg="white", command=start_game)
    canvas.create_window(GAME_WIDTH//2, GAME_HEIGHT//2 + 70, window=start_button)

def start_game():
    global snake
    global food
    canvas.delete(ALL)
    snake = Snake()
    food = Food()
    next_turn(snake, food)

snake = None
food = None
score = 0
direction = 'down'

window = Tk()
window.title("Snake Game")
window.resizable(False, False)
window.focus_set()

label = Label(window, text="Score: {}". format(score), font=('consolas', 20))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

initial_screen()

window.mainloop()
