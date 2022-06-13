tail = input()
body = input()
head = input()
lists = [tail, body, head]
lists[0], lists[2] = lists[2], lists[0]
print(lists)