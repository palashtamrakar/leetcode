## Approach

Instead of finding the lowest common ancestor directly, I'll use the `findparent()` function to move up the tree one node at a time.

First, I collect `p` and all its ancestors in a set. Then I start from `q` and keep moving to its parent. The first node I find in the set must be the lowest common ancestor, because I'm checking `q`'s ancestors from the bottom up.

## Steps

1. Start at `p` and add it to a set.
2. Use `findparent()` to move to its parent, and keep adding each ancestor until there are no more parents.
3. Start at `q`.
4. Check whether the current node is in the set. If it is, return it.
5. Otherwise, move to its parent and repeat the check.
6. If no common ancestor is found, return `None`.

## Example

For `p = 2` and `q = 4`, the relevant part of the tree is:

```text
        5
       / \\
      3   8
     / \\ / \\
    1  4 7  9
     \\
      2
```

Starting from node `2`, the ancestors are `2`, `1`, `3`, and `5`.

Then I move up from node `4`:
- `4` isn't in the set.
- Its parent, `3`, is in the set.

So the lowest common ancestor is node `3`.

## Complexity

Let `n` be the number of nodes and `h` be the height of the tree.

- **Time:** `O(nh)`, because finding each parent may require searching the tree. In the worst case, this can become `O(n²)`.
- **Space:** `O(h)` for the set of ancestors, plus the recursive call stack used by `findparent()`.

## Notes

- Add each node itself to the ancestor set, not just its parent. A node can be an ancestor of itself.
- Store `TreeNode` objects in the set rather than their values.
- Make sure both functions are indented inside the `Solution` class.
"""
