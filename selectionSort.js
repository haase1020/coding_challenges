// write a function that takes in an array of ints and returns a sorted version of that array.
// use the selection sort algorithm to sort the array

// time complexity 0(n^2) where n is length of input array/ space is 0(1)

function selectionSort(array) {
  let currentIdx = 0;
  while (currentIdx < array.length - 1) {
    let smallestIdx = currentIdx;
    for (i = currentIdx + 1; i < array.length; i++) {
      if (array[smallestIdx] > array[i]) {
        smallestIdx = i;
        swap(currentIdx, smallestIdx, array);
        currentIdx++;
      }
    }
  }
  return array;
}

function swap(i, j, array) {
  temp = array[i];
  array[i] = array[j];
  array[j] = temp;
}
