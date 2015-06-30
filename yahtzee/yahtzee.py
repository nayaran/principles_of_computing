"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """

    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set
def gen_hold_helper(outcomes, length):
    """
    Function that creates all permuations of the given length
    from outcomes
    """

    ans = set([()])

    for dummy_index in range(length):
        temp = set()
        to_add = False
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                # First verify that the item is not already taken
                # and then add to the sequence
                for temp_item in outcomes:
                    if temp_item != item:
                        if temp_item not in new_seq:
                            to_add = True
                        else:
                            to_add = False
                            break
                if to_add:
                    new_seq.append(item)
                    # To make sure we are generating distinct combinations,
                    # exploit the no-duplicates-allowed property of the set,
                    # by sorting the sequence before adding it to the ans

                    #if new_seq.count(item) <= outcomes.count(item):
                    temp.add(tuple(sorted(new_seq)))
        ans = temp


    return ans
def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score
    """
    print hand
    max_score = 0
    score_dict = {}

    # Create a dictionary for all the values of the dice and
    # populate it with the values in the current hand
    for dice_value in hand:
        if dice_value in score_dict.keys():
            score_dict[dice_value] += dice_value
        else:
            score_dict[dice_value] = dice_value

    print score_dict

    # Find the maximum score for the given hand
    max_score = max(score_dict.values())

    print max_score
    return max_score


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """

    expected_value = 0.0

    # Generate [1, 2, 3, 4, 5, 6]
    outcomes = [dice_value for dice_value in range(1, 7)]

    length = num_free_dice

    # Generate all the possible outcomes
    all_sequences = gen_all_sequences(outcomes, length)
    print all_sequences

    # Compute expected values of the generated outcomes
    for seq in all_sequences:
        for dice_value in seq:
            expected_value += (dice_value * (1.0/6.0))

    print expected_value

    # Compute expected value for the held dices and generated outcomes
    for dice_value in held_dice:
        expected_value += (dice_value * (1.0/6.0))

    print expected_value

    return expected_value

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    length = len(hand)
    possible_holds = set([()])


    for dummy_index in range(length+1):
        #current_hold = gen_all_sequences(hand, dummy_index)
        current_hold = gen_hold_helper(hand, dummy_index)

        for seq in current_hold:
            possible_holds.add(seq)


    ans = set([()])
    temp2 = []

    for seq in possible_holds:
        if len(seq) > 0:
            if seq.count(seq[0]) == hand.count(seq[0]):
                temp2.append(seq)

    ans = temp2

    print 'total_holds- ', len(ans)
    print ans

    return ans

def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    return (0.0, ())

def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 2, 1, 5, 6)
    print
    print 'score', hand
    score(hand)

    print

    held_dice = (1, 1)
    num_free_dice = len(hand) - len(held_dice)
    print 'expected_value(', held_dice,
    print ',', num_die_sides,
    print ',',num_free_dice,
    print ')'
    expected_value(held_dice, num_die_sides, num_free_dice)

    print
    #hand = (1, 2, 1)

    print 'gen_all_holds', hand, ''
    gen_all_holds(hand)

#    hand_score, hold = strategy(hand, num_die_sides)
#    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score

run_example()

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)







