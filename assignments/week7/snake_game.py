from turtle import *
import os 
import time
from random import *
import csv
from datetime import datetime

delay = 0.1

score = 0
high_score = 0
DEBUG = True
script_dir = os.path.dirname(os.path.abspath(__file__))
record_file = os.path.join(script_dir, "snake_records.csv")

wn = Screen()
wn.title("Snake Game")
wn.bgpic(r"C:\Users\kliog\Desktop\Uni Leuphana\Tech Basics\My repos\techBasics1_Klio_Gosden\assignments\week7\grassy.gif")
wn.setup(width=600, height=600)
wn.tracer(0)
player_name = wn.textinput("Player Name", "Enter your name:")

head = Turtle()
head.speed(0)
head.shape("square")
head.color("darkorange")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

pen = Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.ht()
pen.goto(0, 260)
pen.write("Score: 0     High Score: 0", align = "center", font = ("Futura", 24, "normal"))

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up": 
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

wn.listen()
wn.onkey(go_up, "w")
wn.onkey(go_down, "s")
wn.onkey(go_left, "a")
wn.onkey(go_right, "d")

def save_record(name, score):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        file_exists = os.path.isfile(record_file)

        with open(record_file, "a", newline="") as file:
            writer = csv.writer(file)

            # create header if file does not exist
            if not file_exists:
                writer.writerow(["Name", "Timestamp", "Score"])

            writer.writerow([name, timestamp, score])

    except Exception as e:
        print("Error while saving:", e)


def load_leaderboard():
    records = []

    try:
        with open(record_file, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                name = row[0]
                timestamp = row[1]
                score = int(row[2])

                records.append((name, timestamp, score))

        records.sort(key=lambda x: x[2], reverse=True)

    except FileNotFoundError:
        print("No record file found yet.")

    except Exception as e:
        print("Error while loading leaderboard:", e)

    return records


def show_leaderboard():
    records = load_leaderboard()

    print("\n=== LEADERBOARD ===")

    if len(records) == 0:
        print("No records yet.")
        return

    for i, record in enumerate(records[:5], start=1):
        print(f"{i}. {record[0]} - {record[2]} points - {record[1]}")


if DEBUG:
    print("Debug mode activated")
    fake_score = 0
    save_record(player_name, fake_score)
    show_leaderboard()
    quit()


while True:
    wn.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        final_score = score

        save_record(player_name, final_score)
        show_leaderboard()

        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score: {}     High Score: {}".format(score, high_score), align = "center", font = ("Futura", 24, "normal"))


    if head.distance(food) < 20:
        x = randint(-270,270)
        y = randint(-270,270)
        food.goto(x, y)

        new_segment = Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001

        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}     High Score: {}".format(score, high_score), align = "center", font = ("Futura", 24, "normal"))

    for index in range(len(segments) -1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            final_score = score

            save_record(player_name, final_score)
            show_leaderboard()

            score = 0
            delay = 0.1
            
            pen.clear()
            pen.write("Score: {}     High Score: {}".format(score, high_score), align = "center", font = ("Futura", 24, "normal"))

    time.sleep(delay)

wn.mainloop()