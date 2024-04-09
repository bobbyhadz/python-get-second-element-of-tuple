# Get the Nth element of a Tuple in Python

# ✅ Get the second element of a tuple

my_tuple = ('bobby', 'hadz', 'com')

second_item = my_tuple[1]
print(second_item)  # 👉️ hadz

# ---------------------------------------------

# ✅ Get the second element from a list of tuples

list_of_tuples = [('a', 'b'), ('c', 'd'), ('e', 'f')]

result = [tup[1] for tup in list_of_tuples]
print(result)  # 👉️ ['b', 'd', 'f']