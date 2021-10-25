class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        new_node.next = self.head
        self.head = new_node
        # 
        return self

    def add_to_back(self, val):
        new_node = SLNode(val)
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = new_node
        return self
    
    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner.value,end=",")
            runner = runner.next
        return self
    
    def remove_from_front(self):
        self.head = self.head.next
        return self

    def remove_from_back(self):
        last_node = self.head
        while last_node.next.next != None:
            last_node = last_node.next
        last_node.next = None
        return self
    
    def deletemid(self):
        if self.findSize() < 3:
            print()
            self.remove_from_back()
        else:
            mid = self.findSize()//2
            index = 1
            runner = self.head
            while mid+1!=index+1 and runner != None:
                index = index + 1
                runner = runner.next
            print(runner.next.value)
            runner.next = runner.next.next
                
    def reverse(self):
        prev = None
        runner = self.head
        while runner is not None:
            NXT = runner.next
            runner.next = prev
            prev = runner
            runner = NXT
        self.head = prev






    def remove_val(self, val):
        if self.head.value == val:
            self.remove_from_front()
        else:
            runner = self.head
            while runner.next.value != val and runner.next.next != None:
                runner = runner.next
            if runner.next.value == val:
                runner.next = runner.next.next
        return self

    def insert_at(self, val, n):
        if n == 1:
            self.add_to_front(val)
        elif n > 1:
            runner = self.head
            index = 1
            while n != index and runner.next != None:
                runner = runner.next
                index += 1
            Rside=runner.next
            runner.next=SLNode(val)
            runner.next.next=Rside
    def findSize(self):
        res = 0
        node = self.head
        while (node != None):
            res = res + 1
            node = node.next
        # print(res)
        return res


my_list = SList()
my_list.insert_at("1",1)
my_list.insert_at("2",2)
my_list.insert_at("3",3)
my_list.insert_at("4",4)
my_list.insert_at("5",5)
my_list.insert_at("6",6)
my_list.insert_at("7",7)
# my_list.insert_at("8",8)
# my_list.insert_at("9",9)
# my_list.add_to_front("90")
# my_list.add_to_front("80")
# my_list.add_to_front(" 70")
# my_list.add_to_front("60")
# my_list.add_to_front("50")
# my_list.add_to_front("30")
# my_list.add_to_front("40")
# my_list.add_to_front("20")
# my_list.add_to_front("10")
my_list.print_values()
# my_list.remove_val("9")
# my_list.remove_val("8")
# my_list.remove_val("7")
# my_list.remove_val("6")
# my_list.remove_val("4")
# my_list.remove_val("5")
# my_list.remove_val("3")
# my_list.remove_val("2")
# my_list.remove_val("1")
# my_list.remove_val("70")
# my_list.remove_val("60")
my_list.deletemid()
print("..................")
my_list.print_values()

# my_list = SList()
# my_list.add_to_front("are")
# my_list.add_to_front("Linked lists")
# my_list.add_to_back("fun!")
# my_list.add_to_back('extra')
# my_list.add_to_back('stuff')
# my_list.remove_val('abcd')
# my_list.insert_at('abcd', 5)
# my_list.print_values()