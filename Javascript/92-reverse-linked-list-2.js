var reverseBetween = function (head, left, right) {
  const leftIndex = left - 1;
  const rightIndex = right - 1;
  const nodesArray = [];
  while (head) {
    nodesArray.push(head);
    head = head.next;
  }
  if (nodesArray.length < 2) return head;
  console.log(nodesArray);
  // Swap the nodes in the array
  const tempLeftNode = nodesArray[leftIndex];
  nodesArray[leftIndex] = nodesArray[rightIndex];
  nodesArray[rightIndex] = tempLeftNode;

  if (!leftIndex === 0) nodesArray[leftIndex - 1].next = nodesArray[leftIndex];
  nodesArray[leftIndex].next = nodesArray[leftIndex + 1];
  nodesArray[rightIndex - 1].next = nodesArray[rightIndex];
  nodesArray[rightIndex].next = nodesArray[rightIndex + 1] || null;
  return nodesArray[0];
};

// Algo
// given the head of a linked list and two integers left and right
// Declare a variable leftIndex that gets left - 1
// Declare a variable rightIndex that gets right - 1
// traverse the linked list and store the nodes inside a nodesArray
// swap the two nodes in the array
// adjust the next for the 4 nodes, the two before and the two swapped
