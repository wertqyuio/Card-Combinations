# this file extracts all the deals from the PBN file and the double dummy 
# tricks

# optimizations include skipping file lines during reading

filepath = "qt200217.pbn"
deals = []
results = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        line = fp.readline()
        if line[:6] == "[Deal ":
            deal = line[7:line.find("]")-1]
            deals.append(deal)
        elif line[:19] == "[DoubleDummyTricks ":
            result = line[20:line.find("]")-1]
            results.append(result)

# below to see each deal and result individually
# for deal in deals:
#     print(deal)
# for result in results:
#     print(result)
