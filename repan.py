import requests
import json
import time


# According to the form validation messages on Create repository page,
# Github repo's name should include alphanumeric symbols and '-', '_', '.'
def validRepo(repo):
    return ''.join(c for c in repo if  c not in '-_.').isalpha()

# Rules got from https://github.com/shinnn/github-username-regex:
# According to the form validation messages on Join Github page,
# + Github username may only contain alphanumeric characters or hyphens.
# + Github username cannot have multiple consecutive hyphens.
# + Github username cannot begin or end with a hyphen.
# + Maximum is 39 characters.
def validUser(user):
    alpha = ''.join(user.split('-')).isalpha()
    hyphens = user.find('--')==-1
    behyp = user.find('-')!=0 and user.find('-')!=len(user)-1
    maxlen = len(user)<=39
    return alpha and hyphens and behyp and maxlen

def ValidRepoURL(repoURL):
    if repoURL.find('github.com') == -1:
        print('Wrong repo URL. The address should be like this: http://github.com/author/repo.')
        return False
    else:
        if repoURL.find('http://') > -1 or repoURL.find('https://') > -1:
            url = repoURL.split('//')[1]
        else:
            url = repoURL
        url = url.split('github.com/')[1].split('/')
        user = url[0]
        repo = url[1]
        return validRepo(repo) and validUser(user)


# TODO1: сделать в виде параметров командной строки
repoURL = "http://github.com/django/django"       #if is public 

# TODO3: добавить проверку формата вводимой даты с автоисправлением, если возможно
startDate = '2014-12-22'
stopDate = '2017-01-19'

branch = 'master'




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


# Создаем запрос с параметрами: 
# startDate - дата начала периода
# stopDate - дата конца периода
# branch - ветка
# 
# Начинаем с первой страницы, количество результатов на страницу 100

#########################################################
#                  request для авторов коммитов
#########################################################
r = requests.get('https://api.github.com/repos/django/django/commits', params={'since': startDate, 'until': stopDate, 'branch': branch, 'page': 1, 'per_page': 100})

# Парсим в JSON
data=r.json()

#str = json.loads(r.text)
# N для хранения количества записей в JSON
N = len(data)

# Будущий список с именами авторов
names = []

# Формируем список авторов
for i in range(N):
    names.append(data[i]['commit']['author']['name'])
# На основе списка авторов names формируем словарь, в котором напротив каждого имени автора его количество коммитов
# Автор добавляется в словарь автоматически, если их еще нет, в ином случае количество его коммитов увеличивается на 1
d = dict() 
for c in names:
    d[c] = d.get(c,0) + 1
   
f=open("scrap.json","a",encoding='utf-8')
ss = json.dumps(data, indent=4, sort_keys=True)
f.write('Page 1\n\n')
f.write(ss)
# m - количество страниц в результате запроса
# 60 - ограничение на количество запросов для неавторизованного пользователя
m = 2
while data != [] and m < 61:
    data = []
    names = []
    # получаем следующую страницу
    r = requests.get('https://api.github.com/repos/django/django/commits', params={'since': startDate, 'until': stopDate, 'branch': branch, 'page': m, 'per_page': 100}, headers=headers)
    
    # добавляем к нашим результатам
    data = r.json()
    N = len(data)
    for i in range(N):
        names.append(data[i]['commit']['author']['name'])
    for c in names:
        d[c] = d.get(c,0) + 1
    f=open("scrap.json","a",encoding='utf-8')
    ss = json.dumps(data, indent=4, sort_keys=True)
    f.write('Page '+str(m)+'\n\n')
    f.write(ss)
    f.close()
    print('Проанализировано страниц: '+str(m),end="\r")
    m+=1
    # таймаут, чтобы не превысить количество запросов в секунду
    time.sleep(0.5) 
m -=1


# Сортируем авторов по количеству их коммитов, в убывающем порядке
# Получаем список, где каждый элемент в виде:
# номер. Имя_автора   количево_коммитов
k = 0
listofTuples = sorted(d.items(), reverse=True,  key=lambda x: x[1])
for elem in listofTuples :
    if k>=30:
        break
    print(f"{k+1:3}. {elem[0]:25} {elem[1]:6}")
    k+=1



