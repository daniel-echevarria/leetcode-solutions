var fizzBuzz = function (n) {
  let result = [];

  const transform = (n) => {
    if (n % 15 === 0) return "FizzBuzz";
    if (n % 5 === 0) return "Buzz";
    if (n % 3 === 0) return "Fizz";
    return n.toString();
  };

  for (let i = 1; i <= n; i++) {
    result.push(transform(i));
  }
  return result;
};
