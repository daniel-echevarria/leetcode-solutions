var deleteDuplicates = function (head) {
  const met = [];
  const dup = [];
  const dummy = new ListNode(0, head);
  while (head) {
    met.includes(head.val) ? dup.push(head.val) : met.push(head.val);
    head = head.next;
  }
  let newHead = dummy;
  while (newHead.next) {
    if (dup.includes(newHead.next.val)) {
      newHead.next = newHead.next.next;
      continue;
    }
    newHead = newHead.next;
  }
  return dummy.next;
};

// Algo
// declare an array met
// declare an array duplicates
// create a dummyHead that points to head
// Traverse the list
// for each value check if the value exists in met
// if it does push it to duplicates
// otherwise push it to met
// after traversing the list once
// traverse the list by checking if the next value is in duplicates
// if it is nextValue gets next next  and keep going until next is null
