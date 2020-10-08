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
/*
NOTE: The beginning portion builds our test case linked list. Scroll down to the section titled Our Solution for the code solution!
 */

class ListNode {
  constructor(val, next = null) {
    this.val = val;
    this.next = next;
  }
}
// ---- Generate our linked list ----
const linkedList = [5, 4, 3, 2, 1].reduce(
  (acc, val) => new ListNode(val, acc),
  null
);

// ---- Generate our linked list ----

const printList = (head) => {
  if (!head) {
    return;
  }

  console.log(head.val);
  printList(head.next);
};

// --------- Our solution -----------

var reverseList = function (head) {
  let prev = null;
  let current = head;

  while (current) {
    let nextTemp = current.next;
    current.next = prev;
    prev = current;
    current = nextTemp;
  }

  return prev;
};

printList(linkedList);
console.log('********************after reverse************************');
printList(reverseList(linkedList));
