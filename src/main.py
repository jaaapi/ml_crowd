import logging
import os

import data.colselection as columns
import data.custom_transform as transformer
import data.datahandler as datahandler
import data.dataloader as dataloader
import data.preprocessor as preprocessor
import data.split_data as datasplitter
import features.build_features as features
from data.connection import Connection
import learners.bayes as bayes
# import learners.svm as svm

if __name__ == '__main__':
    # init logging
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    logger = logging.getLogger(__name__)
    # get environment variables
    data_path = os.environ.get('DATABASE_FILE')
    table_name = os.environ.get('TABLE_NAME')
    # determine data directory
    project_dir = os.path.join(os.path.dirname(__file__))
    logger.info('loading database from path {path}'.format(path=data_path))
    data_dir = os.path.join(project_dir, data_path)

    # load data
    output_col = columns.get_output_col()
    db = Connection(data_dir)
    table_info = dataloader.get_table_info(db.get_connection(), table_name)
    dataset = dataloader.load_from_database(db.get_connection(), table_name, columns.get_input_cols(),
                                            output_col)
    output = dataset[output_col['name']]
    input_data = dataset.drop(output_col['name'], 1)
    structure = datahandler.analyze_data_structure(input_data, table_info)

    # transform data
    transformer.transform_data(input_data, structure)
    data = preprocessor.preprocess(input_data, structure, output_col['name'])
    output_mapping = columns.get_output_mapping()
    output_transformed = preprocessor.transform_output(output, output_mapping)

    # select features
    data_trimmed = features.select_features(data, output_transformed)

    # split dataset and output to train and test set
    X_train, X_test, y_train, y_test = datasplitter.split_train_test(data_trimmed, output_transformed, 0.2)

    # train and score svm model
    bayes.train_test_svm(X_train, y_train, X_test, y_test)