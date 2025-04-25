var simplifyPath = function (path) {
  const pathArray = path.split("/");
  const cleanPath = pathArray.filter((x) => x);
  const stack = [];
  for (const s of cleanPath) {
    if (s === "." || s === "") continue;
    if (s === "..") {
      stack.pop();
      continue;
    }
    stack.push(s);
  }
  const simplifiedPath = stack.join("/");
  return "/" + simplifiedPath;
};

// Algo
// given a string path
// split the string at each /
// clear the array from empty strings
// declare a variable stack with initial value of []
// iterate through the array
// if meeting a single do, pass
// if meeting a double dot pop the stack
// after iteration join the stack with /
// adjust first and last /

console.log(simplifyPath("/.../a/../b/c/../d/./"));
console.log(simplifyPath("/home//foo/"));
