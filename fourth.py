import sys


boring_list = [x for x in range(1000000000)]
sys.getsizeof(boring_list)
cool_iterator = (x for x in range(1000000000))
sys.getsizeof(cool_iterator)

