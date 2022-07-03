import sys


# sys.getsizeof returns the size of the object in bytes


# Regular iterator with a normal list
even_numbers = [x for x in range(10000000) if x % 2 == 0]
sys.getsizeof(even_numbers)

# Using a generator
even_numbers = (x for x in range(10000000) if x % 2 == 0)
sys.getsizeof(even_numbers)
