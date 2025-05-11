/**
 * @param {number} capacity
 */
const Node = (val, next = null, prev = null) => {
  return { val, next, prev };
};

var LRUCache = function (capacity) {
  this.capacity = capacity;
  this.map = new Map();
  this.head = Node("H");
  this.tail = Node("T");
  this.head.next = this.tail;
  this.tail.prev = this.head;
};

/**
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function (key) {
  if (!this.map.has(key)) return -1;

  const oldNode = this.map.get(key);
  oldNode.prev.next = oldNode.next;
  oldNode.next.prev = oldNode.prev;

  const newNode = Node([key, oldNode.val[1]], this.tail, this.tail.prev);
  this.tail.prev.next = newNode;
  this.tail.prev = newNode;
  this.map.set(key, newNode);

  const result = newNode.val[1];
  return result;
};

/**
 * @param {number} key
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function (key, value) {
  if (this.map.has(key)) {
    const oldNode = this.map.get(key);
    oldNode.prev.next = oldNode.next;
    oldNode.next.prev = oldNode.prev;
  }
  const newNode = Node([key, value], this.tail, this.tail.prev);
  this.tail.prev.next = newNode;
  this.tail.prev = newNode;
  this.map.set(key, newNode);
  if (this.map.size > this.capacity) {
    const keyToDelete = this.head.next.val[0];
    this.map.delete(keyToDelete);
    this.head.next = this.head.next.next;
    this.head.next.prev = this.head;
  }
};
