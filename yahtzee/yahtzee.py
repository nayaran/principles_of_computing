"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

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

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score
    """

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

    current_hold = set()
    for dummy_index in range(length):
        current_hold = gen_all_sequences(hand, dummy_index)

    possible_holds = current_hold
    print possible_holds

    return set([()])

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
    hand = (1, 1, 1, 5, 6)
    print
    print 'score(hand)'
    score(hand)

    print

    held_dice = (1, 1, 1)
    num_free_dice = 2
    print 'expected_value(held_dice, num_die_sides, num_free_dice)'
    expected_value(held_dice, num_die_sides, num_free_dice)

    print
    print 'gen_all_holds((1, 2, 3))'
    #gen_all_holds((1, 2, 3))

#    hand_score, hold = strategy(hand, num_die_sides)
#    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score

run_example()

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)







