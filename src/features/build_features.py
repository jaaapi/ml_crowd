import logging
import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel

# init logging
log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__name__)


def select_features(data, output):
    clf = ExtraTreesClassifier()
    logger.info('selecting features {}'.format(data.columns))
    fitted = clf.fit(data, output)
    model = SelectFromModel(fitted, prefit=True)
    x_new = model.transform(fitted)
    logger.info('old features {old}, new features {new}'.format(old=data, new=x_new))
