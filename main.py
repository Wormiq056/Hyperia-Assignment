import jobs_finder


def main():
    URL = "https://www.hyperia.sk/kariera/"
    job_links = jobs_finder.JobsFinder(URL).find_jobs()
    

if __name__ == "__main__":
    main()
