import logging
import pandas as pd
import numpy as np
from sklearn import preprocessing

# init logging
log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__name__)


def preprocess(data, structure, output_name):
    new_data = pd.DataFrame(index=data.index, columns=data.columns)
    min_max_scaler = preprocessing.MinMaxScaler()
    imp = preprocessing.Imputer(missing_values='NaN',
                                strategy='mean',
                                axis=0)
    for col in data.columns:
        logger.info('preprocessing {}'.format(col))
        cur_struct = structure[col]
        if cur_struct['type'] == 'TEXT':
            tmp_data = label_text(data[col].values, structure[col])
            new_data[col] = encode_text_features(tmp_data)
        elif cur_struct['type'] == 'FLOAT' or cur_struct['type'] == 'BIGINT':
            new_data[col] = preprocess_number(data[col].values, imp, min_max_scaler)
            encode_text_features(new_data[col].values)
    return new_data


def label_text(values, col_structure):
    label_encoder = preprocessing.LabelEncoder()
    distinct = col_structure['distinct']
    # this seems the right way to replace None values, but doesn't work :(
    # distinct = np.where(distinct is None, '', distinct)
    # this gives a warning
    distinct[np.equal(distinct, None)] = ''
    np.where(distinct == np.array(None), '', distinct)
    label_encoder.fit(distinct)
    values[np.equal(values, None)] = ''
    new_values = label_encoder.transform(values)
    col_structure['encode_params'] = label_encoder.get_params()
    return new_values


def preprocess_number(values, imputer, scaler):
    new_values = values.astype(float)
    data_imputed = imputer.fit_transform(new_values.reshape(-1, 1))
    min_max_data = scaler.fit_transform(data_imputed)
    return min_max_data


def encode_text_features(data):
    encoder = preprocessing.OneHotEncoder(categorical_features='all',
                                          dtype=np.dtype(float),
                                          handle_unknown='error',
                                          n_values='auto',
                                          sparse=True,
                                          )
    new_data = encoder.fit_transform(data.reshape(-1, 1)).toarray()
    return new_data


def transform_output(values, mapping):
    new_vals = values.apply(lambda x: mapping[x])
    new_vals.astype(float)
    return new_vals

