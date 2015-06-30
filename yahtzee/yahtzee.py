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
                new_seq.append(item)

                # Make sure that an item is not repeated more than
                # the no of times it actually appears in the hand
                if new_seq.count(item) <= outcomes.count(item):
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
    print
    print 'inside score......'
    print 'hand- ', hand


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

    print 'max_score- ', max_score
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
    print
    print 'inside expected_value......'
    print 'held_dice- ', held_dice
    print 'num_die_sides- ', num_die_sides
    print 'num_free_dice- ', num_free_dice


    expected_value = 0.0

    possible_expected_values = []

    # Generate [1, 2, 3, 4, 5, 6]
    outcomes = [dice_value for dice_value in range(1, 7)]

    length = num_free_dice

    # Generate all the possible outcomes
    all_sequences = gen_all_sequences(outcomes, length)
    #print all_sequences

    # Compute expected values of the generated outcomes
    for seq in all_sequences:
        current_expected = 0.0
        for dice_value in seq:
            current_expected += (dice_value * (1.0/6.0))

    possible_expected_values.append(current_expected)

    for value in possible_expected_values:
        expected_value += value

    expected_value = expected_value/len(possible_expected_values)

    # Compute expected value for the held dices and generated outcomes
    for dice_value in held_dice:
        expected_value += (dice_value)

    print 'expected_value- ', expected_value

    return expected_value

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    print
    print 'inside gen_all_holds......'
    print 'hand- ', hand


    length = len(hand)
    possible_holds = set([()])


    for dummy_index in range(length+1):
        current_hold = gen_hold_helper(hand, dummy_index)
        for seq in current_hold:
            possible_holds.add(seq)

    print 'total_holds- ', len(possible_holds)
    print 'holds- '
    print possible_holds

    return possible_holds

def strategy(hand, num_die_sides):

    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    print
    print 'inside strategy......'
    print 'hand- ', hand
    print 'num_die_sides- ', num_die_sides,

    all_possible_holds = gen_all_holds(hand)

    best_hold = ()
    max_expected = 0.0

    for held_dice in all_possible_holds:

        num_free_dice = len(hand) - len(held_dice)
        current_expectation = expected_value(held_dice, num_die_sides, num_free_dice)
        print
        print 'with held_dice- ', held_dice
        print 'expectation is- ', current_expectation

        if current_expectation > max_expected:
            max_expected = current_expectation
            best_hold = held_dice


    return (max_expected, best_hold)

    #return (0.0, ())

def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    print
    print 'playing yahtzee...........'
    num_die_sides = 6
    hand = (1, 1, 3, 4, 5)
    #print
    print 'hand', hand
    #score(hand)

    #print

    #held_dice = (1, 1)
    #num_free_dice = len(hand) - len(held_dice)
    #print 'expected_value(', held_dice,
    #print ',', num_die_sides,
    #print ',',num_free_dice,
    #print ')'
    #expected_value(held_dice, num_die_sides, num_free_dice)

    #print
    #hand = (1, 2, 1)

    #print 'gen_all_holds', hand, ''
    #gen_all_holds(hand)

    hand_score, hold = strategy(hand, num_die_sides)
    print
    print
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score

run_example()

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)







