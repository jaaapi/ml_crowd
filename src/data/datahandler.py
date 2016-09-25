import logging
import pandas as pd

# init logging
log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__name__)


def analyze_data_structure(data, table_info):
    logger.info('column info: {col_info}'.format(col_info=table_info.columns))
    result = {}
    for col in data.columns:
        result[col] = create_column_struct(table_info.ix[col, 'type'], data[col])
    return result


def create_column_struct(type, values):
    if type == 'TEXT':
        result = {'type': type, 'min': None, 'max': None, 'distinct': values.unique()}
        result['distinct_cnt'] = result['distinct'].size
        return result
    elif type == 'FLOAT' or type == 'BIGINT':
        return {'type': type, 'min': values.min(), 'max': values.max(), 'distinct': None, 'distinct_cnt': None}
    else:
        logger.error('UNKOWN TYPE {type}'.format(type=type))
        return None

