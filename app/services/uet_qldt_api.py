import requests
from bs4 import BeautifulSoup


def get_list_of_term(term_id, page_size, page):
    url = "https://112.137.129.87/qldt/"
    payload = {
        "ajax": "sinhvien-lmh-grid",
        "pageSize": page_size,
        "SinhvienLmh[term_id]": term_id,
        "r": "sinhvienLmh/admin",
        "SinhvienLmh_page": page,
    }
    r = requests.get(url, params=payload, verify=False)

    soup = BeautifulSoup(r.text, "lxml")
    n = soup.findAll("tbody")
    table_data = [[cell.text for cell in row("td")] for row in n[0]("tr")]

    return table_data


def get_tkb_of_term(term_id):
    url = "http://112.137.129.115/tkb/listbylist.php"
    payload = {"slt_namhoc": term_id}
    r = requests.post(url, params=payload, verify=False)
    soup = BeautifulSoup(r.text, "lxml")
    n = soup.findAll("table")
    tr = n[3]("tr")
    tr.pop(0)
    table_data = [[cell.text for cell in row("td")] for row in tr]
    return table_data


def get_exam_time(mssv):
    url = "https://112.137.129.87/congdaotao/module/dsthi/index.php"
    params = {"r": "lopmonhoc/napmonthi"}
    payload = {"keysearch": mssv}
    r = requests.post(url, params=params, data=payload, verify=False)

    soup = BeautifulSoup(r.text, "lxml")
    n = soup.findAll("tbody")
    table_data = [[cell.text for cell in row("td")] for row in n[0]("tr")]
    return table_data
