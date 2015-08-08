def number_of_threes(num):

    if num == 0:
        return 0

    digit = num % 10

    if digit == 3:
        return 1 + number_of_threes(num/10)
    else:
        return number_of_threes(num/10)

#print number_of_threes(31111122)

def is_member(my_list, elem):

    if my_list == []:
        return False

    else:
        if elem == my_list[0]:
            return True
        return is_member(my_list[1:], elem)

#print is_member(['c', '.', 'd', 't'], '.')

def remove_x(my_string):

    if my_string == '':
        return ''
    else:
        if my_string[0] == 'x':
            return remove_x(my_string[1:])
        else:
            return my_string[0] + remove_x(my_string[1:])

def remove_x2(my_string):
    if my_string == '':
        return ''
    else:
        first_char = my_string[0]
        rest = remove_x2(my_string[1:])

        if first_char == 'x':
            return rest
        else:
            return first_char  + rest

#print remove_x("adfasxadasfx")

def insert_x(my_string):
    if len(my_string) < 2:
        return my_string
    else:
        return my_string[0] + 'x' + insert_x(my_string[1:])

#print insert_x("catdog")

def list_reverse(my_list):
    if my_list == []:
        return []
    else:
        return list_reverse(my_list[1:]) + [my_list[0]]

#print list_reverse([1, 2, 3, 4, ])

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

#print gcd(24, 18)

def slice(my_list, first, last):
    if len(my_list) == last-first:
        return my_list
    else:
        if len(my_list) > last:
            new_list = []
            for count in range(len(my_list) - 1):
                new_list.append(my_list[count])
            return slice(new_list, first, last)
        else:
            if len(my_list) > last-first:
                new_list = []
                for count in range(1, len(my_list)):
                    new_list.append(my_list[count])

                return slice(my_list[1:], first, last)


def test_slice():
    """
    Some test cases for slice
    """
    print "Computed:", slice([], 0, 0), "Expected: []"
    print "Computed:", slice([1], 0, 0), "Expected: []"
    print "Computed:", slice([1], 0, 1), "Expected: [1]"
    print "Computed:", slice([1, 2, 3], 0, 3), "Expected: [1, 2, 3]"
    print "Computed:", slice([1, 2, 3], 1, 2), "Expected: [2]"

test_slice()
