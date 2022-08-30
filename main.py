import job_finder
import job_links_searcher


def main():
    URL = "https://www.hyperia.sk/kariera/"
    job_links = job_finder.JobsFinder(URL).find_jobs()
    classes = job_links_searcher.JobDataFinder(job_links).find_data()


if __name__ == "__main__":
    main()
