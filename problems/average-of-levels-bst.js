function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var averageOfLevels = function (root) {
  var result = [];
  var q = [];
  q.push(root);

  while (q.length) {
    var count = q.length;
    var sum = 0;

    for (let i = 0; i < count; i++) {
      var curr = q.shift();
      sum += curr.val;

      if (curr.left) q.push(curr.left);

      if (curr.right) q.push(curr.right);
    }
    result.push(sum / count);
  }
  return result;
};

const root = new TreeNode(
  3,
  new TreeNode(9, null, null),
  new TreeNode(20, new TreeNode(15, null, null), new TreeNode(7, null, null))
);

console.log(averageOfLevels(root));
