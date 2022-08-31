import job_dataclass
import requests
from bs4 import BeautifulSoup


class JobDataFinder:
    job_data = []
    """
    class which searches all given links and extracts job information
    """

    def __init__(self, job_links: list):
        self.job_links = job_links

    def find_data(self) -> list:
        for job_link in self.job_links:
            self._link_data_finder(job_link)
        return self.job_data

    def _link_data_finder(self, job_link: str):
        name, place, salary, contract_type, contact_email = self._find_job_information(job_link)
        self.job_data.append(job_dataclass.JobData(name, place, salary, contract_type, contact_email))

    def _find_name(self, soup: BeautifulSoup) -> str:
        return soup.find("h1").text

    def _find_additional_info(self, soup: BeautifulSoup) -> tuple:
        data = soup.find_all(class_='col-md-4 icon')
        return data[0].text[21:], data[1].text[20:], data[2].text[21:]

    def _find_contact_email(self, soup: BeautifulSoup) -> str:
        contact_element = soup.find('a', href=True, string="Reagovať na ponuku")
        return contact_element['href'][7:]

    def _find_job_information(self, job_link: str):
        page = requests.get(job_link)
        soup = BeautifulSoup(page.content, "html.parser")
        name = self._find_name(soup)
        place, salary, contract_type = self._find_additional_info(soup)
        contact_email = self._find_contact_email(soup)
        return name, place, salary, contract_type, contact_email
