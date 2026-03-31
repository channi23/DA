import numpy as np
from statsmodels.tsa.arima.model import ARIMA

# Sample time series data
data = np.array([10, 12, 13, 15, 18, 20, 22, 25])

# ARIMA model (p,d,q)
model = ARIMA(data, order=(1,1,1))
model_fit = model.fit()

# Forecast next values
forecast = model_fit.forecast(steps=2)

print("Forecast:", forecast)