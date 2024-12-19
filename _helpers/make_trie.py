class TrieNode:
    label: str = ""
    count: int = 0
    children: dict

    def __init__(self, label):
        if label is None:
            self.label = "_root"
        else:
            self.label = label
        self.children = {}

    def __repr__(self):
        return f'<TrieNode label="{self.label}">'


class Trie:
    root = TrieNode(None)

    def __init__(self, strings: list[str]):
        for s in strings:
            cur = self.root
            for c in s:
                if c not in cur.children:
                    cur.children[c] = TrieNode(c)
                cur = cur.children[c]
            cur.count += 1

    def has(self, string) -> bool:
        cur = self.root
        for c in string:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        return cur.count >= 0


def make_trie(strings: list[str]):
    trie = Trie(strings)
    return trie
