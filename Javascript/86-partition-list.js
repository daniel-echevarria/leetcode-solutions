var partition = function (head, x) {
  if (!head || head.next === null) return head;
  const lessThan = [];
  const greaterOrEqual = [];
  let curr = head;
  while (curr) {
    if (curr.val < x) {
      const last = lessThan[lessThan.length - 1];
      if (last) last.next = curr;
      lessThan.push(curr);
    } else {
      const last = greaterOrEqual[greaterOrEqual.length - 1];
      if (last) last.next = curr;
      greaterOrEqual.push(curr);
    }
    curr = curr.next;
  }
  if (lessThan.length === 0 || greaterOrEqual.length === 0) return head;
  lessThan[lessThan.length - 1].next = greaterOrEqual[0];
  greaterOrEqual[greaterOrEqual.length - 1].next = null;
  return lessThan[0];
};

[1, 4, 3, 2, 5, 2];

// Traverse the list and push the nodes to lessThan
// or to greaterOrEqual
// as you do it point the last node of the array to the coming node
// after that point the last of node of lessThan to the first node of greaterOrEqual
// point the last node of gOE to null
// return head
