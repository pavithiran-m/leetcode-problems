def copyRandomList(self, head):
        old ={None:None}

        temp=head

        while temp:
            old[temp]=(temp.val)
            temp=temp.next

        temp=head
        while temp:
            copy=old[temp]
            copy.next=old[temp.next]
            copy.random =old[temp.random]
            temp=temp.next
        return old[head]