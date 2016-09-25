from sklearn.cross_validation import train_test_split


def split_train_test(data, output, test_size):
    return train_test_split(
        data, output, test_size=test_size, random_state=42)
