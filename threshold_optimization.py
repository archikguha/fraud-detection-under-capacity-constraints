
import numpy as np

def precision_at_k(y_true, y_score, k):
    idx = np.argsort(y_score)[::-1][:k]
    return y_true.iloc[idx].mean()
