"""
Functions to enumerate sequences of outcomes
Repetition of outcomes is allowed
"""


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """
    ans = set([()])

    for dummy_index in range(length):

        temp = set()

        for seq in ans:
            for item in outcomes:

                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))

        ans = temp

    return ans

def gen_sorted_sequences_ver1(outcomes, length):
    """
    Function that creates all sorted sequences via gen_all_sequences
    """
    all_sequences = gen_all_sequences(outcomes, length)

    sorted_sequences = [tuple(sorted(sequence)) for sequence in all_sequences]
    return set(sorted_sequences)

def gen_sorted_sequences_ver2(outcomes, length):
    """
    Function that creates all sorted sequences from scratch
    """
    #all_sequences = gen_all_sequences(outcomes, length)

    #sorted_sequences = [tuple(sorted(sequence)) for sequence in all_sequences]
    #return set(sorted_sequences)
    ans = set([()])

    for dummy_index in range(length):
        temp = set()

        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                new_seq = sorted(new_seq)
                temp.add(tuple(new_seq))
        ans = temp

    return ans

def gen_permutations(outcomes, length):
    """
    Function that creates all permuations of the given length
    from outcomes
    """

    ans = set([()])

    for dummy_index in range(length):
        temp = set()

        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                if item not in new_seq:
                    new_seq.append(item)
                    temp.add(tuple(new_seq))

        ans = temp

    return ans

def gen_combinations(outcomes, length):
    """
    Function that creates all permuations of the given length
    from outcomes
    """

    ans = set([()])

    for dummy_index in range(length):
        temp = set()

        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                if item not in new_seq:
                    new_seq.append(item)
                    temp.add(tuple(sorted(new_seq)))

        ans = temp

    return ans
def print_seq(sequence):
    """
    Prints the sequence line by line
    """
    for seq in sequence:
        print seq

# example

def run_example1():
    """
    Example of all sequences
    """
    #outcomes = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    #outcomes = set(["Red", "Green", "Blue"])
    #outcomes = set(["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])

    outcomes =set(list('abc'))
    length = 2

    seq_outcomes = gen_all_sequences(outcomes, length)
    print
    print "All Sequences"
    print "-------------------------------------------"

    print "Computed", len(seq_outcomes), "sequences of", str(length), "outcomes"
    print "Sequences were- "
    print_seq(seq_outcomes)

    print
    print "Sorted Sequences"
    print "-------------------------------------------"

    seq_outcomes = gen_sorted_sequences_ver2(outcomes, length)
    print "Computed", len(seq_outcomes), "sorted sequences of", str(length) ,"outcomes"
    print "Sequences were- "
    print_seq(seq_outcomes)
    print
    print "Permutations"
    print "-------------------------------------------"
    seq_outcomes = gen_permutations(outcomes, length)
    print "Computed", len(seq_outcomes), "permutations of", str(length) ,"outcomes"
    print "Permutations were- "
    print_seq(seq_outcomes)
    print
    print "Combinations"
    print "-------------------------------------------"

    seq_outcomes = gen_combinations(outcomes, length)
    print "Computed", len(seq_outcomes), "combinations of", str(length) ,"outcomes"
    print "Combinations were- "
    print_seq(seq_outcomes)

    print




run_example1()

