# Return a generator object from a nested list construct.

import sys

def flatten(n):
    iterstack = [iter(n)]
    while iterstack:
        for elem in iterstack[-1]:
            try:
                it = iter(elem)
            except TypeError:
                pass
            else:
                if not isinstance(elem, basestring):
                    iterstack.append(it)
                    break
            yield elem
        else:
            iterstack.pop()  # remove iterator only when it is exhausted

            
                    