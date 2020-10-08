/*
✅ singly linked lists
✅ doubly linked lists
✅ following is for singly linked lists: chains of list nodes that points finally to null (head and tail)
✅ not all linked lists have tails, but all have a HEAD
*/
/*
🔎 Given a linked list, return it in reverse.
    ✅ what do we reutrn if we get null or a single node? Just return null and the node back respectively
    ✅ test cases: 1 -> 2 -> 3 -> 4 -> 5 -> null  | 3 | null
    ✅ we don't know the whole length of a linked list/ so need iteration
*/
/* 
🙋 solution without code:
 1 -> 2 -> 3 -> 4 -> 5 -> null returns:
 5 -> 4 -> 3 -> 2 -> 1 -> null
 cn = 1 -> 2 we want cn = 1 -> null then build left (2,3,etc) we need next = 2 and prev = 1 -> null
*/
