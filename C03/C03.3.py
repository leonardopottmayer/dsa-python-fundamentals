# VERSION 1
# print("Welcome to bubble sort!")

# numbers = [1, 6, 3, 7, 9, 2, 4, 5, 8]

# # Order increasing
# for i in range(len(numbers)):
#     for j in range(len(numbers) - 1):
#         if numbers[j] > numbers[i]:
#             tempJ = numbers[j]
#             numbers[j] = numbers[i]
#             numbers[i] = tempJ

# print("Sorted numbers in increasing:", numbers)

# # Order decreasing
# for i in range(len(numbers)):
#     for j in range(len(numbers) - 1):
#         if numbers[i] > numbers[j]:
#             tempI = numbers[i]
#             numbers[i] = numbers[j]
#             numbers[j] = tempI

# print("Sorted numbers in decreasing:", numbers)

# VERSION 2
list = [6, 7, 8, 3, 10, 19, 4, 1, 0, 61, 30, 16, 17, 82, 29, 34, 43, 21, 11, 39, 56, 67, 12]

def bubble_sort(arr, increasing):
    n = len(arr)

    # For each element i in the array
    for i in range(n):

        # For each element j in the array
        for j in range(0, n-i-1):

            if increasing == True:
                # If the i element is greater than the j element
                if arr[j] > arr[j+1]:

                    # Swap the elements
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                if arr[j] < arr[j+1]:

                    # Swap the elements
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print (bubble_sort(list, True))
print (bubble_sort(list, False))