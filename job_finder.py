import requests
from bs4 import BeautifulSoup


# class that return links to currently available jobs
class JobsFinder:
    job_links = []

    def __init__(self, URL):
        self.URL = URL

    def find_jobs(self):
        page = requests.get(self.URL)
        soup = BeautifulSoup(page.content, "html.parser")
        job_elements = soup.find_all('a', href=True, string="viac info")
        for job_link in job_elements:
            self.job_links.append(self.URL[:23] + job_link['href'][1:])
        return self.job_links
