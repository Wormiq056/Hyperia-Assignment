import job_finder
import job_links_searcher
import util


def main():
    url = "https://www.hyperia.sk/kariera/"
    job_links = job_finder.JobsFinder(url).find_jobs()
    job_data = job_links_searcher.JobDataFinder(job_links).find_data()
    util.write_to_json(job_data)


if __name__ == "__main__":
    main()
