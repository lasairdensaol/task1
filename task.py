# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 15:35:21 2014

@author: user
"""


def _myfun(big_str, small_str):
    # Создание словаря, хранящего информацию о small_str    
    dic_of_small_str = {}
    common_number = 0
    for x in small_str:
    	common_number += 1
    	if x in dic_of_small_str:
                 dic_of_small_str[x][0] += 1
                 dic_of_small_str[x][1] += 1
    	else:
    		dic_of_small_str[x] = [1,1,0]
     
    #Попытка поиска подстроки 
    attempt = 0                             
    #Указывает на число еще не найденных в big_str букв на текущей итерации
    temp_common_number = common_number      
      
    # Поиск перестановок small_str в big_str  
    for x in big_str:
        if x in dic_of_small_str:
            if dic_of_small_str[x][2] == attempt:
                dic_of_small_str[x][1] -= 1
            else:
                dic_of_small_str[x][1] = dic_of_small_str[x][0] - 1
                dic_of_small_str[x][2] = attempt
            temp_common_number -= 1
            if temp_common_number == 0:
                return True
        else:
            temp_common_number = common_number
            attempt += 1
            
            
    return False        


            
if __name__ == "__main__": 
	big_str = raw_input('Enter big string: ')
	small_str = raw_input('Enter small string: ')
    print _myfun(big_str, small_str)        
           
    