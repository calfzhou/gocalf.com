class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        next = str(self.next.val) if self.next else 'X'
        return f'{self.val} -> {next}'


def build_linked_list(values: list[int | None]) -> ListNode | None:
    root = ListNode(None)
    node = root
    for v in values:
        node.next = node = ListNode(v)

    return root.next


def format_linked_list(head: ListNode | None) -> list[int | None]:
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next

    return values
