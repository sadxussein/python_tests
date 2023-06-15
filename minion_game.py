def minion_game(string):
    kevin, stuart = 0, 0
    
    for l in range(len(string)):        
        for n in range(l, len(string)):
            if string[l] in 'AEIOU':
                kevin += 1
            else:
                stuart += 1
                    
    if kevin > stuart: print("Kevin", kevin)
    elif stuart > kevin: print("Stuart", stuart)
    else: print("Draw")   

if __name__ == '__main__':
    s = input()
    minion_game(s)