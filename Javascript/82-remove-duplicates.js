var deleteDuplicates2 = function (head) {
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

const deleteDuplicates = (head) => {
  const dummy = new ListNode(0, head);
  let currentValue = null;
  let prev = dummy;
  while (head) {
    if (head.val === currentValue) {
      prev.next = head.next;
      head = head.next;
      continue;
    }
    if (!head.next) {
      return dummy.next;
    }
    currentValue = head.val;
    if (head.next.val === currentValue) {
      prev.next = head.next.next;
      head = prev.next;
      continue;
    }
    prev = head;
    head = head.next;
  }
  return dummy.next;
};

[1, 1, 1];

[1, 2, 3, 3, 4, 4, 5];

[1, 1, 1, 2, 3];

// Algo one pass
// declare a dummy node that points to head
// declare a variable currentValue with initial value of null
// declare a variable prev with initial value of dummy
// traverse the list until head.next is null
// check if the value of head is the same as currentValue
// if it is prev points to the next value and start again
// if it's not currentValue gets the value of head
// check if the next value is the same as currentValue
// if it is prev next points to next next
// and start again
// if it is not
// prev gets head and head gets next
// and keep going
