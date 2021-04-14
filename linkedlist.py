class linkedlist:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode



node1 = linkedlist(3)
node2 = linkedlist(5)
node3 = linkedlist(10)

node1.nextNode = node2
node2.nextNode = node3

currentnode = node1
while True:
    if currentnode.nextNode is not None:
        print(currentnode.data, '--->', end='')
    else:
        print(currentnode.data)
        break
    currentnode = currentnode.nextNode


        

