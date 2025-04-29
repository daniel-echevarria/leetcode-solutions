/**
 * // Definition for a _Node.
 * function _Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

var copyRandomList = function (head) {
  if (!head) return;
  const dummy1 = head;
  const dummy2 = new Node(null, null, null);
  let current1 = dummy1;
  let current2 = dummy2;
  const originalNodes = [];
  const newNodes = [];
  while (current1) {
    originalNodes.push(current1);
    newNodes.push(current2);
    current2.val = current1.val;
    if (current1.next) current2.next = new Node(null, null, null);
    current1 = current1.next;
    current2 = current2.next;
  }
  current1 = dummy1;
  current2 = dummy2;
  while (current1) {
    const randomIndex = originalNodes.indexOf(current1.random);
    current2.random = newNodes[randomIndex];
    current1 = current1.next;
    current2 = current2.next;
  }
  return dummy2;
};

// Algo copyRandomList
// Given the head of a list
// Declare a variable dummy1 that gets head
// Declare a variable dummy2 that gets a new Node

// First just copy the list without the random
// Declare a variable currentList1 that gets list1Head
// Declare a variable currentList2 that gets newHead
// Launch a loop until currentList1 is null
// currentList2 val gets currentList1Val
// currenList1 gets currentList1.next
// currentLIst2.next gets new Node
// currentlist2 gets currentList2.next
