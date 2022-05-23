# Import the model
from sklearn.linear_model import LinearRegression

# Instanciate the model
model = LinearRegression()

# Define X and y
X = data.drop(columns=['target'])
y = data['target']

# Train the model on the data
model.fit(X, y)

'''The right thing to do before fitting your model is to scale your features
but we will see this in future classes

Exs.:

Robust:

Standardize:

MinMax:

'''
