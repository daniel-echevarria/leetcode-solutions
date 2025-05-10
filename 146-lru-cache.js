/**
 * @param {number} capacity
 */
var LRUCache = function (capacity) {};

/**
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function (key) {};

/**
 * @param {number} key
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function (key, value) {};

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */

// /**
//  * @param {number} capacity
//  */

// const Node = (val, next = null) => {
//   return {
//     val,
//     next,
//   };
// };

// var LRUCache = function (capacity) {
//   this.capacity = capacity;
//   this.map = new Map();
//   this.head = null;
//   this.tail = null;
// };

// /**
//  * @param {number} key
//  * @return {number}
//  */
// LRUCache.prototype.get = function (key) {
//   const value = this.map.get(key);
//   if (value != undefined) {
//     const myNode = Node(key);
//     this.tail.next = myNode;
//     this.tail = myNode;
//     if (this.head) this.head = this.head.next;
//   }
//   const result = value === undefined ? -1 : value;
//   return result;
// };

// /**
//  * @param {number} key
//  * @param {number} value
//  * @return {void}
//  */
// LRUCache.prototype.put = function (key, value) {
//   const keyExists = this.map.has(key);
//   if (keyExists) {
//     this.map.set(key, value);
//   }
//   if (!this.map[key]) {
//     if (this.map.size >= this.capacity) {
//       const lru = this.head.val;
//       delete this.map[lru];
//       if (this.head) this.head = this.head.next;
//     }
//     const myNode = Node(key);
//     if (this.tail) this.tail.next = myNode;
//     if (this.count === 0) this.head = myNode;
//     this.tail = myNode;
//   }
//   this.map[key] = value;
// };

// [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]];

// /**
//  * Your LRUCache object will be instantiated and called as such:
//  * var obj = new LRUCache(capacity)
//  * var param_1 = obj.get(key)
//  * obj.put(key,value)
//  */

// // Algo
// // declare map that will store the key value pairs
// // declare a count that gets+1 for each put
// // declare a variable isAtCapacity that returns true if count is equal or bigger than capacity
// // declare a linkedList
// // always have the head and the tail at hand
// // get is easy just look for the value in the map
// // for put:
// // check if the map isAtCapacity
// // if it is get the value of the head of the list and delete that key
// // head gets head.next
// // tail.next gets a newNode with the value of key and next null
// // if not just update tail next to point ta newNode with this key and update tail for this node
