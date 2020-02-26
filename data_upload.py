from pbn_reader import deals, results

# below to see each deal and result individually
for deal in deals:
    # process each deal into 8 distributions
    # first, currently disregard seats:
    process_deal = deal[2:]
    # note, the each hand is 16 cards spaced 1 apart
    one = process_deal[0:16]
    two = process_deal[16:32]
    print(one,two)
for result in results:
    print(result)


