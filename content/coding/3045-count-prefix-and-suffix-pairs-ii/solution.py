class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        trie: dict[str, dict] = {}
        res = 0
        for word in words:
            # Add word to the trie tree.
            node = trie
            k = len(word)
            for i in range(k):
                j = k - 1 - i
                key = word[i] + word[j]
                if key not in node:
                    node[key] = {}
                node = node[key]
                if '#' in node:
                    res += node['#'] # Count a matched prefix and suffix.

            if '#' in node:
                node['#'] += 1
            else:
                node['#'] = 1

        return res
