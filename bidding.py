# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art

print(art.logo)

auction = {}

choice = "yes"

while choice == "yes":
    name = input("What is your name? ")
    bid_amount = int(input("What is your bid? "))
    auction[name] = bid_amount
    choice = input("Are there more bidders? Type 'Yes' or 'No' ").lower()

print("\n" * 1000)

key_with_max_value = max(auction, key=auction.get)
print("Winner is ", key_with_max_value)


