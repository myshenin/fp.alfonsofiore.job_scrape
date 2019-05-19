import csv


class JobsDumper:
    def __init__(self, filename, delimiter=';'):
        self.filename = filename
        self.delimiter = delimiter

    def dump(self, jobs):
        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=self.delimiter)
            writer.writerow(['employer', 'job_title', 'link', 'salary', 'posted_date'])
            for job in jobs:
                writer.writerow([job['employer'], job['job_title'], job['link'], job['salary'], job['posted_date']])