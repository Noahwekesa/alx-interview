#!/usr/bin/env python3
"""
module to deTERMINE if all boxes can be opened
"""


def canUnlockAll(boxes):
    """
    This function determines if all the boxes can be opened.

    Args:
        boxes: A list of lists, where each inner list represents the keys that can open the corresponding box.

    Returns:
        True if all boxes can be opened, False otherwise.
    """

    # Initialize a visited set to track opened boxes
    visited = set([0])  # Start with box 0 as initially unlocked

    # Loop through all boxes
    for i in range(len(boxes)):
        # Skip processing already visited boxes
        if i not in visited:
            continue

        # Check if all keys in the current box lead to opened boxes
        can_open_all = True
        for key in boxes[i]:
            # Check key validity
            if key not in visited and 0 <= key < len(boxes):
                can_open_all = False
                break
        visited.update(boxes[i])  # Add newly opened boxes to visited set

        # If any key couldn't open a box, return False
        if not can_open_all:
            return False

    # If all boxes are visited (opened), return True
    return True
