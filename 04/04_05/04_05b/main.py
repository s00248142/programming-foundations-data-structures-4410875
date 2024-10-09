print('Version 1')
def has_unique_characters(data):
    set_A = set()
    for i in range(len(data)):
        if data[i] not in set_A:
            set_A.add(data[i])
    if len(set_A) == len(data):
        return True
    else: return False

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))

# Cleaner code
print('\nVersion 2')
def has_unique_characters2(data):
    set_A = set(data) # When converting a string to a set, duplicates are deleted
    return len(data) == len(set_A)

print(has_unique_characters2('sample'))
print(has_unique_characters2('hello world'))
print(has_unique_characters2('linkedin'))
print(has_unique_characters2('python'))
