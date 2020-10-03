function diagonalSum(size) {
  let sum = 1;
  let diagonal;
  while (size > 1) {
    diagonal = 4;
    while (diagonal--) {
      sum += size * size - (size - 1) * diagonal;
    }
    size -= 2;
  }
  return sum;
}

console.log(diagonalSum(1001));
