var sortList = function (head) {
  const values = [];
  const dummy = new ListNode(0, head);
  while (head) {
    values.push(head.val);
    head = head.next;
  }
  const sortedValues = values.sort((a, b) => a - b);
  head = dummy.next;
  let idx = 0;
  while (head) {
    head.val = values[idx];
    head = head.next;
    idx++;
  }
  return dummy.next;
};

// Traverse the list and push the values to an array
// sort the array
// traverse the list again while updating the values with the values from the array
