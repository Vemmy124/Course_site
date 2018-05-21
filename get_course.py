""" taking courses for rubles from CB api """
import xml.etree.ElementTree as ET
import requests


def get_result(code, day, month, year):
    """ getting course for some date """
    if int(day) < 10:
        day = "0{}".format(day)
    if int(month) < 10:
        month = "0{}".format(month)
    get_xml = requests.get(
        'http://www.cbr.ru/scripts/XML_daily.asp?date_req=\
        {}/{}/{}'.format(day, month, year)
    )
    tree = ET.fromstring(get_xml.content)
    valute = tree.find("./*[@ID='{}']".format(code))
    if not valute:
        raise ValueError
    charcode = valute.find("./CharCode")
    course = valute.find("./Value")
    nominal = valute.find("./Nominal")
    return course.text.replace(',', '.'), nominal.text, charcode.text
