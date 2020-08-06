import requests
import json
import random
import time

# TODO1: сделать в виде параметров командной строки
repoURL = "http://github.com/django/django"       #if is public 

# TODO3: добавить проверку формата вводимой даты с автоисправлением, если возможно
startDate = '2014-12-22'
stopDate = '2017-01-19'

branch = 'master'

# список браузеров для ротации в запросе для преодоления защиты от скраперов
user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]
url = 'https://httpbin.org/headers'

# ============== Временный код start ==============
# TODO1: заготовка для командной строки из скрипта, который дает результаты по собственному репозиторию автора
# https://api.github.com/repos/django/django/commits?until=2010-10-10&since=2009-01-01&branch=master&page=25&per_page=100

'''def count_user_commits(user):
    r = requests.get('https://api.github.com/users/%s/repos' % user)
    repos = json.loads(r.content)

    for repo in repos:
        if repo['fork'] is True:
            # skip it
            continue
        n = count_repo_commits(repo['url'] + '/commits')
        repo['num_commits'] = n
        yield repo

def count_repo_commits(commits_url, _acc=0):
    r = requests.get(commits_url)
    commits = json.loads(r.content)
    n = len(commits)
    if n == 0:
        return _acc
    link = r.headers.get('link')
    if link is None:
        return _acc + n
    next_url = find_next(r.headers['link'])
    if next_url is None:
        return _acc + n
    # try to be tail recursive, even when it doesn't matter in CPython
    return count_repo_commits(next_url, _acc + n)


# given a link header from github, find the link for the next url which they use for pagination
def find_next(link):
    for l in link.split(','):
        a, b = l.split(';')
        if b.strip() == 'rel="next"':
            return a.strip()[1:-1]


if __name__ == '__main__':
    import sys
    try:
        user = sys.argv[1]
    except IndexError:
        print "Usage: %s <username>" % sys.argv[0]
        sys.exit(1)
    total = 0
    for repo in count_user_commits(user):
        print "Repo `%(name)s` has %(num_commits)d commits, size %(size)d." % repo
        total += repo['num_commits']

    print "Total commits: %d" % total

'''
# ============== Временный код end  ==============

# Выбираем случайный браузер из списка
user_agent = random.choice(user_agent_list)

# Устанавливаем заголовки 
headers = {'User-Agent': user_agent}

# Создаем запрос с параметрами: 
# startDate - дата начала периода
# stopDate - дата конца периода
# branch - ветка
# 
# Начинаем с первой страницы, количество результатов на страницу 100
'''
#########################################################
#                  request для авторов коммитов
#########################################################
r = requests.get('https://api.github.com/repos/django/django/commits', params={'since': startDate, 'until': stopDate, 'branch': branch, 'page': 1, 'per_page': 100}, headers=headers)

# Парсим в JSON
data=r.json()

# m - количество страниц в результате запроса
m = 0
while 'next' in r.links.keys():
    # получаем следующую страницу
    r = requests.get(r.links['next']['url'], proxies={"http":"http://193.178.249.121:5836"})
    # добавляем к нашим результатам
    data.extend(r.json())
    m+=1
    # таймаут, чтобы не превысить количество запросов в секунду
    time.sleep(0.5) 

# ----- DEBUG start ------  
#print(r.json())
#print('Всего ',m,'страниц')
# ----- DEBUG end  -------


# TODO4: убрать из релиза
# запись в файл для анализа результата запроса и формирования кода
f=open("scrap.json","w",encoding='utf-8')


if r.status_code == 200:
    print('Success!')
    
    # ----- DEBUG start ------ 
    #str = json.loads(r.text)
    #print(json.dumps(str, indent=4, sort_keys=True))
    #ss = json.dumps(str, indent=4, sort_keys=True)
    print(json.dumps(data, indent=4, sort_keys=True))
    # ----- DEBUG end  -------
       
    # форматирование результата в удобном для чтения виде для сохранения в файл  
    ss = json.dumps(data, indent=4, sort_keys=True)
   
    # k - переменная для формирования списка из 30 авторов
    k = 0
    
    # N для хранения количества записей в JSON
    N = len(data)
    
    # Будущий список с именами авторов
    names = []
    
    # Формируем список авторов
    for i in range(N):
        names.append(str[i]['commit']['author']['name'])
       
    # На основе списка авторов names формируем словарь, в котором напротив каждого имени автора его количество коммитов
    # Автор добавляется в словарь автоматически, если их еще нет, в ином случае количество его коммитов увеличивается на 1
    d = dict()
    for c in names:
        d[c] = d.get(c,0) + 1
    
    # Сортируем авторов по количеству их коммитов, в убывающем порядке
    # Получаем список, где каждый элемент в виде:
    # номер. Имя_автора   количево_коммитов
    listofTuples = sorted(d.items(), reverse=True,  key=lambda x: x[1])
    for elem in listofTuples :
        print(f"{k+1:3}. {elem[0]:25} {elem[1]:6}")
        k+=1

    #записываем результат в виде форматированного JSON в файл и сохраняем его
    f.write(ss)
    f.close()
'''

#########################################################
#                  pull request
#########################################################
r = requests.get('https://api.github.com/repos/django/django/pulls?q=is%3Apr+is%3Aclosed', params={'createdAt': startDate, 'closedAt' : stopDate, 'default_branch': branch, 'is': 'pr'}, headers=headers)


f=open("scrap.json","w",encoding='utf-8')

if r.status_code == 200:
    print('Success!')
    str = json.loads(r.text)
    #filter1 = str[i]['created_at']
    '''N = len(str)
    tstr = []
    for i in range(N):
        print(str[i]['created_at'])
        if (str[i]['created_at'] >= startDate):
            tstr.append(str[i])
    
    
    #str = filter_cdate
    print(tstr)'''
    filter_cdate = [x for x in str if x['created_at'] >= startDate]
    str = filter_cdate
    #filterNoClosed = [x for x in str if x['closed_at']!=None]
    #str = filterNoClosed
    #print(str)
    #filterClosed = [x for x in str if x['closed_at']<=stopDate]
    #str = filterClosed
    #print(str)
    #print(json.dumps(str, indent=4, sort_keys=True))
    ss = json.dumps(str, indent=4, sort_keys=True)
    f.write(ss)
    f.close()

elif r.status_code == 404:
#TODO5: продумать надписи об ошибках поинтереснее
    print('Not Found.')
