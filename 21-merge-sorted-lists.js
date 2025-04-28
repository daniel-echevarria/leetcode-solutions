var mergeTwoLists = function (list1, list2) {
  if (list1 === null) return list2;
  if (list2 === null) return list1;
  const head = new ListNode();
  let current = head;

  while (list1 && list2) {
    if (list1.val <= list2.val) {
      current.next = list1;
      list1 = list1.next;
    } else {
      current.next = list2;
      list2 = list2.next;
    }
    current = current.next;
  }

  current.next = list1 || list2;

  return head.next;
};

// Algo
// if list1 is empty return list 2
// if list2 is empty return list 1
// declare a variable mainHead with an empty list
// launch a loop
// if the currentValue of list1 is null
// main next gets list2 and returns
// if the currentValue of list2 is null
// main next gets list 1 and returns
// compare the currentValues of list1 and list2
// mainHead value gets the smallest
// that list gets the next

console.log(mergeTwoLists([1, 2, 4], [1, 2, 4]));
