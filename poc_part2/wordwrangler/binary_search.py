# Binary Search


def  binary_search(given_list, item):

      if len(given_list) == 1:
            return item == given_list[0]

      mid = len(given_list)/2

      if item < given_list[mid]:
            return binary_search(given_list[:mid], item)
      else:
            return binary_search(given_list[mid:], item)


sorted_list = [5, 6, 12, 17, 30, 64, 64, 67, 75, 79, 88, 91, 101, 106, 134, 135, 158, 168, 178, 199, 200, 202, 212, 230, 231, 234, 244, 253, 273, 291, 326, 327, 344, 345, 348, 361, 378, 385, 394, 400, 406, 416, 419, 439, 443, 450, 455, 477, 482, 491, 499, 511, 512, 516, 522, 542, 544, 583, 586, 590, 592, 598, 612, 624, 634, 634, 658, 667, 672, 689, 724, 737, 750, 765, 793, 803, 812, 814, 835, 836, 838, 849, 851, 861, 862, 867, 875, 876, 882, 894, 904, 906, 908, 942, 960, 965, 984, 986, 990, 993]

print "Searched for 135", "Computed:", binary_search(sorted_list, 135), "Expected: True"
print "Searched for 125", "Comptued:", binary_search(sorted_list, 125), "Expected: False"
