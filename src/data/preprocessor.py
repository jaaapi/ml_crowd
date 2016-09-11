import logging
import pandas as pd
from sklearn import preprocessing

# init logging
log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__name__)


def preprocess(data, structure, output_name):
    new_data = pd.DataFrame(index=data.index, columns=data.columns)
    min_max_scaler = preprocessing.MinMaxScaler()
    encoder = preprocessing.OneHotEncoder()
    imp = preprocessing.Imputer(missing_values='NaN',
            strategy='mean',
            axis=0)
    for col in data.columns:
        logger.info('preprocessing {}'.format(col))
        # skip processing the output column
        if col == output_name:
            new_data[col] = data[col]
        else:
            cur_struct = structure[col]
            new_col = preprocess_col(cur_struct['type'], data[col].values, structure[col], imp, min_max_scaler)
            new_data[col] = new_col
    return new_data


def preprocess_col(type, values, col_structure, imputer, scaler):
    if type == 'FLOAT' or type == 'BIGINT':
        new_values = values.astype(float)
        data_imputed = imputer.fit_transform(new_values.reshape(-1, 1))
        min_max_data = scaler.fit_transform(data_imputed)
        return min_max_data
    elif type == 'TEXT':
        label_encoder = preprocessing.LabelEncoder()
        label_encoder.fit(col_structure['distinct'])
        new_values = label_encoder.transform(values)
        col_structure['encode_params'] = label_encoder.get_params()
        return new_values


def transform_output(values, mapping):
    new_vals = values.apply(lambda x: mapping[x])
    new_vals.astype(float)
    return new_vals

