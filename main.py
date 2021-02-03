from replit import clear
from art import logo
print(logo)

bid_finished=False
bidder_record={}

while not bid_finished:
  name=input("What's your name?")
  price=int(input("What's your price? $"))
  bidder_record[name]=price
  bidder_continue=input("Do you add any other bidder name? Yes or No.")
  if bidder_continue=="No":
    bid_finished=True
  else:
    clear()


def bid_win(bidder_record):
  highest_price=0
  for name in bidder_record:
    bidder_price=bidder_record[name]
    if bidder_price>highest_price:
      highest_price=bidder_price
      winner=name
    else:
      continue
  print(f"The highest price is ${highest_price} with {winner}")

bid_win(bidder_record)
    
    
       



  
