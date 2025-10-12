search_names=[
    "Olivia", "Liam", "Emma", "Noah", "Ava", "Oliver", "Sophia", "Elijah", "Isabella", "Lucas",
    "Mia", "Mason", "Charlotte", "Logan", "Amelia", "James", "Harper", "Benjamin", "Evelyn", "Jacob",
    "Abigail", "Carter", "Ella", "Michael", "Elizabeth", "Henry", "Camila", "Alexander", "Luna", "Sebastian",
    "Sofia", "Jack", "Avery", "Samuel", "Mila", "David", "Aria", "Matthew", "Scarlett", "Joseph",
    "Penelope", "Levi", "Layla", "Mateo", "Chloe", "John", "Victoria", "Wyatt", "Madison", "Dylan",
    "Eleanor", "Grayson", "Grace", "Luke", "Nora", "Asher", "Riley", "Gabriel", "Zoey", "Julian",   
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores" ]

def sorted_names():
    """ Return a sorted list of names """
    return sorted(search_names)

def binary_search(arr, target):
    """ Binary Search algorithm
    O(log n) time complexity
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1   

target_name = "Chloe"
result = binary_search(search_names, target_name)
if result:
    print(f"Found {target_name} at index {result}")
else:
    print(f"{target_name} not found in the list")


