var findCenter = function (edges) {
  return edges[0].find((node) => edges[1].includes(node));
};

// Compare the two first edges and return the common node
