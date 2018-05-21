""" collects countries available for get query """
import xml.etree.ElementTree as ET
import pickle
import requests


def get_result(day, month, year):
    """ returns dict of country names/country id based on api """
    if int(day) < 10:
        day = "0{}".format(day)
    if int(month) < 10:
        month = "0{}".format(month)
    get_xml = requests.get(
        'http://www.cbr.ru/scripts/XML_daily.asp?date_req=\
        {}/{}/{}'.format(day, month, year)
    )
    elems = {}
    tree = ET.fromstring(get_xml.content)
    for element in tree:
        el_id = element.items()[0][1]
        name = element.find("./Name").text
        elems[name] = el_id
    return elems

if __name__ == '__main__':
    with open("countries.txt", "wb") as out:
        C = get_result(20, 5, 2018)
        pickle.dump(C, out)
