'''
  Name: 
  James Hargest College
  Programming Internal for 1.7 ~ 4 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
import time

print("Welcome to the Music Quiz!")
print("By Oliver!")
print("🎵🎶🎹🎸")
time.sleep(1)
print("Loading...")
time.sleep(3)
print("Score is at 0")
score = 0

Music_list_dict1 = {
'Question' : 'Who made the album The Dark Side of The Moon?'
}
Music_list_dict2 = {
  'Answer' : 'Pink Floyd'
}


Enter_to_play = input("Please type 'ENTER' to start the quiz>>")
  
if Enter_to_play == 'ENTER':
  print("All right!")
  print (Music_list_dict1)
  answer = input(">>")
  if answer == (Music_list_dict2):
    print ("Well done!")
    score = +10
    print("You now have 10 points!")
    
else:
  print("Invalid input, please try again.")
  score = 0
  print("You are wrong! You have got no points from this!")

  
  



  
  

  
  

  
  
  



