"""LeetCode-compatible node classes for local practice and tests."""

from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, val: int = 0, neighbors: list[Node] | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
