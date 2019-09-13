#!/usr/bin/python

import sys

def making_change(amount, denominations):
  counts = []
  ways = 0

  if amount <= 0:
    ways = 1
  else:
    for i in range(0, len(denominations)):
      if amount >= denominations[i]:
        ways += making_change(amount - denominations[i], denominations)
  
  return ways



if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")