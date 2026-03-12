#sets 1

s1 = {'math','physics','chemistry'}
s2 = {'physics','biology','math'}

common = s1 & s2
only_first = s1 - s2
only_second = s2 - s1
total_unique = s1 | s2

print(common)
print(only_first)
print(only_second)
print(total_unique)
