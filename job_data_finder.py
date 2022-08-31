import requests
from bs4 import BeautifulSoup


class JobDataFinder():

    @staticmethod
    def _find_name(soup):
        return soup.find("h1").text

    @staticmethod
    def _find_additional_info(soup):
        data = soup.find_all(class_='col-md-4 icon')
        return data[0].text[21:], data[1].text[20:], data[2].text[21:]

    @staticmethod
    def _find_contact_email(soup):
        contact_element = soup.find('a', href=True, string="Reagovať na ponuku")
        return contact_element['href'][7:]

    @staticmethod
    def find_job_information(job_link):
        page = requests.get(job_link)
        soup = BeautifulSoup(page.content, "html.parser")
        name = JobDataFinder._find_name(soup)
        place, salary, contract_type = JobDataFinder._find_additional_info(soup)
        contact_email = JobDataFinder._find_contact_email(soup)
        return name, place, salary, contract_type, contact_email
