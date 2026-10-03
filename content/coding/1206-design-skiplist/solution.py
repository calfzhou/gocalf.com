from random import randrange


class Node:
    def __init__(self, val=None):
        self.val = val
        self.rights: list['Node'|None] = []


class Skiplist:

    def __init__(self):
        self._head = Node() # A virtual head node to simplify boundary case processing.
        self._head.rights.append(None)

    def search(self, target: int) -> bool:
        node = self._head
        while node:
            for r in reversed(node.rights):
                if not r: continue
                if r.val == target:
                    return True
                if r.val < target:
                    node = r
                    break
            else:
                return False

        return False


    def add(self, num: int) -> None:
        node = self._head
        parents: list[Node] = []
        while node:
            for r in reversed(node.rights):
                if r and r.val <= num: # Stable sort.
                    node = r
                    break
                else:
                    parents.append(node)
            else:
                break

        new_node = Node(num)
        level = 0
        need_ins = 1
        while need_ins:
            if level < len(parents):
                parent = parents[-1 - level]
            else:
                parent = self._head
                parent.rights.append(None)

            new_node.rights.append(parent.rights[level])
            parent.rights[level] = new_node
            level += 1
            need_ins = randrange(2) # Randomly choose whether to promote it to next level.

    def erase(self, num: int) -> bool:
        node = self._head
        parents = []
        while node:
            for r in reversed(node.rights):
                if r and r.val < num: # Remove the left-most when multiple same numbers.
                    node = r
                    break
                else:
                    parents.append(node)
            else: break

        node = parents[-1].rights[0]
        if not node or node.val != num:
            return False

        for level in range(len(node.rights)):
            parents[-1 - level].rights[level] = node.rights[level]

        return True

    def format(self) -> str:
        height = len(self._head.rights)
        layers = [['HEAD'] for _ in range(height)]

        node = self._head.rights[0]
        while node:
            level = len(node.rights)

            part = f'>{node.val}'
            for i in range(level):
                layers[i].append(part)

            part = '-' * len(part)
            for i in range(level, height):
                layers[i].append(part)

            node = node.rights[0]

        for layer in layers:
            layer.append('>NIL')

        layers.reverse()
        layers.append('')
        return '\n'.join('-'.join(layer) for layer in layers)


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
