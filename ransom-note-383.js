var canConstruct = function (ransomNote, magazine) {
  const ransomLetters = ransomNote.split("");
  const magazineLetters = magazine.split("");

  for (i = 0; i < ransomLetters.length; i++) {
    const letter = ransomLetters[i];
    if (!magazineLetters.includes(letter)) return false;
    const letterIndex = magazineLetters.indexOf(letter);
    magazineLetters.splice(letterIndex, 1);
  }
  return true;
};

canConstruct("aa", "bb");

// Given 2 strings ransomNote and magazine
// split both strings into arrays of strings of 1 char called ransomLetters and magazineLetters
// iterate through the ransomLetters
// if the magazineLetters include the current ransomLetter remove that letter from the magazine and go to the next letter
// otherwise return false
// after going through all the letters return true
