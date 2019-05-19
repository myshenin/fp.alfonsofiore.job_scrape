import functools


class EmailContentGenerator:
    def dump(self, jobs):
        def to_html(job):
            if type(job) is str:
                return job
            else:
                return f'{job["employer"]}<br/>' \
                    f'{job["job_title"]}<br/>' \
                    f'{job["link"]}<br/>' \
                    f'{job["salary"]}<br/>' \
                    f'{job["posted_date"]}<br/>' \
                    f'<br/><br/>'

        def assemble(x, y):
            return to_html(x) + to_html(y)

        return functools.reduce(assemble, jobs)
