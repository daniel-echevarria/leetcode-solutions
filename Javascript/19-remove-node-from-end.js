var removeNthFromEnd = function (head, n) {
  const dummy = new ListNode(0, head);
  const nodes = [dummy];
  while (head) {
    nodes.push(head);
    head = head.next;
  }
  if (nodes.length < 2) return head;
  const badNodeIndex = nodes.length - n;
  nodes[badNodeIndex - 1].next = nodes[badNodeIndex + 1] || null;
  return dummy.next;
};

// Algo
// Traverse the list, push all the nodes to a nodes array
// Create a dummyNode that points to head
// Declare a variable badNodeIndex that gets nodes.length - n
// select the node before badNode and make it point to the node just after
// return dummy.next
