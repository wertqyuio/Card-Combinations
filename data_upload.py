from pbn_reader import date, deals, results

# all_hands records all the hands before saving into database
all_hands = []
suits = ["s", "h", "d", "c"]

# below to see each deal and result individually
for deal in deals:
    # process each deal into 8 distributions
    # first, currently disregard seats:
    process_deal = deal[2:].split(" ")
    for hand in process_deal:
        all_hands.append(hand.split("."))

for idx_board in range(len(deals)):
    for idx_hand in range(2):
        for idx_suit in range(4):
            left_hand = all_hands[4*idx_board+idx_hand][idx_suit]
            right_hand = all_hands[4*idx_board+idx_hand+2][idx_suit]
            print(idx_board+1, suits[idx_suit], left_hand, right_hand)


# print(all_hands)
# for result in results:
#     print(result)
