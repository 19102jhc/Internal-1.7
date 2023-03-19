'''
  Name: 
  James Hargest College
  Programming Internal for 1.7 ~ 4 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
#imports
import time
import random

print("Welcome to the Music Quiz!")
print("By Oliver!")
print("🎵🎶🎹🎸")
time.sleep(1)
print("Loading...")
print('Starting in: ')

for delay in range(5, 0, -1):
  time.sleep(1)
  print(delay)
  
time.sleep(3)
print("Score is currently at 0")
score = 0

Music_list_dict1 = {
'Question' : 'Who made the album The Dark Side of The Moon?', 'Answer': 'Pink Floyd'}
{
'Question' : 'Who is the lead singer of Led Zepplin?', 'Answer': 'Robert Plant'}




Enter_to_play = input("Please type 'ENTER' to start the quiz>>")
  
if Enter_to_play == 'ENTER':
  print("All right!")

  while score <30:
    random_music_questions = random.choice(Music_list_dict1)
    print (random_music_questions(Music_list_dict1))
  answer = input(">>")
  if answer == (Music_list_dict1):
    print ("Well done!")
    score = +5
    print("You now have 5 more points!")
    #end of game
while True:
  if score == 30:
    print("You have passed the quiz! Well done!")
    again = input("Do you want to repeat the quiz?")
  if again == 'yes':
    print("Welcome back!")
    #repeat the quiz
    if again == 'no':
      print("Goodbye! Thanks for playing!")
  break
else:
    #new question added
  #currently fixing 
  print("Invalid input, please try again.")
score = 0
print("You are wrong! You got no points from this!")



    

  

  
  



  
  

  
  

  
  
  



