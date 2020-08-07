def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    numbers_dict = {}
    num_of_arr = len(arrays)
    intersections = []
    for ray in arrays:
        for num in ray:
            if num not in numbers_dict:
                    numbers_dict[num] = 0

            numbers_dict[num] +=1
            if numbers_dict[num] == num_of_arr:
                intersections.append(num)
    
    return intersections


    # get the length of the array of arrays
    # loop over array or arrays,
    # loop over array
    # add each item to the dictionary
    # check length of array in dictionary if it equals length of
        # then that item is added to intersection array


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
# testarrays = [[2,4,7,5],[5,7,8],[7,9,5,1]]
# print(intersection(testarrays))