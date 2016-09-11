import logging
import pandas as pd

# init logging
log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__name__)


def load_from_database(connection, table_name, input_cols, output_col):
    if not output_col['name'] in input_cols:
        input_cols.append(output_col['name'])
    column_str = ', '.join(str(col) for col in input_cols)
    filter_vals = ', '.join('"{}"'.format(str(val)) for val in output_col['values'])
    result = load_values(connection, table_name, column_str, output_col['name'], filter_vals)
    logger.info('loaded value: {val}'.format(val=result.index))
    return result


def load_output_values(conn, table_name, output_col):
    query = 'SELECT  {col}, count({col}) FROM {tn} GROUP BY {col};' \
        .format(col=output_col['name'], tn=table_name)
    df = pd.read_sql_query(query, conn)
    return df


def load_values(conn, table_name, cols, filter_col, filter_vals):
    query = 'SELECT {cls} FROM {tn} WHERE {name} in ({val});' \
        .format(cls=cols, tn=table_name, name=filter_col, val=filter_vals)
    logger.info('created query: {}'.format(query))
    df = pd.read_sql_query(query, conn)
    return df


def get_table_info(connection, table_name):
    df = pd.read_sql_query('PRAGMA TABLE_INFO({})'.format(table_name), connection, 'name')
    return df