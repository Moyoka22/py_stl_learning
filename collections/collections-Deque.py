
# Lists as stacks and queues

# ! Stack 
stack = [1,2,3]
x = stack.pop() # ! O(1) for popping the last item
print(x) # 3 
print(stack) # [1,2]

stack.append(3) # ! Amortized O(1)
print(stack) # [1,2,3]

# ! Queue

queue = [1,2,3]
x = queue.pop(0) # ! O(n)
print(x) # 1
print(queue) # [2,3]

queue.append(4)
print(queue) # [2,3,4]

# http://effbot.org/pyfaq/what-kinds-of-global-value-mutation-are-thread-safe.htm
# Due to the GIL the list methods pop, append and popleft are threadsafe # ? Query popleft

from collections import deque 
# * Pronounced 'deck' meaning double-ended queue

deq = deque([1,2,3,4])
deq.append(5) # ! O(1)
deq.appendleft(0) # ! O(1)
print(deq) # deque([0, 1, 2, 3, 4, 5])
last = deq.pop() # ! O(1)
head = deq.popleft() # ! O(1)
print(head) # 0
print(last) # 5
print(deq) # deque[1, 2, 3, 4]

# Accessing the middle of a deque is O(n)


deq.rotate()
print(deq) # deque([4, 1, 2, 3])

# ? Why is deque lowercase? 
# * Because deque is a type not a class 

from itertools import count
limited_deque = deque([],5)
for i in range(10):
    limited_deque.append(i)

print(limited_deque) # deque([5, 6, 7, 8, 9], maxlen=5)