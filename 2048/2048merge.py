"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """

    # creates a copy of the line

    row = list(line)
    result = [0] * len(line)

    # result line
    destIndex = 0

    # flag to make sure that we merge a tile only once
    canMerge = True

    # iterate over the given row and
    # if found non_zero value,
    # either merge it with the previous
    # value in the result or put it as it is
    #
    for sourceIndex in range(len(row)):

        if row[sourceIndex]:

            # if non_zero value found
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


    return result



print "[2, 0, 2, 4] should return [4, 4, 0, 0], returns - ", merge([2, 0, 2, 4])
print "[0, 0, 2, 2] should return [4, 0, 0, 0], returns - ", merge([0, 0, 2, 2])
print "[2, 2, 0, 0] should return [4, 0, 0, 0], returns - ", merge([2, 2, 0, 0])
print "[2, 2, 2, 2, 2] should return [4, 4, 2, 0, 0], returns - ", merge([2, 2, 2, 2, 2])
print "[8, 16, 16, 8] should return [8, 32, 8, 0], returns - ", merge([8, 16, 16, 8])
print "[2, 0, 2, 4, 0, 4, 8, 8] should return [4, 8, 16, 0, 0, 0, 0, 0] returns - ", merge([2, 0, 2, 4, 0, 4, 8, 8])
