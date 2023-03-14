"""
WIKTOR SATORA
"""
import queue

from egz1atesty import runtests

def snow( S ):
    return sum([value-index for index, value in enumerate(sorted(S,reverse=True)) if value>index])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
