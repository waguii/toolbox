from sklearn.model_selection import cross_validate

# Instantiate model
model = LinearRegression() #or any other model

# 5-Fold Cross validate model
cv_results = cross_validate(model, X, y, cv=5)

# Scores
cv_results['test_score']

# Mean of scores
cv_results['test_score'].mean()

'''
Here again your features should be scaleted before the cross validation

'''
