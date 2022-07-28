import numpy as np


def calculate(ls):

    if len(ls) < 9:
        raise ValueError("List must contain nine numbers.")

    mat = np.array(ls).reshape(3, 3)

    mean = [np.mean(mat, axis=0).tolist(), np.mean(mat, axis=1).tolist(), np.mean(mat.flatten())]
    variance = [np.var(mat, axis=0).tolist(), np.var(mat, axis=1).tolist(), np.var(mat.flatten())]
    std = [np.std(mat, axis=0).tolist(), np.std(mat, axis=1).tolist(), np.std(mat.flatten())]
    maxi = [np.max(mat, axis=0).tolist(), np.max(mat, axis=1).tolist(), np.max(mat.flatten())]
    mini = [np.min(mat, axis=0).tolist(), np.min(mat, axis=1).tolist(), np.min(mat.flatten())]
    sumi = [np.sum(mat, axis=0).tolist(), np.sum(mat, axis=1).tolist(), np.sum(mat.flatten())]

    calculations = {"mean": mean,
                    "variance": variance,
                    "standard deviation": std,
                    "max": maxi,
                    "min": mini,
                    "sum": sumi
                    }

    return calculations



