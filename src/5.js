/* cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element
of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
  def pair(f):
    return f(a, b)
  return pair
Implement car and cdr. */

/* Implementation */
const PAIR_LEN = 2;

const cons = (a, b) => {
  const pair = f => f(a, b);
  return pair;
};

const car = pair => (pair.length !== PAIR_LEN ? null : pair[0]);
const cdr = pair => (pair.length !== PAIR_LEN ? null : pair[1]);

/* Testing */
console.assert(car(cons(3, 4)(Array)) === 3);
console.assert(cdr(cons(3, 4)(Array)) === 4);
