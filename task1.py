# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 15:35:21 2014

@author: user
"""


def _myfun(big_str, small_str):
    # Создание словаря, хранящего информацию о small_str    
    dic = {}
    common_number = 0
    for x in small_str:
    	common_number += 1
    	if x in dic:
                 dic[x][0] += 1
                 dic[x][1] += 1
    	else:
    		dic[x] = [1,1,0]
     
    #Попытка поиска подстроки 
    attempt = 0                             
    #print dic
         
    #Счетчик для нулей
    number_of_zeros = 0
    #Максимальное количество нулей
    limit_of_zeros = len(dic)
    # Позиция просматриваемого элемента
    pos = -1    
    # Текущее число найденных символов,которые вероятно 
    # Образуют перестановку строки small_str
    number_of_symbols = 0
    
    # Длина small_str
    len_small_str = len(small_str)
    
    # Поиск перестановок small_str в big_str  
    for x in big_str:
        pos += 1
        if x in dic:
            number_of_symbols += 1
            if dic[x][2] == attempt:
                if (dic[x][1] == 0) or (number_of_symbols>len_small_str):
                    ch = big_str[pos-number_of_symbols+1]
                    dic[ch][1] += 1
                    number_of_symbols -= 1
                    if dic[ch][1] == 0:
                        number_of_zeros  += 1
                    elif dic[ch][1] == 1:
                        number_of_zeros -= 1
                if dic[x][1] == 0:
                    number_of_zeros -= 1
                dic[x][1] -= 1
                if dic[x][1] == 0:
                    number_of_zeros += 1
            else:
                dic[x][1] = dic[x][0] - 1
                dic[x][2] = attempt
                if dic[x][1] == 0:
                    number_of_zeros += 1     
            if number_of_zeros == limit_of_zeros:
                return True
        else:
            number_of_symbols = 0
            number_of_zeros = 0
            attempt += 1
            
            
    return False        


            
if __name__ == "__main__":
    big_str = raw_input("Enter string: ")
    small_str = raw_input("Enter substring: ")
    print _myfun(big_str, small_str)
           
    