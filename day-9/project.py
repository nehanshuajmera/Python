# Day 9 project
import os
print("\nWelcome to the secret auction program")

# creating empty dictionary
bidders = {}
bidding_finished = False

def find_winner(bidding_dict):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dict:
        bid_amt = bidding_dict[bidder]
        if bid_amt > highest_bid:
            highest_bid = bid_amt
            winner = bidder
    print("\nWinner is ",winner, "and bid amount is $",highest_bid)

while not bidding_finished:
    name  = input("\nWhat is your name? ")
    amount = int(input("\nWhat's your bid? $"))

    bidders[name] = amount

    more_bidders = input("\nAre there any other biders? Type 'yes' or 'no'.\n").lower()
    if more_bidders == "no":
        bidding_finished = True
        find_winner(bidders)    
    elif more_bidders == "yes":
        os.system('cls')
    else:
        print("Please enter correct input")