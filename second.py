

def the_for(object_to_iterate):
    iterable = iter(object_to_iterate)
    iterating = True
    while iterating:
        try:
            i = next(iterable)
            print(i)
        except StopIteration:
            iterating = False
