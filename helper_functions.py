def compare_hands(left, right):
    # function compares two hands and returns the longer one
    # if hands are equal length, returns the hand with the highest card
    if len(left) > len(right):
        return True
    elif len(left) < len(right):
        return False
    elif not len(left) and not len(right):
        # whenever both hands are 0 length return that the left is 'bigger'
        return True
    else:
        cards = ["2", "3", "4", "5", "6", "7",
                 "8", "9", "T", "J", "Q", "K", "A"]
        return cards.index(left[0]) > cards.index(right[0])


def convert_results(results_strings):
    # converts list of string of results into list of list of integers
    tricks = "0123456789abcd"
    return [[tricks.find(strain) for strain in results] for results in
            results_strings]
