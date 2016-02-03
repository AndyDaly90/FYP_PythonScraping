from __future__ import print_function
import urllib
from bs4 import BeautifulSoup

make = "audi"
model = "a4"
site = "cbg"

# make = raw_input("Enter car make: ")
# model = raw_input("Enter car model: ")
#  = raw_input("Enter web site to scrape: ")

min_year = "2012"


def get_car_data(car_make, car_model, car_site):
    print(car_make, car_model)


def strip_html_tags(htmlTxt):
    if htmlTxt is None:
        return None
    else:
        return ''.join(BeautifulSoup(htmlTxt).findAll(text=True))


if site.__contains__("cbg"):
    htmlFile = urllib.urlopen("http://www.cbg.ie/used_cars/" + make + "/" + model + "/all/0/0/" + min_year)
    htmlText = htmlFile.read()

    newFile = open("html/" + make + model + site + "RAW_HTML.txt", "w+")
    newFile.write(htmlText)

    newFile = open("html/" + make + model + site + "RAW_HTML.txt", "r")
    newFile2 = open("html/" + make + model + site + "REFINED_HTML.txt", "w+")

    soup = BeautifulSoup(newFile, 'html.parser')
    newFile.close()
    tag = soup.find_all('div', {'class': 'ads_txt'})
    for info in tag:
        if len(info.attrs) >= 1:
            newFile2 = open("html/" + make + model + site + "REFINED_HTML.txt", "a")
            newFile2.write(str(info.contents[1]))
            newFile2.write(str(info.contents[3]))
        else:
            print("No Data")
    newFile.close()
    newFile2.close()
else:
    print("Error")


def main():
    clean_file = open("html/" + make + model + site + "REFINED_HTML.txt", "r+")
    a = strip_html_tags(clean_file)
    print(a)
    clean_file.close()
#jhgfds
if __name__ == '__main__':
    main()