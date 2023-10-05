"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    if len(items) == 0:
        return frequencies
    
    count = 0
    prev_item = items[0]

    for i in  range(0,len(items)):
        items[i] = str(items[i])
    items.sort()

    for item in items:
        if item == prev_item:
            count += 1
        else:
            prev_item = item
            count = 1
        frequencies[item] = count
        
    return frequencies

dict = frequencies([100, 'Hello', '100', '100', 100, "Haha"])
print(dict.items())



