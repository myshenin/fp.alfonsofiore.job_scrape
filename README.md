# fp.alfonsofiore.job_scrape
to run on pythonanywhere
````
mkvirtualenv venv --python=python3.6
pip install -r requirments.txt
xvfb-run -a python3.6 main.py --sendgrid-key <the key>
````
to run locally
````
pip install -r requirments.txt
python main.py  --sendgrid-key <the key>
````