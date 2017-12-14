# Data Structures

A collection of data structures assignments as part of the CodeFellows Python 401 course
[CodeFellows.com](https://codefellows.com "Codefellows Homepage")

## Data Structure 1: Linked List
Authors: Darren Haynes & [Kevin Robinson](https://github.com/Zan4567 "Kevin Robinson Github Profile Page")

## Data Structure 2: Stack
Authors: Darren Haynes & [Kevin Robinson](https://github.com/Zan4567 "Kevin Robinson Github Profile Page")

### Big O Notation
| Method | Big 0 | Description |
|:---:|:---:| --- |
| __push()__ | `0(1)` | You simply insert something into the head of the stack and now point to the previous head. |
| __pop()__ | `0(1)` | You simply remove the current head and shift the pointer to the new head that replaces it. |
| __\_\_len()\_\___ | `0(1)` | Since the size of the stack is calculated with each `push` and `pop` of the list (incremented and decremented) the size is stored in a variable. |

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