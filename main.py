# Data set for life expectancy over the years
data_points = [
    (2000, 72.5),
    (2001, 73.1),
    (2002, 73.8),
    (2003, 74.2),
    (2004, 74.7),
    (2005, 75.3),
    (2006, 75.9),
    (2007, 76.5),
    (2008, 76.9),
    (2009, 77.4),
    (2010, 78.0),
    (2011, 78.5),
    (2012, 79.0),
    (2013, 79.5),
    (2014, 80.0),
    (2015, 80.5),
    (2016, 81.0),
    (2017, 81.5),
    (2018, 82.0),
    (2019, 82.5)
]

# Function to calculate the mean of a list of numbers
def calculate_mean(data):
    return sum(data) / len(data)

# Function to calculate the regression coefficients (slope and intercept)
def calculate_regression_coefficients(data_points):
    # Separate the data points into x and y lists
    x_values = [point[0] for point in data_points]
    y_values = [point[1] for point in data_points]
    
    # Calculate means of x and y
    x_mean = calculate_mean(x_values)
    y_mean = calculate_mean(y_values)
    
    # Calculate the slope (m) using the formula
    numerator = sum((x - x_mean) * (y - y_mean) for x, y in data_points)
    denominator = sum((x - x_mean) ** 2 for x in x_values)
    slope = numerator / denominator
    
    # Calculate the intercept (b) using the formula
    intercept = y_mean - (slope * x_mean)
    
    return slope, intercept

# Function to make predictions using the linear regression model
def make_predictions(data_points, slope, intercept):
    # Predict y values for the corresponding x values in the data_points
    predictions = [(x, slope * x + intercept) for x, _ in data_points]
    return predictions

# Main program
# Calculate the regression coefficients
slope, intercept = calculate_regression_coefficients(data_points)

# Print the regression coefficients
print(f"Regression Coefficients:\nSlope (m): {slope}\nIntercept (b): {intercept}")

# Prompt the user to enter a new x value for prediction
new_x_value = int(input("\nEnter a new year for prediction: "))
predicted_y = slope * new_x_value + intercept

# Display the predicted y value
print(f"\nPredicted life expectancy for the year {new_x_value}: {predicted_y:.2f}")
