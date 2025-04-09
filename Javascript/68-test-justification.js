// Algo fullJustify
// declare result with an initial value of []
// declare a currentLine with an initial value of []
// declare a letterCount with an initial value of 0
// Iterate through the words
// if letterCount + the next word length is bigger than maxWidth
// push the joined line to result
// currentLine gets []
// letterCount gets 0
// push the current word to currentLine
// add the current word length to letterCount
// push a white space

const justifyLine = (line) => {
  let numWhiteSpaces = line.pop();
  const whiteSpaces = Array.from({ length: numWhiteSpaces }, () => " ");
  if (line.length < 3) {
    line.splice(1, 0, whiteSpaces);
    return line.flat().join("");
  }
  let wordIndex = 0;
  while (numWhiteSpaces > 0) {
    if (wordIndex === line.length - 1) {
      wordIndex = 0;
      continue;
    }
    line[wordIndex] = line[wordIndex] + " ";
    wordIndex++;
    numWhiteSpaces--;
  }
  return line.flat().join("");
};

const verses = (words, maxWidth) => {
  const n = words.length;
  let result = [];
  let currentLine = [];
  let letterCount = 0;
  let realLetterCount = 0;
  for (let i = 0; i < n; i++) {
    currentLine.push(words[i]);
    letterCount += words[i].length + 1;
    realLetterCount += words[i].length;
    if (i + 1 > n - 1) {
      currentLine.push(maxWidth - realLetterCount);
      result.push(currentLine);
      currentLine = [];
      letterCount = 0;
      realLetterCount = 0;
      return result;
    }
    if (letterCount + words[i + 1].length > maxWidth) {
      currentLine.push(maxWidth - realLetterCount);
      result.push(currentLine);
      currentLine = [];
      realLetterCount = 0;
      letterCount = 0;
    }
  }
};

var fullJustify = function (words, maxWidth) {
  const broken = verses(words, maxWidth);
  const solution = broken.map((x) => justifyLine(x));
  return solution;
};

// const justifyLine

// Algo to justifyLine
// Given a string and a width
// declare a variable result []
// pop the numWhiteSpaces from the line
// if there is only one word, or two words, add that many white spaces after the first word and return
// create a loop that adds a white space after each words
// unless the word is the last one of the array
// return the result

// const just = justifyLine(["understand", "well", 6]);
// console.log(just);

// const just2 = justifyLine(["justification.", 2]);
// console.log(just2);

// const just3 = justifyLine(["to", "a", "computer.", "Art", 5]);
// console.log(just3);

const res = fullJustify(
  ["This", "is", "an", "example", "of", "text", "justification."],
  16
);
console.log(res);

const res2 = fullJustify(
  ["What", "must", "be", "acknowledgment", "shall", "be"],
  16
);
console.log(res2);

const res3 = fullJustify(
  [
    "Science",
    "is",
    "what",
    "we",
    "understand",
    "well",
    "enough",
    "to",
    "explain",
    "to",
    "a",
    "computer.",
    "Art",
    "is",
    "everything",
    "else",
    "we",
    "do",
  ],
  20
);

console.log(res3);
