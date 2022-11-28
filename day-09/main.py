import os
from art import logo

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

print(logo)

bids = {}

while True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid
    answer = input("are there any other bidders? Type 'yes' or 'no'.\n")
    if answer == "no":
        find_highest_bidder(bids)
        break
    clear()