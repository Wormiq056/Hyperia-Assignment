import requests
from bs4 import BeautifulSoup


class JobsFinder:
    """
    class that returns available job links
    """
    job_links = []

    def __init__(self, url: str):
        self.url = url

    def find_jobs(self) -> list:
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        job_elements = soup.find_all('a', href=True, string="viac info")
        for job_link in job_elements:
            self.job_links.append(self.url[:23] + job_link['href'][1:])
        return self.job_links
