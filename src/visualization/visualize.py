# -*- coding: utf-8 -*-
import os
import logging
import pandas as pd
import matplotlib.pyplot as plt
from subprocess import check_output

# @click.command()
# @click.argument('input_filepath', type=click.Path(exists=True))
# @click.argument('output_filepath', type=click.Path())
def main():
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    data_path = os.environ.get('CSV_FILE')
    logger.info('database file: %s', data_path)
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
    df_data_dir = os.path.join(project_dir, data_path)
    logger.info('loading data from: %s', df_data_dir)
    df_data = pd.read_csv(df_data_dir, low_memory=False)
    logger.info('loaded data, info: %s', df_data.info())
    group_and_plot_data(df_data, 'addr_state')

def group_and_plot_data(data, group):
    df_group = data.groupby(group, as_index=False)['id'].count()
    df_group.sort_values(['id'], ascending=[True], inplace=True)
    df_group = df_group.reset_index(drop=True)
    plot(df_group)

def plot(data):
    plt.bar(data.index, data.id / 100000)
    plt.xticks(data.index, data.addr_state)
    N = 3
    params = plt.gcf()
    plSize = params.get_size_inches()
    params.set_size_inches((plSize[0] * N, plSize[1] * N))
    plt.show()


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)


    # not used in this stub but often useful for finding various files

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables

    main()
