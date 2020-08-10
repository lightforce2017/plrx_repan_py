import requests
from datetime import date
import time
import sys

defBranch = 'master'

##################################################################################
#                               Validate URL
##################################################################################

# According to the form validation messages on Create repository page,
# Github repo's name should include alphanumeric symbols and '-', '_', '.'
def isValidRepo(repo):
    return ''.join(c for c in repo if  c not in '-_.').isalpha()

# Rules got from https://github.com/shinnn/github-username-regex:
# According to the form validation messages on Join Github page,
# + Github username may only contain alphanumeric characters or hyphens.
# + Github username cannot have multiple consecutive hyphens.
# + Github username cannot begin or end with a hyphen.
# + Maximum is 39 characters.
def isValidUser(user):
    alpha = ''.join(user.split('-')).isalpha()
    hyphens = user.find('--')==-1
    behyp = user.find('-')!=0 and user.find('-')!=len(user)-1
    maxlen = len(user)<=39
    return alpha and hyphens and behyp and maxlen

def isValidRepoURL(repoURL):
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
        return isValidRepo(repo) and isValidUser(user)

# Transform repoURL to request format, eg
# http://github.com/usr/rep
# to
# https://api.github.com/repos/usr/rep/commits
def validateRepoURL(repo):
    data = repo.split('github.com/')[1].split('/')
    usr = data[0]
    rep = data[1]
    return 'https://api.github.com/repos/'+usr+'/'+rep+'/commits'


##################################################################################
#                               Validate date
##################################################################################

# if the date is valid and is in one of three types:
# 1. YYYY-MM-DD
# 2. DD-MM-YYYY 
# 3. MMM-DD-YYYY
def dateType(date):
    sp = date.split('-')
    if isYear(sp[0]) and isMonth(sp[1]) and isDay(sp[2]):
        return 1
    if isDay(sp[0]) and isMonth(sp[1]) and isYear(sp[2]):
        return 2
    if isMonth(sp[0]) and isDay(sp[1]) and isYear(sp[2]):
        return 3
    return 0

# make the date valid for api filter: YYYY-MM-DD
def validateDate(date):
    vd = dateType(date)
    if vd > 0:
        if vd == 1:
            return date
        elif vd == 2:
            ds = date.split('-')
            return ds[2]+'-'+ds[1]+'-'+ds[0]
        else:
            ds = date.split('-')
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            return ds[2]+'-'+str(months.index(ds[0])+1)+'-'+ds[1]
    else:
        print('Wrong date. Input date in one of possible formats: YYYY-MM-DD, or DD-MM-YYYY or MMM-DD-YYYY (eg 2014-12-22, 22-12-2014 or Dec-22-2014)')
        return ''

# is the number a day
def isDay(d):
    if 1 <= len(d) <= 2 and d.isdigit():
        return 1 <= int(d) <= 31

# is the number/string a month
def isMonth(m):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    if len(n) == 3 and m in months:
        return True
    elif 1 <= len(m) <= 2 and m.isdigit():
        return 1 <= int(m) <= 12

# is the number a year
# Github was founded in 2008
def isYear(y):
    if len(y) == 4 and y.isdigit():
        return 2008 <= int(y) <= 2050
    else:
        return False

##################################################################################
#                               Validate branch
##################################################################################
def isValidBranch(br):
    return ''.join(c for c in br if  c not in '-_./').isalpha()

##################################################################################
#                               Count commits
##################################################################################
        
def countCommits(repoURL, startDate, stopDate, branch):
    # startDate - start of period
    # stopDate - end of period
    # branch - branch for search within ('master' bu deafault)
    
    # Starting from the first page, results per page 100
    prm = {'branch': branch, 'page': 1, 'per_page': 100}
    if startDate == '':
        if stopDate != '':
            prm.update({'until': stopDate})
    elif if stopDate == '':
        prm.update({'since': startDate})
    else:
        prm.update({'since': startDate, 'until': stopDate})
    r = requests.get(repoURL, params=prm)
    data=r.json()

    # N to store the number of records in JSON
    N = len(data)

    # Future list with author names
    names = []

    # Make a list of authors
    for i in range(N):
        names.append(data[i]['commit']['author']['name'])
        
    # Based on the list of authors names, we form a dictionary in which, opposite each author name, its number of commits
    # The author is added to the dictionary automatically if they do not exist yet, 
    # otherwise the number of his commits increases by 1
    d = dict() 
    for c in names:
        d[c] = d.get(c,0) + 1

    # m stores the number of pages as a result of the request
    m = 2
    
    # 60 is a limit on the number of requests for an unauthorized user
    while data != [] and m < 61:
        # reset the lists for the next check and save
        data = []
        names = []
        
        # get the next page
        prm.update({'page': m})
        r = requests.get(repoURL, params=prm)
        
        # add to the results
        data = r.json()
        N = len(data)
        for i in range(N):
            names.append(data[i]['commit']['author']['name'])
        for c in names:
            d[c] = d.get(c,0) + 1
        
        # little message for user for not to get bored
        print('Pages analyzed: '+str(m),end="\r")
        m+=1
        
        # timeout so as not to exceed the number of requests per second
        time.sleep(0.5) 

    # Sort authors by the number of their commits, in descending order:
    # No. Author   commits_count
    return sorted(d.items(), reverse=True,  key=lambda x: x[1])
        
##################################################################################
#                               MAIN PROGRAM
##################################################################################      

# Arguments of command line:
#repoURL    :   URL address of a public repository
#startDate  :   date of the start of period
#stopDate   :   date of the end of period
#branch     :   name of the branch, deafult is 'master'
#======   Format   =======
# repoURL* start stop branch
# *required args
#
# Flags (not necessary):
# -f    only start date
# -l    only stop date
# Eg:
# http://github.com/django/django -f 2014-12-22 stable/2.1.x
# will search all commits at http://github.com/django/django from Dec/22/2014 in the 'stable/2.1.x' branch
# http://github.com/django/django -l 2016-12-22
# will search all commits at http://github.com/django/django before Dec/22/2016 in the 'master' branch
# http://github.com/django/django
# will search all commits at http://github.com/django/django at all time in the 'master' branch
if __name__ == '__main__':
    if len(sys.argv) == 1:
        ms = '''Don't forget about args: 
python repan.py repoURL* start stop branch
where * is required arg
-------------------------------
Flags (not necessary):
 -f    only start date
 -l    only stop date
-------------------------------
 Eg:
http://github.com/django/django -f 2014-12-22 stable/2.1.x
will search all commits at http://github.com/django/django from Dec/22/2014 in the 'stable/2.1.x' branch
    
http://github.com/django/django -l 2016-12-22
will search all commits at http://github.com/django/django before Dec/22/2016 in the 'master' branch (by default)

http://github.com/django/django
will search all commits at http://github.com/django/django at all time in the 'master' branch (by default)
        '''
        print(ms)
    else:
        repoURL = ''
        startDate = '' 
        stopDate = '' 
        branch = 'master'
        try:
            repoURL = sys.argv[1]
            if isValidRepoURL(repoURL):
                repoURL = validateRepoURL(repoURL)
            if len(sys.argv) == 3:
                str = sys.argv[2]
                if isValidBranch(str):
                    branch = str
                else:
                    print('Invalid branch name.')
                    sys.exit(1)
            elif len(sys.argv) >= 4:
                today = date.today()
                dn = today.strftime("%Y-%m-%d")
                # -f startDate
                if sys.agrv[3] == '-f': 
                    startDate = validateDate(sys.agrv[4])
                    if startDate == '':
                        sys.exit(1)
                    elif startDate > dn:
                        print('Nobody knows what awaits us in the future.\nERROR! Start date must be earlier than today.')
                        sys.exit(1)
                # -l stopDate
                elif sys.agrv[3] == '-l':    
                    stopDate = validateDate(sys.agrv[4])
                    if stopDate == '':
                        sys.exit(1)
                    elif stopDate > dn:
                        print('It is not known how many commits there will be until '+stopDate+'. I will count until today, i.e. until '+dn+', okay?')
                        stopDate = dn
                # startDate stopDate
                else:
                    startDate = validateDate(sys.agrv[3])
                    if startDate == '':
                        sys.exit(1)
                    elif startDate > dn:
                        print('Nobody knows what awaits us in the future.\nERROR! Start date must be earlier than today.')
                        sys.exit(1)
                    stopDate = validateDate(sys.agrv[4])
                    if stopDate == '':
                        sys.exit(1)
                    elif stopDate > dn:
                        print('It is not known how many commits there will be until '+stopDate+'. I will count until today, i.e. until '+dn+', okay?')
                        stopDate = dn
                    if startDate > stopDate:
                        print('I can\'t count in negative space-time.\nCheck the dates, you wrote the start date: '+startDate+', and the end date: '+stopDate+'.\nI cannot work in such conditions. Try again.')
                        sys.exit(1)
                    elif startDate == stopDate:
                        print('Oh, I see you wanted to check the number of commits in one day, '+startDate+'. Now let\'s count them.')
                
            if len(sys.argv) == 5:
                # branch
                str = sys.argv[5]
                if isValidBranch(str):
                    branch = str
                else:
                    print('Invalid branch name.')
                    sys.exit(1)
            
        except:
            print('ERROR')
            sys.exit(1)
    
        listofTuples = countCommits(repoURL, startDate, stopDate, branch)
        k = 0
        print(f"{Num:3}. {Author:25} {Commits:6}")
        for elem in listofTuples :
            if k>=30:
                break
            print(f"{k+1:3}. {elem[0]:25} {elem[1]:6}")
            k+=1

        






