from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bidd = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = int(bidding_record[bidder])
    if bid_amount > highest_bidd:
      highest_bidd = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bidd}")
    

while not bidding_finished:
  name = input("What's your name?: ")
  price = input("What's your bid: $")
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
  
