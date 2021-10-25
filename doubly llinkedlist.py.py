class DLNode:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class DList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, val):
        new_node = DLNode(val)
        if self.tail == None:
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
        self.head = new_node
        return self

    def add_to_back(self, val):
        new_node = DLNode(val)
        if self.head == None:
            self.head = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
        self.tail = new_node
        return self

    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner.value, end=",")
            runner = runner.next
        return self

    def remove_from_front(self):
        if self.findSize() == 1:  # new
            self.head = None  # new
        elif self.head != None:
            self.head = self.head.next
            self.head.previous = None
        return self

    def remove_from_back(self):
        if self.tail != None:
            self.tail = self.tail.previous
            self.tail.next = None
        return self

    def deletemid(self):
        if self.findSize() < 3:
            print()
            self.remove_from_front()
        mid = self.findSize()//2
        index = 1
        runner = self.head
        while mid+1 != index and runner != None:
            index = index + 1
            runner = runner.next
        print(runner.next.value)
        # print("++++++++")
        # print(mid)
        # print(index)
        # print(runner.value)
        # print("++++++++")
        
        tmpPrev = runner.previous
        tmpNext = runner.next
        tmpPrev.next = tmpNext
        tmpNext.previous = tmpPrev
        # print(tmpNext.value)
        # print(tmp)
        # print(tmpPrev.value)
            # if index == mid:
                # tempPre = runner.previous
                # temp = runner.value
                # tempNxt = runner.next
                # # print(tempPre.value)
                # print(node.value)
                # print(tempNxt.value)

    def reverse(self):
        run = self.tail
        while run is not None:
            print(run.value)
            run = run.previous
        print()
        return self

    def findSize(self):
        counter = 0
        runner = self.head
        while (runner != None):
            counter = counter + 1
            runner = runner.next
        # print(res)
        return counter

    def remove_val(self, val):
        if self.head != None and self.head.value == val:
            self.remove_from_front()
        elif self.head != None:
            runner = self.head
            while runner.next.value != val and runner.next.next != None:
                runner = runner.next
            if runner.next.value == val and runner.next.next != None:
                runner.next.next.previous = runner
                runner.next = runner.next.next
            elif runner.next.value == val and runner.next.next == None:
                self.remove_from_back()
        return self

    def insert_at(self,val,n):
        if n==1:
            self.add_to_front(val)
        elif n>1 and self.head!=None and self.tail!=None:
            insert_node=self.head
            index=1
            while n!=index and insert_node.next!=None:
                insert_node=insert_node.next
                index+=1
            if insert_node.next==None:
                self.add_to_back(val)
            else:
                prev_node=insert_node
                next_node=insert_node.next
                insert_node.next=DLNode(val)
                insert_node.next.next=next_node
                insert_node.next.previous=prev_node
                insert_node.next.next.previous=insert_node.next
        else:
            self.add_to_front(val)
        return self


my_list2 = DList()
my_list2.insert_at(70, 1)
my_list2.insert_at(60, 1)
my_list2.insert_at(50, 1)
my_list2.insert_at(40, 1)
my_list2.insert_at(30, 1)
my_list2.insert_at(20, 1)
my_list2.insert_at(10, 1)
my_list2.print_values()
print(".........................")
my_list2.deletemid()
my_list2.print_values()
print(".........................")
my_list2.print_values()
print(my_list2.findSize())

# my_list2.find(50)

# my_list2.add_to_front(10)
# my_list2.add_to_front(20)
# my_list2.add_to_back(30)
# my_list2.add_to_back(40)
# my_list2.add_to_back(50)
# my_list2.remove_val(60)
# my_list2.insert_at(76,2)
# # my_list2.remove_from_back()
# my_list2.print_values()
# print(".........................")
# # my_list2.reverse()
# my_list2.find(50)
# my_list2.findSize()
# my_list2.deletemid(2)
