'''
  Name: Oliver van Uden-Smith
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
print("You need to get 30 points to pass the quiz! You have 4 chances!")
time.sleep(1)
print("Loading...")
print('Starting in: ')

for delay in range(5, 0, -1):
  time.sleep(1)
  print(delay)
  
time.sleep(3)
print("Score is currently at 0")
score = 0
chances = 4
#dictionary
Music_list_dict1 = {
'Question 1 ' : {'Question' : 'Who made the album The Dark Side of The Moon?', 'Answer': 'Pink Floyd'},
  
'Question 2 ' : {'Question' : 'Who is the lead singer of Led Zepplin?', 'Answer': 'Robert Plant'},

'Question 3 ' : {'Question' : 'What band has been going for the longest time live?', 'Answer': 'The Rolling Stones'},

'Question 4 ' : {'Question' :'What is the most hated music genre?', 'Answer': 'Jazz'},
  
'Question 5 ' : {'Question' :'What is the best selling album of all time?', 'Answer': 'Thriller'},
  'Question 6 ' : {'Question' :'What is The Beatles first album?', 'Answer': 'Please Please Me'},
}
while True:
  Enter_to_play = input("Please type 'ENTER' to start the quiz>>")
  break
  
if Enter_to_play == 'ENTER':
  print("All right!")
  name = input("What is your name?>>   ")
  print("Welcome", name )
else:
  print("Please type what I ask :(")
#randomly generated questions
while score <30:

  while chances >0:
    random_music_questions = random.choice(list(Music_list_dict1.values()))
    print(random_music_questions["Question"])
    answer = input(">>")
    if answer.lower() == random_music_questions["Answer"].lower():
        print("Well done! You got this right!")
        score +=5
        print("\033[1;32m That is correct! Well done! \n")
        print("\033[0;37;40m .........................................................\n")
        print("Your score is now at", score)
    else:
       print("\031[1;32;40m That is incorrect! \n")
       chances -=1
    print("You have",chances,"Chances left! ")
    print("You have gained", score, "points")
    #end of game
while True:
  if score == 30:
    print("You have passed the quiz! Well done!")
    again = input("Do you want to repeat the quiz?")
    if again.upper() == 'yes':
      score == 0
      chances == 4
      continue
    print("Welcome back!")
    break
    if chances ==0:
 
      print("Sadly you didn't pass the quiz!")
    again = input("Do you want to repeat the quiz?")
    if again.lower() == 'yes':
      score == 0
      chances == 4
      continue
    print("Alright!")
   
  elif again.lower() == 'no':
      print("Goodbye! Thanks for playing!")
  break
else:
  print("That is an invalid response!")






    

  

  
  



  
  

  
  

  
  
  



