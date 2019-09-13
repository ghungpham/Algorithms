#!/usr/bin/python

import sys


# def rock_paper_scissors(n):
#   opts = ['rock', 'paper', 'scissors']
#   plays= []
#   def recursion(n, play):
#     if n == 0:
#       plays.append(play)
#     for i in opts:
#       updatedPlay = play.copy()
#       updatedPlay.append(i)    
#     recursion([], n)
#     return plays


plays = []

def rock_paper_scissors(n, play):
  options = ['rock', 'paper', 'scissors'] 
  
  if n == 0:
    plays.append(play)
  else:
    for i in options:
      updatedPlay = play.copy()
      updatedPlay.append(i)
      rock_paper_scissors(n-1, updatedPlay)

  return plays


print(rock_paper_scissors(1))
        
      


print(rock_paper_scissors(0))


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')