import requests
from bs4 import BeautifulSoup


# class that return links to currently available jobs
class JobsFinder:
    def __init__(self, URL):
        self.URL = URL

    def find_jobs(self):
        job_links = []
        page = requests.get(self.URL)
        soup = BeautifulSoup(page.content, "html.parser")
        job_elements = soup.find_all('a', href=True, string="viac info")
        for job_link in job_elements:
            job_links.append(job_link['href'])
        return job_links
