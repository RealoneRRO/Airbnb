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
Training a linear regression model to predict house prices begins with robust data preparation and thoughtful preprocessing. The first step is understanding the dataset and identifying relevant features. Null values are checked and handled appropriately; if the target variable has nulls, the null might be replaced by zero or an average of the values in the column. Exploratory Data Analysis (EDA) is used to understand the distribution of features, especially the target variable. All column names are standardized to lowercase to maintain consistency. Key preprocessing techniques such as normalization, standardization, and one-hot encoding are applied. The dataset is then split into training, validation, and test sets in a 60:20:20 ratio, with shuffling and random seeding to ensure reproducibility. To avoid overfitting, the target variable (price) is carefully removed before certain steps and added back only when needed.

Once the data is cleaned and transformed, the model training begins. Without relying on machine learning libraries like scikit-learn, I implemented the linear regression algorithm from scratch. Setting up a framework used for optimization by minimizing the Mean Squared Error (MSE) cost function. Each feature (Xn+1) and its corresponding weight (Wn) are represented as arrays. Predictions are calculated by computing the dot product between the weight and feature vectors for each row in the dataset. This matrix-based approach simplifies and accelerates prediction. The process is modular and reusable, as demonstrated in the custom *Airbnb.py* implementation. See *line 48* in the code for the core algorithm.![The formulae for Linear regression](https://github.com/user-attachments/assets/9851e78c-d07d-482c-a94e-d2d788a0f58a)

During model evaluation, feature selection plays a key role in improving performance. A high Root Mean Square Error (RMSE) initially indicated missing influential features. Adding geographic features like latitude and longitude improved prediction accuracy. Regularization techniques were introduced to handle multicollinearity and prevent overfitting. Polynomial regression can be considered for more accurate modeling if the dataset exhibits non-linear patterns. Ultimately, the model is evaluated to ensure it generalizes well to unknown data, making it suitable for real-world housing price predictions.

# In Conclusion
Building a linear regression model from scratch to predict house prices offers deep insight into the core mechanics of machine learning. From rigorous data preprocessing to manually implementing gradient descent and evaluating with RMSE, this project emphasizes not just getting accurate predictions but understanding the why behind each step. This hands-on approach reinforces fundamental concepts like feature transformation, loss minimization, and overfitting prevention using regularization.

By bypassing high-level libraries and constructing the framework manually, we gain a granular understanding of model behavior and decision-making. Using the model on the test dataset to predict a home costs $64,745. The successful inclusion of features like location and thoughtful preprocessing workflows led to a model capable of generalizing well to unseen data. This foundation sets the stage for more advanced experimentation, including non-linear regression and feature engineering, as I evolve in building the projects.
# Installation
* Python (3.8 or later)
* Pip (Python package manager)
* Git (to clone the repository)
* FlaskAPI (Running Locally)
* Streamlit(Using Web Apps)
* Docker (if you want to run it in a container)
* [Check out the article on this project here](https://medium.com/@sashefrro/airbnb-predicting-the-price-of-vacation-homes-using-a-machine-learning-model-c6048484a24c)



