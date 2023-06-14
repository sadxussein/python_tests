def print_rangoli(size):
    width = 1+(size-1)*4
    ch_list = ['a']
    for c in range(98, 97+size):
        #ch_list.insert(0, chr(c))
        ch_list.append(chr(c))
    for i in range(1, size+1):
        print(ch_list[-i:], -i)
    print(ch_list)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)