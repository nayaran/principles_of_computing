# Quick Sort


def quick_sort(given_list):

      # return if list is empty
      if given_list == []:
            return given_list

      # choose the pivot to be the first element
      pivot = given_list[0]

      # create a list of elements which are less than pivot
      less_than_pivot = [num for num in given_list if num < pivot]

      # create a list of elements which are equal pivot
      equal_to_pivot = [num for num in given_list if num == pivot]

      # create a list of elements which are greater than pivot
      greater_than_pivot = [num for num in given_list if num > pivot]

      return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)

print quick_sort([9, 8, 7, 6, 5, 4, 3, 2, 1])
