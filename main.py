ump_a_turtle
import turtle as trtl
import random as rand
import leaderboard as lb
#a121_catch_a_turtle.py
#-----import statements-----


#-----game configuration----
spot_color = "teal"
spot_height = 1
spot_shape = "arrow"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
inverse = rand.randint(1,6)
name = input("What is your name? ")
leaderboard_file_name = "a122_leaderboard.txt"
#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_height)
spot.fillcolor(spot_color)
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(160,160)
score_writer.pendown()
counter = trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-160,160)
counter.pendown()
#-----game functions--------
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score,font=font_setup)
def change_position():
    rx = rand.randint(-150, 150)
    ry = rand.randint(-150, 150)
    spot.goto(rx,ry)
def spot_clicked(x,y):
    global spot_height
    global timer,timer_up
    global spot_color
    global inverse
    inverse = rand.randint(1,6)
    if timer_up == False:
        spot.shapesize(rand.randint(2,12))
        spot.stamp()
        update_score()
        change_position()
        if inverse == 1:
            spot_color = "teal"
            spot.fillcolor(spot_color)
            inverse = rand.randint(1,6)
        elif inverse == 2:
            spot_color = "red"
            spot.fillcolor(spot_color)
            inverse = rand.randint(1,6)
        elif inverse == 3:
            spot_color = "gold"
            spot.fillcolor(spot_color)
            inverse = rand.randint(1,6)
        elif inverse == 4:
            spot_color = "orange"
            spot.fillcolor(spot_color)
            inverse = rand.randint(1,6)
        elif inverse == 5:
            spot_color = "green"
            spot.fillcolor(spot_color)
            inverse = rand.randint(1,6)
        elif inverse == 6:
            spot_color = "black"
            spot.fillcolor(spot_color)
            inverse = rand.randint(1,6)
    else:
        spot.hideturtle()
def manage_leaderboard():

  global score
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_names, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)
def game_start():
    user_start = input("Are you ready to start the game?(yes or no) ").lower()
    if user_start == "yes":
#-----events----------------
        trtl.bgcolor("purple")
        spot.speed(0)
# every time it clicks changes color stamps and size are changed
# function start game