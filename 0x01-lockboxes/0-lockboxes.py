#!/usr/bin/python3
"""
module to deTERMINE if all boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Function to determine if all boxes can be opened
    """

    no_of_keys = [0]
    no_of_boxes = len(boxes)

    for keys in no_of_keys:
        for box in boxes[keys]:
            if box < no_of_boxes and box not in no_of_keys:
                no_of_keys.append(box)
    if len(no_of_keys) == no_of_boxes:
        return True
    return False
