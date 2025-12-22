class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
    def __str__(self):
        return str(self.data)

class Lock:
    def __init__(self):
        self.click = 0
        self.root = Node(50)
        curr = self.root
        for i in list(range(51,100)) + list(range(0,50)):
            # print(i)
            new_node = Node(i)
            curr.next = new_node
            new_node.prev = curr
            curr = new_node
        curr.next = self.root
        self.root.prev = curr
        

    def turn(self, lr: ["L", "R"], num: int):
        for _ in range(num):
            if lr == "L":
                self.root = self.root.prev
            else:
                self.root = self.root.next
            if self.root.data == 0:
                self.click += 1
        

with open("2025/src/resources/day1_input.txt") as f:
    code = [l.strip() for l in f.readlines()]

l = Lock()
count = 0
for t_c in code:
    t = t_c[0]
    c = int(t_c[1:])

    l.turn(t, c)

# print(l.root.data)
print(l.click)
