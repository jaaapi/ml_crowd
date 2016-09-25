import logging
import pandas as pd
import numpy as np
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel

# init logging
log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__name__)


def select_features(data, output):
    clf = ExtraTreesClassifier()
    fitted = clf.fit(data, output)
    model = SelectFromModel(fitted, prefit=True)
    x_new = model.transform(data)
    feature_importance = sort_importances(data.columns, clf)
    logger.info('importances {}'.format(feature_importance))
    logger.info('old features {old}, new features {new}'.format(old=data.shape, new=x_new.shape))
    return x_new

def sort_importances(columns, clf):
    importances  = clf.feature_importances_
    indices = np.argsort(importances)[::-1]
    logger.info("Feature ranking:")
    for f in range(columns.shape[0]):
        logger.info("{no}. feature {name} - {score})".format(no=f + 1, name=columns[indices[f]], score=importances[indices[f]]))
    return columns[indices]

