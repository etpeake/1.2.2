#leaderboard.py
# The leaderboard module to be used in Activity 1.2.2
# set the levels of scoring
bronze_score = 15
silver_score = 20
gold_score = 25

# return names in the leaderboard file
def get_names(file_name):
  leaderboard_file = open(file_name, "r")  # be sure you have created this
  # use a for loop to iterate through the content of the file, one line at a time
  # note that each line in the file has the format "leader_name,leader_score" for example "Pat,50"
  names = []
  for line in leaderboard_file:
    leader_name = ""
    index = 0
    # TODO 1: use a while loop to read the leader name from the line (format is "leader_name,leader_score")
    while (line[index] != ","):
      leader_name = leader_name + line[index]
      index = index + 1
    # TODO 2: add the player name to the names list
    names.append(leader_name)
  print("names:", names)

  leaderboard_file.close()

  #  TODO 6: return the names list in place of the empty list
  return names
 
# return scores from the leaderboard file
def get_scores(file_name):
  leaderboard_file = open(file_name, "r")  # be sure you have created this
  scores = []
  for line in leaderboard_file:
    leader_score = ""    
    index = 0
    # TODO 3: use a while loop to index beyond the comma, skipping the player's name
    while (line[index] != ","):
      index = index + 1
    index = index + 1
    # TODO 4: use a while loop to get the score
    while (line[index] != "\n"):
      leader_score = leader_score + line[index]
      index = index + 1
    # TODO 5: add the player score to the scores list
    scores.append(int(leader_score))
  print("scores:", scores)
   
  leaderboard_file.close()
  # TODO 7: return the scores in place of the empty list
  return scores
# update leaderboard by inserting the current player and score to the list at the correct position
def update_leaderboard(file_name, leader_names, leader_scores,  player_name, player_score):
  # TODO 8: loop through all the scores in the existing leaderboard list
  for index in range(len(leader_scores)):
    # TODO 9: check if this is the position to insert new score at
    if (player_score >= leader_scores[index]):
      break
    else:
      index = index + 1
 
  # TODO 10: insert new player and score
  leader_names.insert(index, player_name)
  leader_scores.insert(index, player_score)
  # TODO 11: keep both lists at 5 elements only (top 5 players)
  if (len(leader_names) > 5):  # can use scores list in place of names
    leader_names.pop()
    leader_scores.pop()
   # TODO 12: store the latest leaderboard back in the file
  leaderboard_file = open(file_name, "w")  # this mode opens the file and erases its contents for a fresh start
 
   # TODO 13 loop through all the leaderboard elements and write them to the the file
  for index in range(len(leader_names)): # note:can use scores list in place of names
    if (player_score >= gold_score):
        turtle_object.write("You earned a gold medal!", font=font_setup)
    elif (player_score >= silver_score):
        turtle_object.write("You earned a silver medal!", font=font_setup)
    elif (player_score >= bronze_score):
        turtle_object.write("You earned a bronze medal!", font=font_setup)
