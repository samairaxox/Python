ids = {}
bidding_finished = False
def find_higherbidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bidding_amt = bidding_record[bidder]
        if bidding_amt > highest_bid:
            highest_bid = bidding_amt
            winner = bidder
    print(f"The winner of the silent auction is {winner} with the bid of ${highest_bid}")
while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  conti = input("Are there more bidders?. Type 'yes' or 'no'\n ")
  if conti == "no":
   bidding_finished = True
   find_higherbidder(bids)
  else:
     print("Next bidder")
