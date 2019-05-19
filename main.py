from jobextractor import JobExtractor
from jobsdumper import JobsDumper
from constants import Constants
from emailcontent import EmailContentGenerator
from emailsender import EmailSender

page_number = 0

job_extractor = JobExtractor(f'{Constants.URL_TEMPLATE.value}&page={page_number}')
job_extractor.start_driver()


job_extractor.load_page()
page_posts = job_extractor.extract_data(
    job_extractor.filtered_posts(job_extractor.is_recent(['today', 'yesterday', '2 days', '3 days'])))
total_posts = list(page_posts)

while len(page_posts) != 0:
    page_number += 1
    job_extractor.set_url(f'{Constants.URL_TEMPLATE.value}&page={page_number}')
    job_extractor.load_page()
    page_posts = job_extractor.extract_data(
        job_extractor.filtered_posts(job_extractor.is_recent(['today', 'yesterday', '2 days', '3 days'])))
    total_posts += page_posts

jobs_dumper = JobsDumper('jobs.csv')
jobs_dumper.dump(total_posts)

email_generator = EmailContentGenerator()
email = email_generator.dump(total_posts)

sender = EmailSender()
sender.send(email)

job_extractor.close_driver()
