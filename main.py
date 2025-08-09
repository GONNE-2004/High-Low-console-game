from art import logo,vs
from game_data import data
import random
import os

# first import the top logo and print it
#2nd import the game data
print(logo)

def clear_screen():
  """Clears the terminal when for another guess"""
  # os.system checks whether the os is windows,mac or linux then uses the right command to clear terminal screen
  try:
    os.system("cls" if os.name == "nt" else "clear")
  except:
      print("\n" * 25) #Just in case the upper doesn't work in some IDLE



#Write a function the compares the follower count
def compare_follower(user_guess, a_follower, b_follower):
    """Holds comparsion between follower count"""
    if a_follower > b_follower:
        return user_guess == "a"
    else:
        return  user_guess == "b"


#write a function that returns the attributes
def attributes(person):
    """Returns the formated user charactersistics"""
    return f"{person["name"]}, {person["description"]}, from {person["country"]}"
    # i had to create the person argument to act in order to acts as the name of the name dictionary inside the list


def main():
  """prints the logos,keeps the game in loop, and game restart"""
  score = 0
  #generate a random person from data
  person_b = random.choice(data)
  play_game = True

  while play_game:
      #making person B become the next person A
      person_a = person_b
      person_b = random.choice(data)

      #making sure person A isn't same like person B
      while person_a == person_b:
          person_b = random.choice(data)

      print(f"Compare A :{ attributes(person_a)}")
      print(vs)
      print(f"Against B : {attributes(person_b)}")

      #asking th user who has more follower again and  again
      guess = input("Who has more followers? Type 'a' or 'b':  ").lower().strip()
      while guess not in ['a','b']:
              guess = input("Who has more followers? Type 'a' or 'b':  ").lower().strip()

      #clear screen after each guess
      clear_screen()
      print(logo)

      #getting the follower count
      a_follower_count = person_a["follower_count"]
      b_follower_count = person_b["follower_count"]

      #checking user guess
      is_correct = compare_follower(guess, a_follower_count,b_follower_count)

      #keeping user score and giving feedback
      if is_correct:
          score += 1
          print(f"You are right! Current score: {score}")
      else:
          print(f"You are wrong! Final score: {score}")
          play_again = input("Play again (y/n):  ").lower().strip()
          if play_again == "y":
            main() # restarts game in case user failed, it's implemented using recurssion
          else:
            play_game = False # ends game






main()