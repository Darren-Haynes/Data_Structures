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