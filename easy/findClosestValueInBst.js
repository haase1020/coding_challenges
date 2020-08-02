// find the closest value in binary search tree
// avg time = 0(log(n)) | worst case = 0(n), which is tree with 1 branch
// space complexity: if recursively, avg. and worst are same as time. Iteratively: 0(1) both avg and worst case

// recursive method:
function findClosestValueInBst(tree, target) {
  return findClosestValueInBstHelper(tree, target, tree.value);
}

function findClosestValueInBstHelper(tree, target, closest) {
  if (tree === null) return closest;
  if (Math.abs(target - closest) > Math.abs(target - tree.value)) {
    closest = tree.value;
  }
  if (target < tree.value) {
    return findClosestValueInBstHelper(tree.left, target, closest);
  } else if (target > tree.value) {
    return findClosestValueInBstHelper(tree.right, target, closest);
  } else {
    return closest;
  }
}

// iterative method:
function findClosestValueInBst(tree, target) {
  return findClosestValueInBstHelper(tree, target, tree.value);
}

function findClosestValueInBstHelper(tree, target, closest) {
  let currentNode = tree;
  while (currentNode !== null) {
    if (Math.abs(target - closest) > Math.abs(target - currentNode.value)) {
      closest = currentNode.value;
    }
    if (target < currentNode.value) {
      currentNode = currentNode.left;
    } else if (target > tree.value) {
      currentNode = currentNode.right;
    } else {
      break;
    }
  }
  return closest;
}

// this is the class of the input tree:
class BST {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}
