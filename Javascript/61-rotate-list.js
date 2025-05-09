var rotateRight = function (head, k) {
  if (!head || head.next === null) return head;
  const nodes = [];
  let dummyHead = head;
  while (dummyHead) {
    nodes.push(dummyHead);
    dummyHead = dummyHead.next;
  }
  const rotations = k % nodes.length;
  for (let i = 0; i < rotations; i++) {
    const last = nodes.pop();
    last.next = head;
    head = last;
  }
  nodes[nodes.length - 1].next = null;
  return head;
};

// Algo
// traverse the list while storing the nodes into an array nodes
// find the remainder of dividing k by the size of the list
// That gives us the number of 'meaningful' rotations
// store that number in a variable rotations
// for each rotation:
// pop the last node and make it point to head
// head gets the popped node
// after that process make the last node of the list point to null
// return head
