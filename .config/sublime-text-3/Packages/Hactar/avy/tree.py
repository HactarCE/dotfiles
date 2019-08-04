# based on https://github.com/abo-abo/avy/wiki/Library

import math


def avy_subdiv(n, base):
    """Split a number in terms of the base.

    Split a number in terms of the base as evenly as possible while following
    these rules:
    - At most, only one member of the result may be not a power of the base.
    - The result must be sorted.
    - Each member of the result must be between 2**k and 2**(k+1), where k is a
      positive integer (int(log(n, base))).

    If n < b, then 0 is allowed in the result.
    """
    if n <= base:
        return [1] * n + [0] * (base - n)
    k = int(math.log(n, base))
    result = [n ** k] * base
    n -= n ** k * base
    for i in reversed(range(base)):
        n += n ** k
        diff = min(n, n ** (k + 1))
        result[i] = diff
        n -= diff
        if not n:
            break
    return result


print(avy_subdiv(42, 5))
print(avy_subdiv(42, 4))
print(avy_subdiv(42, 3))
print(avy_subdiv(42, 2))
print(avy_subdiv(42, 40))
print(avy_subdiv(42, 50))


def avy_tree(leaves, keys):
    """Return a nested dictionary where subsequent indexing by keys lead to
    leaves.
    """
    if len(leaves) == 1:
        return leaves[0]
    i1, i2 = 0, 0
    result = {}
    for key, chunk_size in zip(keys, avy_subdiv(leaves, len(keys))):
        i2 += chunk_size
        chunk = leaves[i1:i2]
        result[key] = avy_tree(chunk, keys)
        i1 += chunk_size
