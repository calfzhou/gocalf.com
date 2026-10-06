from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: list[list[int]] = []
        mapping: dict[str, int] = {} # sorted(s): groups index
        for s in strs:
            key = ''.join(sorted(s))
            idx = len(groups)
            if key not in mapping:
                mapping[key] = idx
                groups.append([])
            else:
                idx = mapping[key]

            groups[idx].append(s)

        return groups
