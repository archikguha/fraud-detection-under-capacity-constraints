
from sklearn.ensemble import GradientBoostingClassifier

def train_model(X, y):
    model = GradientBoostingClassifier()
    model.fit(X, y)
    return model
