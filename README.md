# Airbnb
A machine learning model that provides the price of vacation homes, whether short or long stay for Airbnb customers, leveraging linear regression algorithm to predict total package of the homes. Airbnb, Inc. is an American San Francisco-based company operating an online marketplace for short- and long-term homestays and experiences. The company acts as a broker and charges a commission from each booking.

# Aim and Objectives of the Project
To build a foundational understanding of linear regression by implementing the algorithm manually, enabling deeper insight into how machine learning models work under the hood. The following are the objectives of the Project:


### Exploration Data Analysis (EDA)
* Checking for the empty or null column
* Data Visualization
* Plot loss curves and regression lines over training iterations to observe how the model learns over time and validate convergence.

### Implement Model Components from Scratch
* Setting the framework manually.
* Manually code essential elements such as mean square error and linear regression.
* Internalize each step in the learning process, like avoiding overfitting and underfitting.
* Feature Selection and Engineering.

### Understand Core Math and Logic
* Grasp the underlying principles of linear regression.
* Model evaluation and how the model minimizes error.
* Use this manual implementation as a stepping stone toward more advanced models, such as polynomial regression, logistic regression, or even neural nets by understanding optimization fundamentals.

# Techniques
Training a linear regression model to predict house prices begins with robust data preparation and thoughtful preprocessing. Before training the model, I make sure to figure out the type of data we have and its features. The column of the dataset was scrutinized for the null value, and the target has null, good dataset. Check the distribution of the feature, especially the target variables, using exploratory data analysis (EDA) to accomplish this. All the columns were turned to lowercase to make the data more interpretable and predictive. Techniques like normalization, standardization, and one-hot encoding are applied. Creating the framework (without using scikit), Setting Training, Validation, and Test in 0.6, 0.2, 0.2 in percentage respectively. While making sure it can be shuffled, reproducing at random and deleting price (target) to eradicate overfitting and enhance the model’s ability to capture subtle patterns in the housing market.

Once the data is cleaned and transformed, the next phase involves model training and optimization. Using techniques like train-test splitting or k-fold cross-validation ensures that the model generalizes well to unseen data. When coding from scratch, gradient descent is a common method for finding optimal weights by minimizing a cost function such as Mean Squared Error. Training linear regression, I put the features(Xn) in list likewise weights (Wn) generating arrays apiece with n indicating numbers for each feature and weight. Loop over these weights and multiply them by the corresponding feature values.  b the a Regularization methods like Lasso or Ridge regression can also be integrated to prevent overfitting, especially when many correlated features are involved. Polynomial regression may be considered if the data shows non-linear patterns that simple linear models can't capture.



