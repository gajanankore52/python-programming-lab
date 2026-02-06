# Python - Replace second duplicate Occurrence in String



test_str = 'Gfg is best. Gfg also has Classes now. Classes help understand better.'
                
repl_dict = {'Gfg' : 'It', 'Classes' : 'They' } 

test_str = test_str.split()

str1 = ''

for iCnt in range(len(test_str)):
    if test_str[iCnt] in test_str[:iCnt]:
        str1 += repl_dict[test_str[iCnt]] + ' '
    else:
        str1 += test_str[iCnt] + ' '
        
print(str1)
        