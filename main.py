'''
  Name: 
  James Hargest College
  Programming Internal for 1.7 ~ 4 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
import time
import randit
  
print("Welcome to the Music Quiz!")
print("By Oliver!")
print("🎵🎶🎹🎸")
time.sleep(1)
print("Loading...")
time.sleep(3)

Music_list_dict = {
'Questions' : randit['Who made the album The Dark Side of The Moon?']
}
Music_list_dict = {
  'Answers' : ['Pink Floyd']
}


Enter_to_play = input("Please type 'ENTER' to start the quiz>>")
  
if Enter_to_play == 'ENTER':
  print("All right!")
  print("Lets start the quiz!")
else:
  print("Invalid input, please try again.")
  
  

  
  
  



