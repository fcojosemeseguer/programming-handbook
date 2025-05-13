def rev_list(lista):
    """
    Time Complexity : O(n)
    Space Complexity : O(1)
    """
    if (lista.first is None) or (lista.first.next is None):
        return lista
    
    pt1 = lista.first
    pt2 = lista.first.next
    pt3 = pt2.next  #lista.first.next.next

    pt2.next = pt1
    pt1.next = None
    while (pt3 != None):
        pt1 = pt2
        pt2 = pt3
        pt3 = pt3.next
        pt2.next = pt1

    lista.first = pt2
    return lista




# Recursive Method
"""
Time Complexity : O(n)
Space Compexty : O(n)
"""

"""def reverse_linkedlist(lista):
    if lista.head is None or lista.head.next is None:
        return lista.head
    
    last = reverse_linkedlist(lista.head.next)
    lista.head.next.next = lista.head
    lista.head.next = None
    return last
"""


from linkedlist_ import LinkedList

if __name__ == '__main__':

    L = LinkedList(1)
    L.insert_end(2)
    L.insert_end(3)
    L.insert_end(4)
    L.insert_end(5)

    L.display()

    rev_list(L)

    L.display()