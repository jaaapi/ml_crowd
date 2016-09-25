import logging
from sklearn import svm


# init logging
log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__name__)


def train_test_svm(X_train, y_train, X_test, y_test):
    clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    logger.info('SVM score : {}'.format(score))