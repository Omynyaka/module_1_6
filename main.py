my_dict={'Denis':1997,'Dasha':1988,'Natasha':1989}
print(my_dict)
print(my_dict['Denis'])
print(my_dict.get('Mihail','Отсутсвуют данные'))
a=my_dict.pop('Denis')
print(my_dict)
print(a)
my_dict.update({'Marina':1979,'Sergey':1980})
print(my_dict)
