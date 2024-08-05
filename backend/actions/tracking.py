import requests
from bs4 import BeautifulSoup

class Suivi:
    def __init__(self, date, country, location, eventType, info):
        self.date = date
        self.country = country
        self.location = location
        self.eventType = eventType
        self.info = info

class DataFetcher:
    def __init__(self, barcode):
        self.barcode = barcode
        self.listSuivi = []
        self.loadingdone = False

    def getData(self):
        url = f'http://www.rapidposte.poste.tn/fr/Item_Events.asp?ItemId={self.barcode}&submit=Valider'
        response = requests.get(url)
        if response.status_code == 200:
            self.loadingdone = True
            el = BeautifulSoup(response.content, 'html.parser')
            # print(el.prettify())
            if len(el.find_all('table',id="200")) !=0 :
                infoTable = el.find_all('table',id="200")[0].find_all('tr')
                for i in range(2, len(infoTable)):
                    tds = infoTable[i].find_all('td')
                    s = Suivi(tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text)
                    # print(tds[0].text)
                    # print(tds[1].text)
                    # print(tds[2].text)
                    # print(tds[3].text)
                    # print(tds[4].text)
                    # print("---------")
                    self.listSuivi.append(s)
                return self.listSuivi
            else:
                return None
        else:
            print("Error while getting data. Can't access the page.")
            return None


# Example usage:
# fetcher = DataFetcher("RB345343406SG")
# data = fetcher.getData()
# print("result : ---------------------------")
# for row in data :
#     print(row.date + " - " + row.country + " - "+ row.location + " - "+ row.eventType + " - "+ row.info)
#     print("----")



