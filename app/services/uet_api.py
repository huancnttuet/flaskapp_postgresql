from bs4 import BeautifulSoup
import requests


def find_token(htmlstr, type_token):
    _token = ''
    if type_token == 0:
        soup = BeautifulSoup(htmlstr, "lxml")
        for n in soup.findAll('input'):
            _token = n['value']
            return _token
    else:
        soup = BeautifulSoup(htmlstr, "lxml")
        for n in soup.findAll('input'):
            if n['id'] == 'myToken':
                _token = n['value']
                return _token


def set_cookie(cookies):
    token = ''
    session = ''
    for c in cookies:
        if c.name == 'XSRF-TOKEN':
            token = c.value
        if c.name == 'laravel_session':
            session = c.value
    cookies = 'XSRF-TOKEN={}; laravel_session={}'.format(token, session)
    return cookies


def login():
    url = 'http://112.137.129.30/viewgrade'
    r = requests.get(url)
    cookie = set_cookie(r.cookies)
    _token = find_token(r.text, 0)
    payload = {'_token': _token,
               'username': '17020781', 'password': '341997mok'}
    headers = {'Cookie': cookie}

    url2 = "http://112.137.129.30/viewgrade/submitLoginForm"

    a = requests.post(url2,
                      headers=headers, data=payload)

    cookie = set_cookie(a.cookies)
    _token = find_token(a.text, 1)
    return {'cookie': cookie, '_token': _token}


def get_score(term, type_education):

    data = login()
    url = 'http://112.137.129.30/viewgrade/home/getListSubjectOfTerm'

    headers = {'Cookie': data['cookie']}
    payload = {'_token': data['_token'],
               'term': term, 'type_education': type_education}
    r1 = requests.post(url, headers=headers, data=payload)

    return r1.json()


def get_list_year_term():
    data = login()
    url = 'http://112.137.129.30/viewgrade/home/getListYearTerm'

    headers = {'Cookie': data['cookie']}
    payload = {'_token': data['_token']}
    r = requests.post(url, headers=headers, data=payload)
    return r.json()


def get_list_term(year):
    data = login()
    url = 'http://112.137.129.30/viewgrade/home/getListTerm'

    headers = {'Cookie': data['cookie']}
    payload = {'_token': data['_token'], 'year': year}
    r = requests.post(url, headers=headers, data=payload)
    return r.json()


def search(text, term, type_education):
    data = login()
    url = 'http://112.137.129.30/viewgrade/home/getSearchWithTerm'

    headers = {'Cookie': data['cookie']}
    payload = {'_token': data['_token'], 'idterm': term,
               'input': text, 'type_education': type_education}
    r = requests.post(url, headers=headers, data=payload)
    return r.json()


def get_hint_input(text):
    data = login()
    url = 'http://112.137.129.30/viewgrade/home/getHintInput'

    headers = {'Cookie': data['cookie']}
    payload = {'_token': data['_token'], 'idterm': -1,
               'input': text}
    r = requests.post(url, headers=headers, data=payload)
    return r.json()


def quick_search(text):
    data = login()
    url = 'http://112.137.129.30/viewgrade/home/getResultSearch'

    headers = {'Cookie': data['cookie']}
    payload = {'_token': data['_token'],
               'input': text}
    r = requests.post(url, headers=headers, data=payload)
    return r.json()
