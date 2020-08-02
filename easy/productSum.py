# write a function that takes in a "special" array and returns it's product sum.
# a special array is a non-empty array that contains either ints or other special arrays.
# The product sum of a special array is the sum of its elements where special arrays
# inside it are summed themselves and then multipled by their level of depth.
# depth of a special array is how far nested it is. [[[]]] is 3.
# therefore the prodcut sum of [x,y] is x+y; the product sum of [x,[y,z]] is x+2*(y+z);
# the product sum of [x,[y,[z]]] is x+2*(y+3z).
# this is a classic recursive problem

# time complexity is 0(N) where n is all elements in array and elements in subarrays, space is 0(D) where D is depth of array
def productSum(array, multiplier=1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplier + 1)
        else:
            sum += element
    return sum * multiplier


print(productSum([1, 2, [3], 4, 5]))
