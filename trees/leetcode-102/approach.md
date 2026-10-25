
# Binary Tree Level Order Traversal## Approach

I used recursion to visit each node and kept track of which level it belongs to.

The helper function takes two arguments: the current node and its level. The root starts at level `0`, and each time I move to a child, I increase the level by `1`.

I store the values in `outarr`. If I reach a level that doesn't have a list yet, I create one. Then I add the current node's value to the list for that level.

I recursively visit the left child first, then the right child. This means values at the same level are added from left to right.

## Steps

1. Create an empty result list called `outarr`.
2. Start the helper function at the root with level `0`.
3. If the current node is `None`, return.
4. If the current level doesn't have a sublist in `outarr`, add an empty list.
5. Append the node's value to `outarr[level]`.
6. Recursively visit the left and right children at `level + 1`.
7. Return `outarr`.

## Example

For the tree represented by `[3, 9, 20, None, None, 15, 7]`, the traversal groups nodes like this:

- Level 0: `[3]`
- Level 1: `[9, 20]`
- Level 2: `[15, 7]`

The result is:

```python
[[3], [9, 20], [15, 7]]
```

## Complexity

Let `n` be the number of nodes and `h` be the height of the tree.

- **Time:** `O(n)` because every node is visited once.
- **Auxiliary space:** `O(h)` for the recursion stack.
- **Total space:** `O(n)` when the output list is included, since it stores every node's value.

For a balanced tree, the recursion stack is `O(log n)`. For a skewed tree, it can grow to `O(n)`.

