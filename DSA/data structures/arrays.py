new_list = [1, 2, 3, 4, 5]
results = new_list[1:4] # slicing the list from index 1 to 3
print(results) # Output: [2, 3, 4]

new_list.append(6) # adding an element to the end of the list
print(new_list) # Output: [1, 2, 3, 4, 5, 6]    
new_list.remove(2) # removing an element from the list
print(new_list) # Output: [1, 3, 4, 5, 6]
new_list.sort() # sorting the list
print(new_list) # Output: [1, 3, 4, 5, 6]

extended_list = [7, 8, 9]
new_list.extend(extended_list) # extending the list with another list
print(new_list) # Output: [1, 3, 4, 5, 6, 7, 8, 9]

if 3 in new_list:
    print("3 is present in the list")
else:
    print("3 is not present in the list")

for index, value in enumerate(new_list):
    print(f"Index: {index}, Value: {value}")
    break

for i in new_list:
    print(i)
    if i == 3:
        print("Found 3!")

        break

# Arrays are a fundamental data structure in computer science and programming.
# They are used to store a collection of elements, typically of the same data type, in a
# contiguous block of memory. Arrays provide a way to organize and access data efficiently,
# allowing for fast retrieval and manipulation of elements based on their index positions.
# Common operations on arrays include accessing elements by index, iterating through the array,
# adding or removing elements, and sorting the array. Arrays are widely used in various applications,
# including databases, graphics, and scientific computing, due to their simplicity and efficiency.

# In Python, arrays can be implemented using lists, which are dynamic arrays that can grow or shrink in size as needed.
# Lists in Python are versatile and can hold elements of different data types, making them a powerful
# and flexible data structure for various programming tasks.    

# Example usage:
my_array = [10, 20, 30, 40, 50]
print(my_array[2])  # Output: 30
my_array.append(60)  # Adding an element to the end of the array
print(my_array)  # Output: [10, 20, 30, 40, 50, 60]
my_array.remove(20)  # Removing an element from the array
print(my_array)  # Output: [10, 30, 40, 50, 60]
my_array.sort()  # Sorting the array
print(my_array)  # Output: [10, 30, 40, 50, 60]


# When resizing an array, the following steps are typically involved:
# 1. Allocate a new array with the desired size.
# 2. Copy the elements from the old array to the new array.
# 3. Update the reference to point to the new array.
# 4. Deallocate the old array if necessary (in languages with manual memory management).
# 5. Update any metadata (like size and capacity) associated with the array.    

# resizing is triggered  when 0, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576
# new_list = [1, 2, 3, 4, 5]
for i in range(20):
    new_list.append(i)
    print(f"Length: {len(new_list)}, Capacity: {len(new_list)}")
    print(new_list)
# Output: [2, 3, 4]
