
def is_sorted(arr):  # returns true if a list is sorted from greatest to least
    for num in range(len(arr)-1):
        if arr[num] < arr[num+1]:
            return False
    return True


def format_right(original_len, arr):  # this function formats the arrays last element to print in the same column
    length = len(arr)
    space_count = original_len - length
    for x in range(space_count):
        print("   ", end="")


def count_odds(arr):  # this function returns True if there is an even number of odd elements
    odd_count = 0
    for num in arr:
        if num % 2 != 0:
            odd_count += 1

    if odd_count % 2 != 0:
        return False
    return True


def check_zeros(arr):  # returns true if every element is a 0
    flag = False
    for num in arr:
        if num != 0:
            flag = True
    if flag:
        return False
    return True


def havel_hakimi(arr):

    arr.sort(reverse=True)  # sorts the given list from greatest to least
    if arr[0] > len(arr)-1:  # checks if the largest element is greater than one less the length of the list
        print("Not graphical, one or more elements are greater than one less the length of the list.")
        return
    if not count_odds(arr):  # checks if there are an odd number of even elements
        print("Not graphical, there is an odd number of odd elements.")
        return

    arr_len = len(arr)
    print(arr, " -> The original list sorted")
    while not check_zeros(arr):
        removed = arr.pop(0)
        for num in range(0, removed):
            arr[num] -= 1

            if arr[num] <= -1:  # checks if there are any numbers less than 0 in the list
                print("Not graphical, an element less than 0 cannot be a value in the list.")
                return

        format_right(arr_len, arr)
        print(arr, " -> %d Was removed. 1 was subtracted from the next %d elements." % (removed, removed))

        if not is_sorted(arr):  # sorts the list and prints if it was not sorted
            arr.sort(reverse=True)
            format_right(arr_len, arr)
            print(arr, " -> The list sorted")


list1 = [5, 5, 4, 4, 2, 2, 1, 1]
list2 = [5, 5, 7, 6, 4, 2, 4, 5]
list3 = [3, 5, 6, 4, 3, 3, 5, 1, 2, 4, 6, 11, 3, 4, 6, 7, 5, 5, 3, 2, 4, 6, 8, 2, 4, 6, 8]
list4 = [5, 5, 5, 3, 2, 2, 1, 1]

havel_hakimi(list4)
