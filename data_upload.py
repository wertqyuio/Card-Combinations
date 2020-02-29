from pbn_reader import date, deals, results
from database_setup import create_connection
from database_credentials import PGDATABASE, PGUSER, PGPASSWORD
from helper_functions import compare_hands

# all_hands records all the hands before saving into database
all_hands = []
suits = ["s", "h", "d", "c"]
insert_deals = []
insert_distributions = []

connection = create_connection(
    PGDATABASE, PGUSER, PGPASSWORD, "127.0.0.1", "5432"
)


# below to see each deal and result individually
for idx, deal in enumerate(deals):
    # process each deal into 8 distributions
    # first, currently disregard seats:
    process_deal = deal[2:].split(" ")
    insert_deals.append(
        (date[0], date[1], date[2], idx+1, " ".join(process_deal),
         results[idx]))
    for hand in process_deal:
        all_hands.append(hand.split("."))

deals_records = ", ".join(["%s"] * len(insert_deals))

insert_query_deals = (
    f"INSERT INTO deals (year, month, day, board, hands, results) VALUES {deals_records}"
)

for idx_board in range(len(deals)):
    for idx_hand in range(2):
        for idx_suit in range(4):
            # every field entered into database will have prefix - insert
            left_hand = all_hands[4*idx_board+idx_hand][idx_suit]
            right_hand = all_hands[4*idx_board+idx_hand+2][idx_suit]
            swap = False

            if not compare_hands(left_hand, right_hand):
                left_hand, right_hand = right_hand, left_hand
                swap = True
            insert_distributions.append((
                date[0], date[1], date[2], idx_board+1, suits[idx_suit],
                left_hand, right_hand, swap))

distributions_records = ", ".join(["%s"] * len(insert_distributions))

insert_query_distributions = (
    f'''INSERT INTO distributions (year, month, day, board, suit, long, short, swap)
     VALUES {distributions_records}'''
)

connection.autocommit = True
cursor = connection.cursor()

cursor.execute(insert_query_deals, insert_deals)
cursor.execute(insert_query_distributions, insert_distributions)
