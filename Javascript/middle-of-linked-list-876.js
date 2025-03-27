var middleNode = function (head) {
  const recurMiddleNode = (currentNode = head, currentMiddle = head) => {
    if (currentNode.next === null) return currentMiddle;
    currentMiddle = currentMiddle.next;
    if (currentNode.next.next === null) return currentMiddle;
    currentNode = currentNode.next.next;
    return recurMiddleNode(currentNode, currentMiddle);
  };
  return recurMiddleNode();
};

// Given a node of a linked list
// Declare a variable currentMiddle that gets the node value
// Declare a variable currentNode that gets the node value
// check if the currentNode next node is null
// if it is return the currentMiddle
// otherwise the currentMiddle gets the currentMiddle next Node
// check if the currentNode next next node is null
// if it is return the currentMiddle
// otherwise currentNode gets the next next Node
// call middleNode with the current values
