# Task 1: Accepts user input to create a list of integers and compute the sum
def create_integer_list():
    user_input = input("Enter integers separated by spaces: ")
    # Splitting the input into a list of strings and converting each to an integer
    integer_list = [int(x) for x in user_input.split()]
    print("The list of integers is:", integer_list)
    total_sum = sum(integer_list)
    print("The sum of all integers in the list is:", total_sum)

create_integer_list()



# Task 2: Create a tuple of five favorite books and print each book on a separate line
def print_favorite_books():
    books = ("The Alchemist", "1984", "To Kill a Mockingbird", "Pride and Prejudice", "Moby Dick")
    print("My favorite books are:")
    for book in books:
        print(book)

print_favorite_books()


# Task 3: Store user info (name, age, favorite color) in a dictionary and print it
def create_person_info():
    person = {}
    person['name'] = input("Enter your name: ")
    person['age'] = input("Enter your age: ")
    person['favorite_color'] = input("Enter your favorite color: ")
    
    print("Person Information:", person)

create_person_info()

# Task 4: Accept user input to create two sets and find common elements
def find_common_elements():
    set1 = set(map(int, input("Enter integers for the first set (separated by spaces): ").split()))
    set2 = set(map(int, input("Enter integers for the second set (separated by spaces): ").split()))
    
    common_elements = set1 & set2
    print("The common elements between both sets are:", common_elements)

find_common_elements()

# Task 5: Create a list of words, then use list comprehension to find words with odd number of characters
def filter_odd_length_words():
    words = input("Enter a list of words (separated by spaces): ").split()
    
    odd_words = [word for word in words if len(word) % 2 != 0]
    print("Words with an odd number of characters:", odd_words)

filter_odd_length_words()



