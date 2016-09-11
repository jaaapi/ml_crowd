import logging
import pandas as pd

# init logging
log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__name__)


def transform_data(data, structure):
    data['emp_length'] = data['emp_length'].apply(transform_emp_length_item)
    data['emp_length'].astype(float)
    structure['emp_length']['type'] = 'FLOAT'
    data['term'] = data['term'].str.replace(' months', '')
    data['term'].astype(float)
    structure['term']['type'] = 'FLOAT'


def transform_emp_length_item(emp_length):
    if emp_length == '< 1 year':
        return 0
    elif emp_length == '1 year':
        return 1
    elif emp_length == '2 years':
        return 2
    elif emp_length == '3 years':
        return 3
    elif emp_length == '4 years':
        return 4
    elif emp_length == '5 years':
        return 5
    elif emp_length == '6 years':
        return 6
    elif emp_length == '7 years':
        return 7
    elif emp_length == '8 years':
        return 8
    elif emp_length == '9 years':
        return 9
    elif emp_length == '10+ years':
        return 15
    else:
        return None

