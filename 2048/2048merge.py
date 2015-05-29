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
    destIndex = 0

    # flag to make sure that we merge a tile only once
    canMerge = True

 #   print

    # iterate over the given row and
    # if found non_zero value,
    # either merge it with the previous
    # value in the result or put it as it is
    #
    for sourceIndex in range(len(row)):

        if row[sourceIndex]:

            # if non_zero value found
#           print 'sourceIndex- ', sourceIndex, row
#           print 'destIndex- ', destIndex, result

            if result[destIndex-1] == row[sourceIndex] and canMerge:
                # merge can be done
                # hence merge
                result[destIndex-1] *= 2

                # disable merging for the merged tile
                canMerge = False

            else:

                # no merging can be done
                # hence copy the value as it is
                result[destIndex] = row[sourceIndex]
                destIndex += 1

                # enable merging
                canMerge = True

#        print result
#        print

    return result



def test(mergeMethod):
    """
    Function that tests the merge method in 2048.
    """
    print "Test Case #1-"
    print "Input-\t[0, 0, 2, 2]"
    print "Expects-[4, 0, 0, 0]"
    print "Got-\t", mergeMethod([0, 0, 2, 2])
    print

    print "Test Case #2-"
    print "Input-\t[2, 0, 2, 4]"
    print "Expects-[4, 4, 0, 0]"
    print "Got-\t", mergeMethod([2, 0, 2, 4])
    print

    print "Test Case #3-"
    print "Input-\t[2, 2, 0, 0]"
    print "Expects-[4, 0, 0, 0]"
    print "Got-\t", mergeMethod([2, 2, 0, 0])
    print

    print "Test Case #4-"
    print "Input-\t[2, 2, 2, 2, 2]"
    print "Expects-[4, 4, 2, 0, 0]"
    print "Got-\t", mergeMethod([2, 2, 2, 2, 2])
    print

    print "Test Case #5-"
    print "Input-\t[8, 16, 16, 8]"
    print "Expects-[8, 32, 8, 0]"
    print "Got-\t", mergeMethod([8, 16, 16, 8])
    print

    print "Test Case #6-"
    print "Input-\t[2, 0, 2, 4, 0, 4, 8, 8]"
    print "Expects-[4, 8, 16, 0, 0, 0, 0, 0]"
    print "Got-\t", mergeMethod([2, 0, 2, 4, 0, 4, 8, 8])
    print

test(merge)
