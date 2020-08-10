# repan.py

__REPository ANalysis__  is a program for analyzing a Github repository. It counts the number of commits left by the authors in the time specified in the parameters in a particular branch.

## Входные параметры:
1) __repo_name__ includes alphanumeric characters (Latin only) and symbols ```-```, ```_```, ```.```
Eg: ```http://github.com/author/repo```
The specified repository must exist and be public.

2) __start_date__ is a date in one of the formats: ```YYYY-MM-DD```, ```DD-MM-YYYY```, ```MMM-DD-YYYY```.  
Вы не можете указать дату ранее 2008 года.
Если указана только начальная дата, то перед ней следует добавить флаг ```-f```:
Пример: ```http://github.com/author/repo -f 12-12-2012```

3) __end_date__ similarly _start_date_. 
If start and end dates are specified, the end date cannot be earlier than the start date. Dates may be the same, in this case being commits search for a particular day, the date specified in.
If only the end date is specified, then add the flag ```-l``` before it:
Eg: ```http://github.com/author/repo -l 12-12-2012```

4) __branch__ - includes alphanumeric characters (Latin only) and symbols '-', '_', '.', '/'
If the branch name is not specified, the search will be conducted in the  _master_ branch
Eg: ```http://github.com/author/repo master```



> __NOTE!__ Of all the input parameters, only _repo_name_ is required. The rest of the arguments can be left blank




## Sample result output:
```
> python repan.py http://github.com/django/django master
Num. Author                    Commits
  1. Tim Graham                   965
  2. Mariusz Felisiak             583
  3. Jon Dufresne                 341
  4. Sergey Fedoseev              294
  5. Claude Paroz                 277
  6. Simon Charette               259
  7. Hasan Ramezani               173
  8. Carlton Gibson               151
  9. Nick Pope                    135
 10. Mads Jensen                   93
 11. Adam Johnson                  88
 12. François Freitag              63
 13. Adam Chainz                   42
 14. David Smith                   41
 15. Tom Forbes                    37
 16. Florian Apolloner             34
 17. Anton Samarchyan              33
 18. Baptiste Mispelon             31
 19. Josh Schneier                 23
 20. Ed Morley                     20
 21. Johannes Hoppe                19
 22. Srinivas Reddy Thatiparthy     19
 23. Tom                           19
 24. Hannes Ljungberg              18
 25. Daniel Hahler                 17
 26. can                           17
 27. Paulo                         15
 28. Aymeric Augustin              14
 29. Markus Holtermann             14
 30. Ian Foote                     13
 ```
***

# repan.py

REPository ANalysis - программа для анализа репозитория Github. Она считает количество коммитов, оставленных авторами за указанное в параметрах время в определенной ветке.

## Входные параметры:
1) __имя_репозитория__ - включает буквенно-цифровые символы (только латиница) и символы ```-```, ```_```, ```.```
Пример: ```http://github.com/author/repo```
Указанный репозиторий должен существовать и быть публичным.

2) __дата_начала_периода__ - дата в одном из форматов: ```YYYY-MM-DD```, ```DD-MM-YYYY```, ```MMM-DD-YYYY```.  
Вы не можете указать дату ранее 2008 года.
Если указана только начальная дата, то перед ней следует добавить флаг ```-f```:
Пример: ```http://github.com/author/repo -f 12-12-2012```

3) __дата_окончания_периода__ - аналогично _дате_начала_периода_. 
Если указаны даты начала и конца, то конечная дата не может быть более ранней, чем начальная дата. Даты могут совпадать, в таком случае ведется поиск коммитов за конкретный день, указанный в дате.
Если указана только конечная дата, то перед ней следует добавить флаг ```-l```:
Пример: ```http://github.com/author/repo -l 12-12-2012```

4) __название_ветки__ - включает буквенно-цифровые символы (только латиница) и символы '-', '_', '.', '/'
Если название ветки не указано, поиск будет вестись в ветке _master_
Пример: ```http://github.com/author/repo master```



> __ВНИМАНИЕ!__ Из всех входных параметров только имя_репозитория является обязательным. Остальные аргументы можно не заполнять




## Образец вывода результата:
```
> python repan.py http://github.com/django/django master
Num. Author                    Commits
  1. Tim Graham                   965
  2. Mariusz Felisiak             583
  3. Jon Dufresne                 341
  4. Sergey Fedoseev              294
  5. Claude Paroz                 277
  6. Simon Charette               259
  7. Hasan Ramezani               173
  8. Carlton Gibson               151
  9. Nick Pope                    135
 10. Mads Jensen                   93
 11. Adam Johnson                  88
 12. François Freitag              63
 13. Adam Chainz                   42
 14. David Smith                   41
 15. Tom Forbes                    37
 16. Florian Apolloner             34
 17. Anton Samarchyan              33
 18. Baptiste Mispelon             31
 19. Josh Schneier                 23
 20. Ed Morley                     20
 21. Johannes Hoppe                19
 22. Srinivas Reddy Thatiparthy     19
 23. Tom                           19
 24. Hannes Ljungberg              18
 25. Daniel Hahler                 17
 26. can                           17
 27. Paulo                         15
 28. Aymeric Augustin              14
 29. Markus Holtermann             14
 30. Ian Foote                     13
 ```