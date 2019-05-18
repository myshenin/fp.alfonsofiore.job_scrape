from jobextractor import JobExtractor

URL = 'https://www.mycareersfuture.sg/search?search=product&salary=20000&sortBy=new_posting_date&page=0'
job_extractor = JobExtractor(URL)
job_extractor.start_driver()
job_extractor.load_page()
print(job_extractor.extract_data(job_extractor.filtered_posts(job_extractor.is_recent(['today', 'yesterday', '2 days']))))
job_extractor.close_driver()
