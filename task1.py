def FindMiMiMi(str1, str2):
    dic = {}
    summa = 0
    for i in str1:
        summa += 1
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
            
    find = False
    for i in range(len(str2) - len(str1) + 1):
        substr = str2[i:i+len(str1)]
        dic_temp = dic.copy()
        sum_temp = summa
        for s in substr:
            if s in str1:
                if (dic_temp[s] > 0):
                    dic_temp[s] -= 1
                    sum_temp -= 1
                else:
                    break
            else:
                break
            if (sum_temp == 0):
                find = True
                break
        if (find):
            break
    return (find)
    
    
    
    
    
s2 = raw_input("Enter string: ")
s1 = raw_input("Enter substring: ")
print FindMiMiMi(s1, s2)

                