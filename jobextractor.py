from time import sleep
import re
from random import randint
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from datetime import date, timedelta
from constants import Constants
from pyvirtualdisplay import Display


class JobExtractor:
    def __init__(self, url):
        self.url = url

    def start_driver(self):
        print('starting driver...')
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox()
        sleep(4)

    def close_driver(self):
        print('closing driver...')
        self.driver.quit()
        print('closed!')

    def load_page(self):
        with Display():
            self.driver.get(self.url)
        sleep(randint(4, 7))

    def is_recent(self, ages):
        def recent(element, _ages=ages):
            post_date = element.find_element_by_css_selector('[name="last_posted_date"]')
            include = False
            for age in _ages:
                include = include or (age in post_date.text)
            return include
        return recent

    def filtered_posts(self, filter_function):
        return list(filter(lambda element: filter_function(element), self.driver.find_elements_by_css_selector('.card.relative')))

    def extract_data(self, posts):
        def extract_from_post(post):
            post_data = {}
            post_data['employer'] = post.find_element_by_css_selector('[name = "company"]').text
            post_data['job_title'] = post.find_element_by_css_selector('[name="job_title"').text
            post_data['link'] = post.find_element_by_css_selector('.card.relative a').get_attribute('href')

            salary_type = post.find_element_by_css_selector('.salary_type').text
            if salary_type == 'Monthly':
                post_data['salary'] = f'from {post.find_element_by_css_selector(".salary_range").text.replace("to", " to ")}'
            elif salary_type == 'Annually':
                range_nums = re.findall(r'\d+', post.find_element_by_css_selector(".salary_range").text.replace(',', ''))
                post_data['salary'] = f'from ${(int(range_nums[0]) // 12):,} to ${(int(range_nums[1]) // 12):,} (originally posted from ${int(range_nums[0]):,} to ${int(range_nums[1]):,})'

            posted_date = post.find_element_by_css_selector('[name="last_posted_date"]').text
            if posted_date == 'today':
                post_data['posted_date'] = date.today()
            elif posted_date == 'yesterday':
                post_data['posted_date'] = date.today() - timedelta(days=1)
            else:
                days = int(re.findall(r'\d+', posted_date)[0])
                post_data['posted_date'] = date.today() - timedelta(days=days)
            post_data['posted_date'] = post_data['posted_date'].strftime(Constants.DATE_FORMAT.value)
            return post_data

        return list(map(lambda post: extract_from_post(post), posts))

    def set_url(self, url):
        self.url = url
