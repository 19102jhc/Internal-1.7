'''
  Name: Oliver van Uden-Smith
  James Hargest College
  Programming Internal for 1.7 ~ 4 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
import time
import random

def the_welcome_message():
    print("Welcome to the Music Quiz!")
    print("By Oliver!")
    print("🎵🎶🎹🎸")
    print("You need to get 30 points to pass the quiz! You have 4 chances!")
    time.sleep(1)
    print("Loading...")
    print('Starting in:')
    
    # countdown from 5 to start the quiz
    for delay in range(5, 0, -1):
        time.sleep(1)
        print(delay)
    
    time.sleep(3)
    print("Score is currently at 0")


def play_again():
    again = input("Do you want to repeat the quiz? yes or no")
    
    if again.lower() == 'yes':
        return True
    else:
        print("Goodbye! Thanks for playing!")
        time.sleep(9999)
        return False

    
#Grabs the welcome message to loop back to when the welcome message acually happens
the_welcome_message()

score = 0
chances = 4

# dictionary of multiple questions on music
music_list_dict = {
    'Question 1': {'Question': 'Who made the album The Dark Side of The Moon?', 'Answer': 'Pink Floyd'},
    'Question 2': {'Question': 'Who is the lead singer of Led Zepplin?', 'Answer': 'Robert Plant'},
    'Question 3': {'Question': 'What band has been going for the longest time live?', 'Answer': 'The Rolling Stones'},
    'Question 4': {'Question': 'What is the most hated music genre?', 'Answer': 'Jazz'},
    'Question 5': {'Question': 'What is the best selling album of all time?', 'Answer': 'Thriller'},
    'Question 6': {'Question': 'What is The Beatles first album?', 'Answer': 'Please Please Me'},
    'Question 7': {'Question': 'What symbol was on Ed Sheerans 2011 album?', 'Answer': '+'},
    'Question 8': {'Question': 'What was the first rap song to reach number 1 on the US Billboard Hot 100 chart?', 'Answer': 'Rapper\'s Delight'},
    'Question 9': {'Question': 'Who won the album of the Year at the 2022 Grammy Awards?', 'Answer': 'Taylor Swift'},
    'Question 10': {'Question': 'Which artist holds the record for the most Grammy Awards won?', 'Answer': 'Georg Solti'},
    'Question 11': {'Question': 'What was the name of Nirvana\'s lead singer?', 'Answer': 'Kurt Cobain'},
    'Question 12': {'Question': 'Who wrote the song "Bohemian Rhapsody"?', 'Answer': 'Freddie Mercury'},
    'Question 13': {'Question': 'What was the first music video ever aired on MTV?', 'Answer': 'Video Killed the Radio Star'},
    'Question 14': {'Question': 'Who is the highest selling female artist of all time?', 'Answer': 'Madonna'},
    'Question 15': {'Question': 'What was the name of Beyonce\'s first solo album?', 'Answer': 'Dangerously in Love'},
    'Question 16': {'Question': 'What was the first music album to be released on CD?', 'Answer': '52nd Street'},
    'Question 17': {'Question': 'What is the most streamed song of all time on Spotify?', 'Answer': 'Shape of You'},
    'Question 18': {'Question': 'Who is known as the "King of Pop"?', 'Answer': 'Michael Jackson'},
    'Question 19': {'Question': 'What is the name of Taylor Swift\'s debut album?', 'Answer': 'Taylor Swift'},
    'Question 20': {'Question': 'Who is the lead singer of the Red Hot Chili Peppers?', 'Answer': 'Anthony Kiedis'},
    'Question 21': {'Question': 'What is the name of the first album released by Eminem?', 'Answer': 'Infinite'},
    'Question 22': {'Question': 'Who composed the music for the film "The Lion King"?', 'Answer': 'Hans Zimmer'},
    'Question 23': {'Question': 'What is the name of the lead singer of Coldplay?', 'Answer': 'Chris Martin'}
}

# loop to start the quiz so you cannot just randomly put anything
while True:
    enter_to_play = input("Please type 'ENTER' to start the quiz>>")
    if enter_to_play.upper() == 'ENTER':
        print("All right!")
        name = input ("What is your name?")
        print("Welcome", name)

        break
    else:
        print("Please type what I ask :(")


while True:
  #if user has 30 points, code asks if you want to repeat or not. If so, the code loops back to when the questions are asked, otherwise it breaks.
    if score == 30:
        print("You have passed the quiz! Well done!")
        if play_again():
            score = 0
            chances = 4
        else:
            break

  
          #if user has 0 chances left, code asks if you want to repeat or not. If so, the code loops back to when the questions are asked, otherwise it breaks.
    elif chances == 0:
        print("You have lost all of your chances!")
        if play_again():
            score = 0
            chances = 4
        else:
          break

          # randomly generated questions from the dict
    else:
        random_music_questions = random.choice(list(music_list_dict.values()))
        print(random_music_questions["Question"])
        answer = input(">>")
      #if answer matches the answer in the dict, they gain 5 points, they can also type the questions in lower or uppercase and they will still get it right. This is because of the .lower, .upper points.

      
        if answer.lower() == random_music_questions["Answer"].lower():
            print("Well done! You got this right!")
            score += 5
            print("\033[1;32m That is correct! Well done! \n")
            print("\033[0;37;40m ..........................................................\n")
            print("Your score is now at", score, "!")

      
        else:
          #else, they loose one chance, and the quiz picks another random question from the dict
            print("\033[1;31;40m That is incorrect!  \n")
            print("\033[0m.........................................................\n")
            chances -= 1
        print("You now have", chances, "chances left!")