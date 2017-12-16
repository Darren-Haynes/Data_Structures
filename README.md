# Data Structures

A collection of data structures assignments as part of the CodeFellows Python 401 course
[CodeFellows.com](https://codefellows.com "Codefellows Homepage")

<br />

## Data Structure 1: Linked List
Authors: Darren Haynes & [Kevin Robinson](https://github.com/Zan4567 "Kevin Robinson Github Profile Page")

<br />

## Data Structure 2: Stack
Authors: Darren Haynes & [Kevin Robinson](https://github.com/Zan4567 "Kevin Robinson Github Profile Page")

### Big O Notation
| Method | Big 0 | Description |
|:---:|:---:| --- |
| __push()__ | `0(1)` | You simply insert something into the head of the stack and now point to the previous head. |
| __pop()__ | `0(1)` | You simply remove the current head and shift the pointer to the new head that replaces it. |
| __\_\_len()\_\___ | `0(1)` | Since the size of the stack is calculated with each `push` and `pop` of the list (incremented and decremented) the size is stored in a variable. |

<br />

## Data Structure 3: Doubly Link List
Authors: Darren Haynes & [Kevin Robinson](https://github.com/Zan4567 "Kevin Robinson Github Profile Page")

### Big O Notation
| Method | Big 0 | Description |
|:---:|:---:| --- |
| __push()__ | `0(1)` | Adding a node changes head to the this node and points new node to previous head node. All simple `0(1) operations|
| __append()__ | `0(1)` | Adding a node changes tail to the this node and points new node to previous tail node. All simple `0(1) operations|
| __shift()__ | `0(1)` | Removes tail and pointers to it. Restablish new tail. All simple `0(1) operations. |
| __pop()__ | `0(1)` | Removes head and pointers to it. Restablish new head. All simple `0(1) operations. |
| __remove()__ | `0(n)` | Worst case is `0(n)` since remove may need to travers the whole list if the item to remove is the last item in list, or not in the list at all. |
| __\_\_len()\_\___ | `0(1)` | Since the size of the stack is calculated with each `push`, `pop`, `shift`, `append`, `remove` of the list (incremented and decremented) the size is stored in a variable. |

<br />

## Data Structure 4: Queue
Authors: Darren Haynes & [Kevin Robinson](https://github.com/Zan4567 "Kevin Robinson Github Profile Page")

### Big O Notation
| Method | Big 0 | Description |
|:---:|:---:| --- |
| __enqueue()__ | `0(1)` | You simply insert something into the back of the queue and adjust pointers. |
| __dequeue()__ | `0(1)` | You simply remove the current front and adjust the pointers. |
| __peek()__ | `0(1)` | A simple operation, just check if a node is at the front and return it's value if there is one. |
| __\_\_len()\_\___ | `0(1)` | Since the size of the stack is calculated with each `push` and `pop` of the list (incremented and decremented) the size is stored in a variable. |

<br />
## Data Structure 5: Deque
Authors: Darren Haynes & [Kevin Robinson](https://github.com/Zan4567 "Kevin Robinson Github Profile Page")

### Big O Notation
| Method | Big 0 | Description |
|:---:|:---:| --- |
| __appendleft()__ | `0(1)` | You simply insert something into the start of the deque and adjust pointers. |
| __append()__ | `0(1)` | You simply insert something into the end of the deque and adjust pointers. |
| __peekleft()__ | `0(1)` | Just take a peek at the start node. |
| __peek()__ | `0(1)` | Just take a peek at the end node. |
| __pop()__ | `0(1)` | Removes end and pointers to it. All simple `0(1) operations. |
| __popleft()__ | `0(1)` | Removes start and pointers to it. All simple `0(1) operations. |
| __size()__ | `0(1)` | Size is incremented and decremented with each append and pop. So its just accessing a variable containing the size. |

<br />

## Data Structure 5: Priority Queue
Author: Darren Haynes

### Big O Notation
| Method | Big 0 | Description |
|:---:|:---:| --- |
| __insert()__ | `0(1)` | In this case, the priority queue uses the python dictionary as its datastructure. The insert method utilizes the dictionary `setter` which is an `0(1)` operation. |
| __pop()__ | `0(1)` | This utilizes the python dictionary `get` method which is an `0(1) operations. |
| __peek()__ | `0(1)` | This also utilizes the python dictionary `get` method along with the list `get` (by index) method. Both an `0(1) operations. |

