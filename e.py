"""
    compares the time needed to add elements to the front of a list and deque.
"""

# Needed imports
from collections import deque
from time import perf_counter
from typing import List, Deque, Callable, Any
import t as lq
import test as dllq

# Number of insertions to perform
NB_OPS = 10_000

# Initialize the various structures
queue_using_list = lq.initialize()
queue_using_dll = dllq.initialize()
queue_using_deque = deque()


def average_time (func: Callable[[Any], None], times: int) -> float:
    
    """
        This function computes the average time needed to execute a function.
        In:
            * func:  Function to execute.
            * times: Number of times to execute the function.
        Out:
            * Average time needed to execute the function.
    """ 

    # Run the function multiple times
    total = 0.0
    for i in range(times):
        start = perf_counter()
        func(i)
        total += (perf_counter() - start) * 1e9
    
    # Return the average time
    return total / times



# Compute the average time needed to insert an element in the list-based queue
list_time = average_time(lambda i: lq.push(queue_using_list, i), NB_OPS)

# Compute the average time needed to insert an element in the doubly linked list-based queue
dll_time = average_time(lambda i: dllq.insert_at_end(queue_using_dll, i), NB_OPS)

# Compute the average time needed to insert an element in the deque-based queue
deque_time = average_time(lambda i: queue_using_deque.appendleft(i), NB_OPS)

# Evaluate the gain
gain = list_time / deque_time
gain2 = list_time / dll_time
gain3 = dll_time / deque_time

# Print results
print("----\n INSERTION \n---")
print(f"Average time list queue:               {list_time:.6} ns")
print(f"Average time doubly-linked list queue: {dll_time:.6} ns")
print(f"Average time deque:                    {deque_time:.6} ns")
print(f"deque over list:               {gain:.6}x faster")
print(f"doubly-linked list over list:  {gain2:.6}x faster")
print(f"deque over doubly-linked list: {gain3:.6}x faster")

# Compute the average time needed to remove an element in the list-based queue
list_time = average_time(lambda i: lq.pop(queue_using_list), NB_OPS)

# Compute the average time needed to remove an element in the doubly linked list-based queue
dll_time = average_time(lambda i: dllq.pop_from_beginning(queue_using_dll), NB_OPS)

# Compute the average time needed to remove an element in the deque-based queue
deque_time = average_time(lambda i: queue_using_deque.pop(), NB_OPS)

# Evaluate the gain
gain = list_time / deque_time
gain2 = list_time / dll_time
gain3 = dll_time / deque_time

# Print results
print("----\n DELETION \n---")
print(f"Average time list queue:               {list_time:.6} ns")
print(f"Average time doubly-linked list queue: {dll_time:.6} ns")
print(f"Average time deque:                    {deque_time:.6} ns")
print(f"deque over list:               {gain:.6}x faster")
print(f"doubly-linked list over list:  {gain2:.6}x faster")
print(f"deque over doubly-linked list: {gain3:.6}x faster")