var hasCycle = function (head) {
  if (head === null) return false;
  let slow = head;
  let fast = head;
  while (true) {
    if (fast.next === null || fast.next.next === null) return false;
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) return true;
  }
};

// Algo
// Declare a variable slow with initial value of head
// Declare a variable fast with initial value of fast
// launch a loop that never stops
// slow gets slow.next
// fast gets fast.next.next
// if slow and fast are the same return true
// if fast.next is null return false
