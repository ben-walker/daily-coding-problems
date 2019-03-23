/* Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass? */

/* Implementation */
const addToK = (list, k) => {
  const tracker = [];
  let check = false;

  list.forEach((i) => { // we only iterate over the array once, i.e. "one pass"
    // by subtracting the current value from the target value, the result
    // is the value which would combine with the current value to get the target.
    // in other words, k - i = j (thus i + j = k); we then store j; if we later find j,
    // the condition (do two numbers add to k?) is true
    if (tracker.includes(i)) check = true;
    tracker.push(k - i);
  });

  return check;
};

/* Testing */
console.assert(addToK([10, 15, 3, 7], 17));
console.assert(!addToK([], 17));
console.assert(!addToK([17], 17));
console.assert(addToK([17, 0], 17));
console.assert(addToK([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 17));
console.assert(addToK([0, 0], 0));
console.assert(addToK([15, 2, 3, 0, -1, 2, 3, -5], -6));
