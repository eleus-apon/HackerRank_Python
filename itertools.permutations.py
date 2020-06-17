from itertools import permutations

S, k = input().split()
print(*[''.join(i) for i in permutations(sorted(S),int(k))],sep='\n')

#
permutations(sorted(s),int(n)) returns generated object or something of the sort containing the permutations. 
But it consists of tuples and not strings, thats why we use:-
'*'.join(i) for i in permutations(sorted(s),int(n)) so that each tuple is converted to string

str.join(iterable,)Concatenate any number of strings.
The string whose method is called is inserted in between each given string. The result is returned as a new string.
Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
#
