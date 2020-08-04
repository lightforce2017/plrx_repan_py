import requests
import json
import random

# TODO1: сделать в виде параметров командной строки
repoURL = "http://github.com/django/django"       #if is public 
#repoURL = "https://api.github.com/user"       #if is public 

# TODO3: добавить проверку формата вводимой даты с автоисправлением, если возможно
startDate = '2009-08-12'
stopDate = '2020-08-12'

branch = 'master'

user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]
url = 'https://httpbin.org/headers'

# TODO1: заготовка для командной строки
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

# TODO2: проверить количество коммитов для разных промежутков времени
params = repoURL, startDate, stopDate, branch
#https://github.com/django/django/graphs/contributors?from=2007-12-01&to=2010-10-28&type=c
#r = requests.get(repoURL+'/'+branch+'/graphs/contributors?from='+startDate+'&to='+stopDate+'&type=c')

user_agent = random.choice(user_agent_list)
#Set the headers 
headers = {'User-Agent': user_agent}
#Make the request
#r = requests.get(repoURL+'/contributors?branch='+branch+'&from='+startDate+'&to='+stopDate+'&type=c', headers=headers)
#r = requests.get(repoURL+'/contributors', headers=headers)
r = requests.get('https://api.github.com/repos/django/django/contributors?branch=master&from=2007-12-01&to=2010-10-28&type=c')

# TODO4: убрать из релиза
f= open("scrap.json","w",encoding='utf-8')

if r.status_code == 200:
    print('Success!')
    #commits = json.loads(r.content)
    #print(r.json())
    str = json.loads(r.text)
    #print(json.dumps(parsed, indent=4, sort_keys=True))
    ss = json.dumps(str, indent=4, sort_keys=True)
    #print(str[0]["login"]+' has '+str(str[0]["contributions"])+' commits.')
    k = 0
    userc = 'user'
    cmtsc = 'commits'
    print(f" {userc:23} {cmtsc:8}")
    while k < 30:
        user = str[k]["login"]
        cmts = str[k]["contributions"]
        print(f"{k+1:3} {user:20} {cmts:8}")
        k += 1
    #print(type(str[0]["login"]))
    f.write(ss)
    f.close()
    #start1 = str.find('div id="contributors')
    #start2 = str.find('ol class="contrib-data list-style-none',start1)
    #print(start2)
elif r.status_code == 404:
#TODO5: продумать надписи об ошибках
    print('Not Found.')
