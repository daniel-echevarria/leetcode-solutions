// var sortList2 = function (head) {
//   const values = [];
//   const dummy = new ListNode(0, head);
//   while (head) {
//     values.push(head.val);
//     head = head.next;
//   }
//   const sortedValues = values.sort((a, b) => a - b);
//   head = dummy.next;
//   let idx = 0;
//   while (head) {
//     head.val = values[idx];
//     head = head.next;
//     idx++;
//   }
//   return dummy.next;
// };

// Traverse the list and push the values to an array
// sort the array
// traverse the list again while updating the values with the values from the array

const sortList = (head) => {
  const dummy = new ListNode("#", head);
  const sort = (node) => {
    if (!node || !node.next) return;
    if (node.val < node.next.val) return;
    [node.val, node.next.val] = [node.next.val, node.val];
    sort(node.next);
  };
  while (head) {
    sort(head);
    head = head.next;
  }
  return dummy.next;
};

// Traverse the tree while keeping track of the previous node
// If the previous node value was bigger than the current one
// swap the values
