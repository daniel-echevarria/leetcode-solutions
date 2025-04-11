var isIsomorphic = function (s, t) {
  const hashS = {};
  const hashT = {};
  let freshS = "";
  let freshT = "";
  for (let i = 0; i < s.length; i++) {
    const keyS = s[i];
    const valS = t[i];
    const keyT = t[i];
    const valT = s[i];
    hashS[keyS] = valS;
    hashT[keyT] = valT;
  }
  for (let i = 0; i < s.length; i++) {
    const keyS = s[i];
    const keyT = t[i];
    freshS += hashS[keyS];
    freshT += hashT[keyT];
  }
  return freshS === t && freshT === s;
};

// Given two strings s and t
// iterate through s
// create a hash map with a key of s[i] and a value of t[i]
// after iteration use hashMap to recreate the string
// check if the strings match

console.log(isIsomorphic("egg", "add"));
console.log(isIsomorphic("foo", "bar"));
console.log(isIsomorphic("badc", "baba"));
