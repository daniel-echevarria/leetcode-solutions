const reverseBetween = (head, left, right) => {
  if (left === right) return head;
  if (right === 2) {
    let tempRight = head.next;
    head.next = tempRight.next;
    tempRight.next = head;
    return tempRight;
  }
  let leftPre;
  let leftNode;
  let previousNode = null;
  let currentNode = head;
  let count = 1;
  const dummy = head;
  while (currentNode) {
    if (left === count) {
      leftNode = currentNode;
      leftPre = previousNode;
    }
    if (right === count) {
      if (leftPre) leftPre.next = currentNode;
      const tempPostR = currentNode.next;
      if (right - left === 1) {
        currentNode.next = leftNode;
        leftNode.next = tempPostR;
      } else {
        currentNode.next = leftNode.next;
        previousNode.next = leftNode;
        leftNode.next = tempPostR;
        if (!leftPre) return currentNode;
      }
    }
    previousNode = currentNode;
    currentNode = currentNode.next;
    count++;
  }
  return dummy;
};
