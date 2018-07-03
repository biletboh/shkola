# The Ukrainian Saterday School in Warshaw 

This repository contains the source for a website of The Ukrainian Saterday School in Warshaw. It contains a blog and information about teachers developed with Django.

## The website
https://uaszkolawaw.pl/

### Prerequisites

To run the website you have to install anaconda/miniconda and set up virtual environment: https://conda.io/docs/install/quick.html 

### Configuring 

0. Set up virtual environment: `conda create --name virtenv python=3.6`
1. Activate virtual environment: `source activate virtenv`
2. Install requirements: `pip install -r requirements.txt`
3. Migrate `python manage.py migrate`
4. Configure translations for existing languages. For example: `python manage.py compilemessages -l en`
