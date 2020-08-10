# REPository ANalysis

REPository ANalysis - программа для анализа репозитория Github. Она считает количество коммитов, оставленных авторами за указанное в параметрах время в определенной ветке.

## Входные параметры:
1) имя_репозитория - включает буквенно-цифровые символы (только латиница) и символы '-', '_', '.'
Пример: ```http://github.com/author/repo```
Указанный репозиторий должен существовать и быть публичным.

2) дата_начала_периода - дата в одном из форматов: YYYY-MM-DD, DD-MM-YYYY, MMM-DD-YYYY. Внимание! Указанная дата не может быть ранее 2008 года.
Если указана только начальная дата, то перед ней следует добавить флаг -f:
Пример: http://github.com/author/repo -f 12-12-2012

3) дата_окончания_периода - аналогично дате_начала_периода. 
Если указаны даты начала и конца, то конечная дата не может быть более ранней, чем начальная дата. Даты могут совпадать, в таком случае ведется поиск коммитов за конкретный день, указанный в дате.
Если указана только конечная дата, то перед ней следует добавить флаг -l:
Пример: http://github.com/author/repo -l 12-12-2012

4) название_ветки - включает буквенно-цифровые символы (только латиница) и символы '-', '_', '.', '/'
Если название ветки не указано, поиск будет вестись в ветке "master"
Пример: http://github.com/author/repo master

---------------------------------
__ВНИМАНИЕ!!!__ Из всех входных параметров только имя_репозитория является обязательным. Остальные аргументы можно не заполнять
---------------------------------


## Образец вывода результата:

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