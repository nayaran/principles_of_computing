"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """

    # creates a copy of the line

#   print
#   print 'input - ', line
    row = list(line)
    result = [0] * len(line)

    # result line
    dest_index = 0

    # flag to make sure that we merge a tile only once
    can_merge = True

 #   print

    # iterate over the given row and
    # if found non_zero value,
    # either merge it with the previous
    # value in the result or put it as it is
    #
    for source_index in range(len(row)):

        if row[source_index]:

            # if non_zero value found
#           print 'source_index- ', source_index, row
#           print 'dest_index- ', dest_index, result

            if result[dest_index-1] == row[source_index] and can_merge:
                # merge can be done
                # hence merge
                result[dest_index-1] *= 2

                # disable merging for the merged tile
                can_merge = False

            else:

                # no merging can be done
                # hence copy the value as it is
                result[dest_index] = row[source_index]
                dest_index += 1

                # enable merging
                can_merge = True

#        print result
#        print

    return result



def test(merge2048):
    """
    Function that tests the merge2048 method in 2048.
    """
    print "Test Case #1-"
    print "Input-\t[0, 0, 2, 2]"
    print "Expects-[4, 0, 0, 0]"
    print "Got-\t", merge2048([0, 0, 2, 2])
    print

    print "Test Case #2-"
    print "Input-\t[2, 0, 2, 4]"
    print "Expects-[4, 4, 0, 0]"
    print "Got-\t", merge2048([2, 0, 2, 4])
    print

    print "Test Case #3-"
    print "Input-\t[2, 2, 0, 0]"
    print "Expects-[4, 0, 0, 0]"
    print "Got-\t", merge2048([2, 2, 0, 0])
    print

    print "Test Case #4-"
    print "Input-\t[2, 2, 2, 2, 2]"
    print "Expects-[4, 4, 2, 0, 0]"
    print "Got-\t", merge2048([2, 2, 2, 2, 2])
    print

    print "Test Case #5-"
    print "Input-\t[8, 16, 16, 8]"
    print "Expects-[8, 32, 8, 0]"
    print "Got-\t", merge2048([8, 16, 16, 8])
    print

    print "Test Case #6-"
    print "Input-\t[2, 0, 2, 4, 0, 4, 8, 8]"
    print "Expects-[4, 8, 16, 0, 0, 0, 0, 0]"
    print "Got-\t", merge2048([2, 0, 2, 4, 0, 4, 8, 8])
    print

test(merge)
