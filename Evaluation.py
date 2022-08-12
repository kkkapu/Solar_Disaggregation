import numpy as np


def model_evaluation(data):
    SSR_model = sum(
        (
            np.array(data.prediction).reshape(data.shape[0], 1)
            - np.array(data.solar).reshape(data.shape[0], 1)
        )
        ** 2
    )
    MSE = SSR_model / data.shape[0]
    T = len(data)
    top = sum(
        abs(
            np.array(data.prediction).reshape(data.shape[0], 1)
            - np.array(data.solar).reshape(data.shape[0], 1)
        )
    )
    bottom = sum([abs(i - j) for i, j in zip(data.solar, data.solar[1:])])
    MASE = (T - 1) / T * top / bottom
    top = np.sqrt(
        sum(
            (
                np.array(data.prediction).reshape(data.shape[0], 1)
                - np.array(data.solar).reshape(data.shape[0], 1)
            )
            ** 2
        )
        / T
    )
    bottom = data.solar.mean()
    CV = top / bottom

    return MSE, MASE, CV
