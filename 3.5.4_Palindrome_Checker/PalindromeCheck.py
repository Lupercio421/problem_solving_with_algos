from collections import deque

def palchecker(aString):
    chardeque = deque()

    for ch in aString:
        chardeque.appendleft(ch)

    stillEqual = True

    while len(chardeque) > 1 and stillEqual:
        first = chardeque.pop()

        last = chardeque.popleft()

        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))