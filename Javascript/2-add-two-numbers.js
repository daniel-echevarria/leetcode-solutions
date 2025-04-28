function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

const createLinkedList = (list) => {
  let next = null;
  while (list.length > 0) {
    const currentNode = new ListNode(list.pop(), next);
    next = currentNode;
  }
  return next;
};

var addTwoNumbers = function (l1, l2) {
  let leftIntArray = [];
  let rightIntArray = [];
  while (l1 != null) {
    leftIntArray.push(l1.val);
    l1 = l1.next;
  }
  while (l2 != null) {
    rightIntArray.push(l2.val);
    l2 = l2.next;
  }
  const leftInt = leftIntArray.reverse().join("");
  const rightInt = rightIntArray.reverse().join("");
  const sum = BigInt(leftInt) + BigInt(rightInt);
  const sumArray = sum.toString().split("").reverse();
  const sumDigits = sumArray.map((x) => +x);
  const result = createLinkedList(sumDigits);
  return result;
};

// Algo
// given 2 linked lists l1 and l2
// declare a variable leftIntArray with initial value of []
// declare a variable rightIntArray with initial value of []
// traverse l1 and push the values to leftIntArray
// traverse l2 and push the values to rightIntArray
// reverse the arrays
// join the arrays
// sum the values
// split the sum
// create  linkedList from the array

// Algo createLinkedList
// given an array of values
// declare a variable next with initial value of null
// loop until the array is empty
// pop the last value and create a node that points to next
// next get the new node

const left = createLinkedList([
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 1,
]);

const right = createLinkedList([5, 6, 4]);

console.log(addTwoNumbers(left, right));
