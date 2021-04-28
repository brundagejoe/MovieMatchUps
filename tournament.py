from elopy import *
import random
i = Implementation()

def start_match(optionA, optionB):
  answer = '!'
  while answer == '!':
    answer = input(optionA +' or ' + optionB + "? ")
    if answer == '<':
      winner = optionA
      i.recordMatch(optionA, optionB, winner=optionA)
    elif answer == '>':
      winner = optionB
      i.recordMatch(optionA, optionB, winner=optionB)
    else:
      print("Invalid option")
      answer = '!'
      
# i.addPlayer("Hank")
# i.addPlayer("Bill")
# start_match("Hank","Bill")

Star_Wars_list = ["The Phantom Menace", "Attack of the Clones", "Revenge of the Sith", 
                  "Solo: A Star Wars Story", "Rogue One: A Star Wars Story", 
                  "A New Hope", "The Empire Strikes Back", "Return of the Jedi",
                  "The Force Awakens", "The Last Jedi", "Rise of Skywalker"]

for movie in Star_Wars_list:
  i.addPlayer(movie)

def start_tournament(input_list):
  for i in range(10):
    matchup = random.sample(range(len(input_list)), 2)
    start_match(input_list[matchup[0]], input_list[matchup[1]])

start_tournament(Star_Wars_list)
unordered_list = i.getRatingList()
output_list = sorted(unordered_list, key = lambda x: x[1], reverse=True)
print(output_list)
