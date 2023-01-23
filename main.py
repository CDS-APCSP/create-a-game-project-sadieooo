import os, time

health = 100
machete = False
explosives = False

def startGame():
  os.system('clear') # clear the screen for the player
  print("Welcome explorers! Your name is Jungle Mike and you'll be navigating through an adveture game where the goal is to escape the jungle!")
  print()
  print()
  print("Let's get started!")
  time.sleep(5) # wait 3 seconds before moving on
  cave1() # runs to send the player to cave #1

def cave1():
  global machete # use the shovel variable from the top
  os.system('clear')

  ##############
  print("Do you want to bring your machete?")
  decision = input(">>").strip().lower()
  if decision.find("yes") > -1:
    machete = True
  if not machete:
    print("You can't get through the thick forestry, you start to crawl under the bushes and trees.")
    time.sleep(5)  
    snakeBite()
  else:
    print("You cut yourself a path, at the end of the path you see a glowing skull, do you run towards it?")
####################
    decision = input(">>").strip().lower()
    if decision.find("yes") > -1:
      print ("You run to the skull, you touch the skull and it transports you to the top of a mountain.")
      time.sleep(3)
      topOfMountain()
    else:
      time.sleep(3)
      cave1()
  # elif decision.find("wake up") > -1:
  #   print("You showered, you aren't stinky!")
  #   time.sleep(3)
  #   cave1()
  # elif decision.find("snooze") > -1:
  #   print("uh oh you're running late!")
  #   time.sleep(3)
  #   cave2()
  # else:
  #   print("Sorry, that command is not found.")
  #   time.sleep(3)
  #   cave1()
  

def topOfMountain():
  global explosives, health
  os.system('clear')
  print("Welcome to Top of the Mountain")
  print("Do you want to roll down the hill or try to run down the hill (answer with roll or run")
  decision = input(">>").strip().lower()
  if decision.find("roll") > -1:
    print ("You start rolling down the hill, you suprisingly dodge all of the dangerous sticks and rocks in the ground. You land at the top of a river.") 
    time.sleep(3)
    riverAdventure()
  else:
    print ("You tried to run down the hill but you run into the biggest tree you've ever seen")
    time.sleep(4)  
    runningDeath()
  
  
def snakeBite():
  global explosives, health
  os.system('clear')
  print('You got bit by a freakin huge snake')
  time.sleep(3)
  print ("You died.")
  time.sleep(2)
  print ("Game Over:(")

def runningDeath():
  print ("You died.")
  time.sleep(2)
  print ("Game Over:(")
def riverAdventure():
  os.system('clear')
  print ("Do you want to swim down the river or walk around it?")
  decision = input(">>").strip().lower()
  if decision.find("swim") > -1:
    print ("You start swimming down the river, YOU SEE AN ALLIGATOR!!! do you swim faster or duel it with your machete?") 
  decision = input(">>").strip().lower()
  if decision.find("duel") > -1:
    print("YOU KILLED THE FREAKING ALLIGATOR, you reach the end of the river and you can finally see the end of the jungle! Congrats you win!")
  else:
    time.sleep(3)
    alligatorDeath()
def alligatorDeath():
  print ("You died.")
  time.sleep(2)
  print ("Game Over:(")
def endGame():
  os.system("clear")
  pass

startGame()


#You run to the skull, you touch the skull and it transports you to the top of a mountain.