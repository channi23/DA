import numpy as np
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.arima.model import ARIMA

# Sample time series data
data = np.array([10, 12, 13, 15, 18, 20, 22, 25])

# -------- AR Model --------
ar_model = AutoReg(data, lags=2).fit()
print("AR Prediction:", ar_model.predict(start=6, end=7))

# -------- MA Model --------
ma_model = ARIMA(data, order=(0, 0, 2)).fit()
print("MA Prediction:", ma_model.predict(start=6, end=7))