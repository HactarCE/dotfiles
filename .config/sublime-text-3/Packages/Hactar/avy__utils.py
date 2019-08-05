# based on https://github.com/abo-abo/avy/wiki/Library

import math


def avy_subdiv(n, base):
    """Split a number in terms of the base.

    Split a number in terms of the base as evenly as possible while following
    these rules:
    - At most, only one member of the result may be not a power of the base.
    - The result must be sorted.
    - Each member of the result must be between 2**k and 2**(k+1), where k is a
      positive integer (int(log(n, base)) - 1).

    If n < b, then 0 is allowed in the result.
    """
    if n <= base:
        return [1] * n + [0] * (base - n)
    k = int(math.log(n, base)) - 1
    result = [base ** k] * base
    n -= base ** (k + 1)
    for i in reversed(range(base)):
        n += base ** k
        diff = min(n, base ** (k + 1))
        result[i] = diff
        n -= diff
        if not n:
            break
    return result


# print(avy_subdiv(42, 5))
# print(avy_subdiv(42, 4))
# print(avy_subdiv(42, 3))
# print(avy_subdiv(42, 2))
# print(avy_subdiv(42, 40))
# print(avy_subdiv(42, 50))


def avy_tree(leaves, keys):
    """Return a nested dictionary where subsequent indexing by keys leads to a
    leaf.
    """
    if len(leaves) == 0:
        return {}
    if len(leaves) == 1:
        return leaves[0]
    i1, i2 = 0, 0
    result = {}
    for key, chunk_size in zip(keys, avy_subdiv(len(leaves), len(keys))):
        if chunk_size:
            i2 += chunk_size
            chunk = leaves[i1:i2]
            result[key] = avy_tree(chunk, keys)
            i1 += chunk_size
    return result

# from pprint import pprint
# pprint(avy_tree("ABCDEFGHIJKLMNOPQRSTUVWXYZ", [1, 2, 3, 4]))


def avy_flatten(tree):
    """Return a flat dictionary where indexing by a sting of joined keys leads
    to a leaf.

    Keys to the tree should be single-character strings.
    """
    if not tree:
        return {}
    elif isinstance(tree, dict):
        result = {}
        for k1, v1 in tree.items():
            for k2, v2 in avy_flatten(v1).items():
                result[k1 + k2] = v2
        return result
    else:
        return {'': tree}

# from pprint import pprint
# pprint(avy_flatten(avy_tree("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 'abcd')))


def avy_seqs(n, keys, *, allow_empty=True):
    """Return a list of key sequences used to index n leaves."""
    if n == 0:
        return []
    if n == 1 and allow_empty:
        return ['']
    result = []
    for key, chunk_size in zip(keys, avy_subdiv(n, len(keys))):
        for rest in avy_seqs(chunk_size, keys):
            result.append(key + rest)
    return result


def common_prefix(a, b):
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            return a[:i]
    return a[:len(b)]
