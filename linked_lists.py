class Linked_List:

    class Node:
        def __init__(self, val):
            self.val = val
            self.__next = None
            self.__prev = None

    def __init__(self):
        self.__header = Linked_List.Node(None)
        self.__trailer = Linked_List.Node(None)
        self.__header.__next = self.__trailer
        self.__trailer.__prev = self.__header
        self.__size = 0

    def __len__(self): ## TESTED AND WORKS
        return self.__size

    def append_element(self, val):    ## TESTED AND WORKS
        newest = Linked_List.Node(val)
        prevElement = self.__trailer.__prev
        prevElement.__next = newest
        self.__trailer.__prev = newest
        newest.__prev = prevElement
        newest.__next = self.__trailer
        self.__size = self.__size + 1

    def insert_element_at(self, val, index): ## TESTED AND WORKS
        if (index >= len(self)) or (index < 0): ## If index is out of range
            raise IndexError
        newest = Linked_List.Node(val)

        if index == 0: ## Inserting at head
            nextElement = self.__header.__next
            self.__header.__next = newest
            nextElement.__prev = newest
            newest.__prev = self.__header
            newest.__next = nextElement

        elif index != 0: ## Inserting anywhere else
            cur = self.__header
            for i in range(0, index):
                cur = cur.__next
            nextElement = cur.__next
            cur.__next = newest
            nextElement.__prev = newest
            newest.__prev = cur
            newest.__next = nextElement

        self.__size = self.__size + 1

    def remove_element_at(self, index): ## TESTED AND WORKS
        if ( index >= self.__size ) or (index < 0):
            raise IndexError
        current = self.__header
        for i in range(0, index):
            current = current.__next
        current.__next = current.__next.__next
        current.__next.__previous = current
        self.__size = self.__size - 1

    def get_element_at(self, index): ## TESTED AND WORKS
        if (index >= len(self)) or (index < 0):
            raise IndexError
        else:
            i = 0
            current = self.__header.__next
            while(i < index):
                current = current.__next
                i = i + 1
        return current.val

    def rotate_left(self): ## TESTED AND WORKS
        if len(self) < 2: ## to handle exceptions
            return

        temp = self.__header.__next
        newHead = temp.__next
        self.__header.__next = newHead
        newHead.__prev = self.__header
        prevTail = self.__trailer.__prev
        prevTail.__next = temp
        self.__trailer.__prev = temp
        temp.__prev = prevTail
        temp.__next = self.__trailer
        return

    def __str__(self): ## TESTED AND WORKS
        if self.__size == 0:
            return "[ ]"
        a = "[ "
        b = self.__header.__next
        if b is not self.__trailer:
            a = a + str(b.val)
            b = b.__next
            while b is not self.__trailer:
                a = a + ", " + str(b.val)
                b = b.__next
        a = a + " ]"
        return a ## TESTED AND WORKS

    def __iter__(self):
        self.iter_index = 0
        return self

    def __next__(self):
        if self.iter_index < self.__len__():
            to_return = self.get_element_at(self.iter_index)
            self.iter_index = self.iter_index + 1
        else:
            raise StopIteration
        return to_return

if __name__ == '__main__':
w
    ## Cases will be reset after every individual test
    ## 3 Cases will be tested: Empty, list with one item, and list with 5 items
    ## Case 1: Empty Linked_List
    case1 = Linked_List()
    case = 1
    print("\nNow testing case " + str(case) + ": empty set")
    print("Original list is:" + str(case1))

    ## Checking __len__
    print("\n" + "Checking __len__ function")
    try:
            print("Length is " + str(len(case1)))
    except ValueError:
            print("Length undefined")

    ## Checking append_element
    print("\n" + "Checking append_element function")
    try:
        case1.append_element("appended element")
        print("Appended list: " + str(case1))
        case1 = Linked_List()
    except ValueError:
        print("append_element method broken")

    ## Checking insert_element_at
    print("\n" + "Checking insert_element_at function")
    try:
        case1.insert_element_at("inserted element", -1)
        print("Inserted list is" + str(case1))
        case1 = Linked_List()
    except IndexError:
        print("Index -1 out of range!")
    try:
        case1.insert_element_at("inserted element", 0)
        print("Inserted list is" + str(case1))
        case1 = Linked_List()
    except IndexError:
        print("Index 0 out of range!")
    try:
        case1.insert_element_at("inserted element", len(case1))
        case1 = Linked_List()
    except IndexError:
        print("Index " + str(len(case1)) + " out of range!")
    case1 = Linked_List()

    ## Checking remove_element_at
    print("\n" + "Checking remove_element_at function")
    try:
        case1.remove_element_at(-1)
    except IndexError:
        print("Index -1 out of range!")
    try:
        case1.remove_element_at(0)
    except IndexError:
        print("Index 0 out of range!")
    try:
        case1.remove_element_at(len(case1))
    except IndexError:
        print("Index " + str(len(case1)) + " out of range!")
    case1 = Linked_List()

    ## Checking get_element_at
    print("\n" + "Checking get_element_at function")
    try:
        case1.get_element_at(-1)
    except IndexError:
        print("Index -1 out of range!")
    try:
        case1.get_element_at(0)
    except IndexError:
        print("Index 0 out of range!")
    try:
        case1.get_element_at(len(case1))
    except IndexError:
        print("Index " + str(len(case1)) + " out of range!")
    case1 = Linked_List()

    ## Checking rotate_left
    print("\n" + "Checking rotate_left function")
    try:
        print("Original list: " + str(case1))
        case1.rotate_left()
        print("Rotated list: " + str(case1))
    except IndexError:
        print("Rotation failed")
    case1 = Linked_List()

    ## Checking for loop
    print("\n" + "Checking for loop")
    try:
        print("Our nodes, in order, are:")
        for node in case1:
            print (node)
        case1 = Linked_List()
    except TypeError:
        print("For looping failed")

    ## resetting
    print("\n ____________ \n")


    ## Case 2: Linked_List containing one element
    case2 = Linked_List()
    case2.append_element("Item 1")
    case = 2
    print("Now testing case " + str(case) + ": set with 1 item")
    print("Original list is:" + str(case2))

    ## Checking __len__
    print("\n" + "Checking __len__ function")
    print("Original list is:" + str(case2))
    try:
            print("Length is " + str(len(case2)))
    except ValueError:
            print("Length undefined")

    ## Checking append_element
    print("\n" + "Checking append_element function")
    print("Original list is:" + str(case2))
    try:
        case2.append_element("appended element")
        print("Appended list: " + str(case2))
        case2 = Linked_List()
        case2.append_element("Item 1")
    except ValueError:
        print("append_element method broken")

    ## Checking insert_element_at
    print("\n" + "Checking insert_element_at function")
    print("Original list is:" + str(case2))
    try:
        case2.insert_element_at("inserted element", -1)
        print("Inserted list is" + str(case2))
        case2 = Linked_List()
        case2.append_element("Item 1")
    except IndexError:
        print("Index -1 out of range!")
    try:
        case2.insert_element_at("inserted element", 0)
        print("Inserted list is" + str(case2))
        case2 = Linked_List()
        case2.append_element("Item 1")
    except IndexError:
        print("Index 0 out of range!")
    try:
        case2.insert_element_at("inserted element", len(case2))
        case2 = Linked_List()
        case2.append_element("Item 1")
    except IndexError:
        print("Index " + str(len(case2)) + " out of range!")
    case2 = Linked_List()
    case2.append_element("Item 1")

    ## Checking remove_element_at
    print("\n" + "Checking remove_element_at function")
    print("Original list is:" + str(case2))
    try:
        case2.remove_element_at(-1)
        print("Removed list is: " + str(case2))
        case2 = Linked_List()
        case2.append_element("Item 1")
    except IndexError:
        print("Index -1 out of range!")
    try:
        case2.remove_element_at(0)
        print("Removed list is: " + str(case2))
        case2 = Linked_List()
        case2.append_element("Item 1")
    except IndexError:
        print("Index 0 out of range!")
    try:
        case2.remove_element_at(len(case2))
        print("Removed list is: " + str(case2))
        case2 = Linked_List()
        case2.append_element("Item 1")
    except IndexError:
        print("Index " + str(len(case2)) + " out of range!")
    case2 = Linked_List()
    case2.append_element("Item 1")

    ## Checking get_element_at
    print("\n" + "Checking get_element_at function")
    print("Original list is:" + str(case2))
    try:
        temp = str(case2.get_element_at(-1))
        print("Value at index -1 is: " + temp)
    except IndexError:
        print("Index -1 out of range!")
    try:
        temp = str(case2.get_element_at(0))
        print("Value at index 0 is: " + temp)
    except IndexError:
        print("Index 0 out of range!")
    try:
        temp = str(case2.get_element_at(len(case2)))
        print("Value at index " + str(len(case2)) + " is: " + temp)
    except IndexError:
        print("Index " + str(len(case2)) + " out of range!")
    case2 = Linked_List()
    case2.append_element("Item 1")

    ## Checking rotate_left
    print("\n" + "Checking rotate_left function")
    print("Original list is:" + str(case2))
    try:
        case2.rotate_left()
        print("Rotated list: " + str(case2))
    except IndexError:
        print("Rotation failed")
    case2 = Linked_List()
    case2.append_element("Item 1")

    ## Checking for loop
    print("\n" + "Checking for loop")
    print("Original list is:" + str(case2))
    try:
        print("Our nodes, in order, are:")
        for node in case2:
            print (node)
        case2 = Linked_List()
        case2.append_element("Item 1")
    except TypeError:
        print("For looping failed")

    ## resetting
    print("\n ____________ \n")

    ## Case 3: Linked_List with several (5) elements
    case3 = Linked_List()
    for i in range(1, 6):
            case3.append_element(("Item " + str(i)))
    case = 3
    print("Now testing case " + str(case) + ": set with 5 items")
    print("Original list is:" + str(case3))

    ## Checking __len__
    print("\n" + "Checking __len__ function")
    print("Original list is:" + str(case3))
    try:
            print("Length is " + str(len(case3)))
    except ValueError:
            print("Length undefined")

    ## Checking append_element
    print("\n" + "Checking append_element function")
    print("Original list is:" + str(case3))
    try:
        case3.append_element("appended element")
        print("Appended list: " + str(case3))
        case3 = Linked_List()
        for i in range(1, 6):
            case3.append_element(("Item " + str(i)))
    except ValueError:
        print("append_element method broken")

    ## Checking insert_element_at
    print("\n" + "Checking insert_element_at function")
    print("Original list is:" + str(case3))
    try:
        case3.insert_element_at("inserted element", -1)
        print("Inserted list is" + str(case3))
        case3 = Linked_List()
        for i in range(1, 6):
            case3.append_element(("Item " + str(i)))
    except IndexError:
        print("Index -1 out of range!")
    try:
        case3.insert_element_at("inserted element", 0)
        print("Inserted list is" + str(case3))
        case3 = Linked_List()
        for i in range(1, 6):
            case3.append_element(("Item " + str(i)))
    except IndexError:
        print("Index 0 out of range!")
    try:
        case3.insert_element_at("inserted element", len(case3))
        case3 = Linked_List()
        for i in range(1, 6):
            case3.append_element(("Item " + str(i)))
    except IndexError:
        print("Index " + str(len(case3)) + " out of range!")
    case3 = Linked_List()
    for i in range(1, 6):
            case3.append_element(("Item " + str(i)))

    ## Checking remove_element_at
    print("\n" + "Checking remove_element_at function")
    print("Original list is:" + str(case3))
    try:
        case3.remove_element_at(-1)
        print("Removed list is: " + str(case3))
        case3 = Linked_List()
        for i in range(1, 6):
            case3.append_element(("Item " + str(i)))
    except IndexError:
        print("Index -1 out of range!")
    try:
        case3.remove_element_at(0)
        print("Removed list is: " + str(case3))
        case3 = Linked_List()
        for i in range(1, 6):
            case3.append_element(("Item " + str(i)))
    except IndexError:
        print("Index 0 out of range!")
    try:
        case3.remove_element_at(len(case3))
        print("Removed list is: " + str(case3))
        case3 = Linked_List()
        for i in range(1, 6):
            case3.append_element(("Item " + str(i)))
    except IndexError:
        print("Index " + str(len(case3)) + " out of range!")
    case3 = Linked_List()
    for i in range(1, 6):
            case3.append_element(("Item " + str(i)))

    ## Checking get_element_at
    print("\n" + "Checking get_element_at function")
    print("Original list is:" + str(case3))
    try:
        temp = str(case3.get_element_at(-1))
        print("Value at index -1 is: " + temp)
    except IndexError:
        print("Index -1 out of range!")
    try:
        temp = str(case3.get_element_at(0))
        print("Value at index 0 is: " + temp)
    except IndexError:
        print("Index 0 out of range!")
    try:
        temp = str(case3.get_element_at(len(case3)))
        print("Value at index " + str(len(case3)) + " is: " + temp)
    except IndexError:
        print("Index " + str(len(case3)) + " out of range!")
    case3 = Linked_List()
    for i in range(1, 6):
            case3.append_element(("Item " + str(i)))

    ## Checking rotate_left
    print("\n" + "Checking rotate_left function")
    print("Original list is:" + str(case3))
    try:
        case3.rotate_left()
        print("Rotated list: " + str(case3))
    except IndexError:
        print("Rotation failed")
    case3 = Linked_List()
    for i in range(1, 6):
            case3.append_element(("Item " + str(i)))

    ## Checking for loop
    print("\n" + "Checking for loop")
    print("Original list is:" + str(case3))
    try:
        print("Our nodes, in order, are:")
        for node in case3:
            print (node)
        case3 = Linked_List()
        for i in range(1, 6):
            case3.append_element(("Item " + str(i)))
    except TypeError:
        print("For looping failed")

    ## resetting
    print("\n ____________ \n")
 