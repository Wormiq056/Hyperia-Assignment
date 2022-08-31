import job_finder
import job_links_searcher
import json_writer


def main():
    URL = "https://www.hyperia.sk/kariera/"
    job_links = job_finder.JobsFinder(URL).find_jobs()
    job_data = job_links_searcher.JobDataFinder(job_links).find_data()
    json_writer.JsonWriter(job_data)


if __name__ == "__main__":
    main()
