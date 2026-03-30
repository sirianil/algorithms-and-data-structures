# algorithms-and-data-structures
Algorithms and Data Structures

1. Tree:
DFS with recursion
DFS with a stack.
BFS with a queue.

Level order with DFS:
you pass the level and then have a list. you can have a function inside a function to store the level values.

Level order with BFS:
you take the length of the queue before you start a level.
and everyhting in that lenght will be that level.
BFS is more intutive to level order.

2. stack.
you initialize a list normally.
1. list.append() -> to append to the top
2. list.pop() -> you pop the latest element.

3. queue.
use a deque from collections.
from collections import deque
d.append() -> append normally
d.popleft() -> you get the first element.

you can do a normal list and do pop(0) but 
this would be very ineffecient - O(n) each time.


