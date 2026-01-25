
def mergeKLists(self, lists):

    def merge(list1, list2):

        temp = list1
        temp1 = list2

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        
        if temp1.val < temp.val:
            list1 = temp1
            temp1 = temp1.next
            list1.next = temp
            temp = list1

        pre = temp

        while temp and temp1:
            if temp.val <= temp1.val:
                pre = temp
                temp = temp.next
            else:
                new = temp1.next
                pre.next = temp1
                temp1.next = temp
                pre = temp1
                temp1 = new

        if temp1:
            pre.next = temp1

        return list1

    li = None
    for i, lii in enumerate(lists):
        if i == 0:
            li = lii
        else:
            li = merge(li, lii)

    return li
