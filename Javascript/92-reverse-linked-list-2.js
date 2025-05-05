// const reverseBetween = (head, left, right) => {
//   let position = 1;
//   const dummy = head;
//   let preReverse = null;
//   let previousNode = null;
//   while (position < left) {
//     previousNode = head;
//     head = head.next;
//     position++;
//   }
//   preReverse = previousNode;
//   const leftNode = head;
//   let newHead = leftNode;
//   while (position < right) {
//     newHead = previousNode = head;
//     head = head.next;
//     previousNode.next = newHead;
//     position++;
//   }
//   console.log(dummy);
//   const postReverse = head.next;
//   if (preReverse) preReverse.next = newHead;
//   leftNode.next = postReverse;
//   return dummy;
// };

// Algo given a linked list and a left and right position
// declare a variable position with initial value of 1
// declare a variable dummy that gets head
// traverse the list until the position equals left
// declare a variable preReverse that stores the node at the position just before the reverse
// declare a variable leftNode that gets the node at position left
// declare a variable newHead that gets the node at position left
// keep traversing the list until position equals right
// each turn point the previous node to the new head
// newHead gets the previous node
// store a temporary postReverse that gets the node after right
// point preReverse to the newHead
// point leftNode to the temporary postReverse
// return the dummy head

// Algo subOptimal

const reverseBetween = (head, left, right) => {
  const nodes = [];
  while (head) {
    nodes.push(head);
    head = head.next;
  }
  const sub = nodes.slice(left - 1, right);
  const rev = sub.reverse();

  nodes.splice(left - 1, rev.length, ...rev);
  for (let i = 0; i < nodes.length; i++) {
    nodes[i].next = nodes[i + 1] || null;
  }
  return nodes[0];
};

// Declare a variable nodesArray
// Traverse the linkedList and push all the nodes
// slice the array from left to right
// reverse the subArray and splice it in again
// iterate through the list and make each node point to the next
