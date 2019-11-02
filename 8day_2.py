list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]

for x in list1:
    print(f'{x} in list1 and list2') if x in list2 else print(f'{x} only in list1')

    # if x in list2:
    #     print(f'{x} in list1 and list2')
    # else:
    #     print(f'{x} only in list1')

def find_same(l1,l2):
    for x in list1:
        print(f'{x} in list1 and list2') if x in list2 else print(f'{x} only in list1')

if __name__=='__main__':
    find_same(list1,list2)
