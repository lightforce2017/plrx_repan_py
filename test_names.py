from repan import isValidRepo, isValidUser, isValidRepoURL, validateRepoURL, isValidBranch

# According to the form validation messages on Create repository page,
# Github repo's name should include alphanumeric symbols and '-', '_', '.'
def test_rname():
    assert isValidRepo('repo123') == True
 
def test_rname2():
    assert isValidRepo('repo-123') == True

def test_rname3():
    assert isValidRepo('repo.123') == True

def test_rnamef():
    assert isValidRepo('repo#123') == False

def test_rnamef2():
    assert isValidRepo('репо') == False

def test_rnamef3():
    assert isValidRepo('format C:') == False

def test_rnamef4():
    assert isValidRepo('repo/123') == False

# Rules got from https://github.com/shinnn/github-username-regex:
# According to the form validation messages on Join Github page,
# + Github username may only contain alphanumeric characters or hyphens.
# + Github username cannot have multiple consecutive hyphens.
# + Github username cannot begin or end with a hyphen.
# + Maximum is 39 characters.    
def test_uname():
    assert isValidUser('user123') == True

def test_uname2():
    assert isValidUser('user-123') == True

def test_unamef():
    assert isValidUser('user--123') == False
    
def test_unamef1():
    assert isValidUser('-user123') == False

def test_unamef2():
    assert isValidUser('user123-') == False

def test_unamef3():
    assert isValidUser('-user123-') == False

def test_unamef3():
    assert isValidUser('this-is-a-super-creative-name-for-github-user') == False

def test_unamef4():
    assert isValidUser('format C:') == False

# The address should be like this: http://github.com/author/repo 
# or this: https://github.com/author/repo 
# or this: github.com/author/repo 
def test_rurl():
    assert isValidRepoURL('http://github.com/author/repo') == True

def test_rurl2():
    assert isValidRepoURL('https://github.com/author/repo') == True
    
def test_rurl3():
    assert isValidRepoURL('github.com/author/repo') == True

def test_rurl4():
    assert isValidRepoURL('http://github.com/author/repo.') == True

def test_rurl5():
    assert isValidRepoURL('htp://github.com/author/repo') == True

def test_rurl6():
    assert isValidRepoURL('ttp://github.com/author/repo') == True

def test_rurl7():
    assert isValidRepoURL('tp://github.com/author/repo') == True

def test_rurl8():
    assert isValidRepoURL('p://github.com/author/repo') == True

def test_rurl9():
    assert isValidRepoURL('://github.com/author/repo') == True
 
def test_rurl10():
    assert isValidRepoURL('//github.com/author/repo') == True
 
def test_rurl11():
    assert isValidRepoURL('/github.com/author/repo') == True

def test_rurlf():
    assert isValidRepoURL('author/repo') == False

    
def test_rurlf10():
    assert isValidRepoURL('format C:') == False

# Transform repoURL to request format, eg
# http://github.com/usr/rep
# to
# https://api.github.com/repos/usr/rep/commits
def test_vrepo():
    assert validateRepoURL('http://github.com/author/repo') == 'https://api.github.com/repos/author/repo/commits'
    
# Github branch name should include alphanumeric symbols and '-', '_', '.', '/'
def test_bname():
    assert isValidBranch('branch123') == True
 
def test_bname2():
    assert isValidBranch('branch-123') == True

def test_bname3():
    assert isValidBranch('branch.123') == True

def test_bname4():
    assert isValidBranch('branch/123') == True

def test_bnamef():
    assert isValidBranch('branch#123') == False

def test_bnamef2():
    assert isValidBranch('ветка') == False

def test_bnamef3():
    assert isValidBranch('format C:') == False

