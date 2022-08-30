import job_data_finder
import job_dataclass


class JobDataFinder:
    job_data = []
    data_finder = job_data_finder.JobDataFinder()

    def __init__(self, job_links):
        self.job_links = job_links

    def find_data(self):
        for job_link in self.job_links:
            self._link_data_finder(job_link)

    def _link_data_finder(self, job_link):
        job_information = self.data_finder.find_job_information(job_link)
