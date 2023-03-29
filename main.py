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
def welcome_message():
    print("Welcome to the Music Quiz!")
    print("By Oliver!")
    print("🎵🎶🎹🎸")
    print("You need to get 30 points to pass the quiz! You have 4 chances!")
    time.sleep(1)
    print("Loading...")
    print('Starting in:')
    # countdown
    for delay in range(5, 0, -1):
        time.sleep(1)
        print(delay)
    time.sleep(3)
    print("Score is currently at 0")

def play_again():
    again = input("Do you want to repeat the quiz?")
    if again.lower() == 'yes':
        return True
    else:
        print("Goodbye! Thanks for playing!")
        return False

# tells the welcome function to show the welcome message
welcome_message()

score = 0
chances = 4

# dictionary
music_list_dict = {
    'Question 1': {'Question': 'Who made the album The Dark Side of The Moon?', 'Answer': 'Pink Floyd'},
    'Question 2': {'Question': 'Who is the lead singer of Led Zepplin?', 'Answer': 'Robert Plant'},
    'Question 3': {'Question': 'What band has been going for the longest time live?', 'Answer': 'The Rolling Stones'},
    'Question 4': {'Question': 'What is the most hated music genre?', 'Answer': 'Jazz'},
    'Question 5': {'Question': 'What is the best selling album of all time?', 'Answer': 'Thriller'},
    'Question 6': {'Question': 'What is The Beatles first album?', 'Answer': 'Please Please Me'},
    'Question 7': {'Question': 'What symbol was on Ed Sheerans 2011 album?', 'Answer': '+'}
}

# loop to start the quiz so you cannot just randomly put anything
while True:
    enter_to_play = input("Please type 'ENTER' to start the quiz>>")
    if enter_to_play == 'ENTER':
        print("All right!")
        name = input("What is your name?>>   ")
        print("Welcome", name)
        break
    else:
        print("Please type what I ask :(")

# randomly generated questions from the dict
while True:
    if score == 30:
        print("You have passed the quiz! Well done!")
        if play_again():
            score = 0
            chances = 4
        else:
            break
    elif chances == 0:
        print("You have lost all of your chances!")
        if play_again():
            score = 0
            chances = 4
        else:
            break
    else:
        random_music_questions = random.choice(list(music_list_dict.values()))
        print(random_music_questions["Question"])
        answer = input(">>")
        if answer.lower() == random_music_questions["Answer"].lower():
            print("Well done! You got this right!")
            score += 5
            print("\033[1;32m That is correct! Well done! \n")
            print("\033[0;37;40m ..........................................................\n")
            print("Your score is now at", score, "!")
        else:
            print("\033[1;31;40m That is incorrect!  \n")
            print("\033[0m.........................................................\n")
            chances -= 1
        print("You now have", chances, "chances left!")

    

  

  
  



  
  

  
  

  
  
  



