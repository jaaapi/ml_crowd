import logging
from sklearn.naive_bayes import GaussianNB

# init logging
log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__name__)


def train_test_svm(X_train, y_train, X_test, y_test):
    gnb = GaussianNB()
    y_pred = gnb.fit(X_train, y_train).predict(X_test)
    logger.info('size {}'.format(y_test.shape[0]))
    logger.info('result {}'.format(((y_test != y_pred).sum())/y_test.shape[0]))
