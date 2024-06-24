import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample data
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([1, 2, 1.3, 3.75, 2.25, 6, 5.5, 6.3, 8.8, 8.5])

# Linear Regression
linear_model = LinearRegression()
linear_model.fit(x.reshape(-1, 1), y)
y_pred_linear = linear_model.predict(x.reshape(-1, 1))

# Segmented Least Squares
# Defining the breakpoints
breakpoints = [4, 7]
segments = np.split(x, np.searchsorted(x, breakpoints))

# Fit separate linear models to each segment
models = []
y_pred_segmented = np.empty_like(y)
start_idx = 0
for segment in segments:
    end_idx = start_idx + len(segment)
    model = LinearRegression()
    model.fit(segment.reshape(-1, 1), y[start_idx:end_idx])
    y_pred_segmented[start_idx:end_idx] = model.predict(segment.reshape(-1, 1))
    models.append(model)
    start_idx = end_idx

# Plotting the results
plt.scatter(x, y, color='black', label='Data')
plt.plot(x, y_pred_linear, color='blue', label='Linear Regression')
plt.plot(x, y_pred_segmented, color='red', linestyle='--', label='Segmented Least Squares')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression vs. Segmented Least Squares')
plt.show()
