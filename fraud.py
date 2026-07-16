import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
import joblib

# Reading the dataset
mobdata = pd.read_csv("mobile_money_fraud.csv")
print(mobdata)

# EDA
print(mobdata.head(10))
print(mobdata.info())
print(mobdata.isnull().sum())
print(mobdata.shape)

#Separate the X and Y features
X = mobdata.drop(columns=['transaction_status','transaction_id'])
print(X.shape)
y = mobdata['transaction_status']
print(y)

# Plotting the absolute correlation between features and target variable
for column in X.columns:
    correlation = abs(X[column].corr(y.map({'Legitimate': 0, 'Suspicious': 1, 'Fraudulent': 2})))
    print(f"Absolute correlation between {column} and transaction_status: {correlation}")



# plt.figure(figsize=(10, 8))
# plt.barh(X.columns, [abs(X[column].corr(y.map({'Legitimate': 0, 'Suspicious': 1, 'Fraudulent': 2}))) for column in X.columns])
# plt.xlabel("Absolute Correlation with transaction_status")
# plt.ylabel("Features")
# plt.title("Feature Correlation with transaction_status")
# plt.show()
#Train and test
X_train,X_test,y_train,y_test = train_test_split(
    X,y, test_size = 0.3,random_state=42,stratify=y)#random state is to ensure data remains consistent.
#keeps class proportions consistent in train/test
print(X_train.shape)
print(X_test.shape)


#Fit the model on training data
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train,y_train)

y_pred = model.predict(X_test)
print(y_pred)

print("Accuracy:", accuracy_score(y_test,y_pred))

# Save the model
joblib.dump(model, 'Fraud_model.pkl')

# Using ANN model for prediction
from sklearn.neural_network import MLPClassifier
ann_model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=300, random_state=42)
ann_model.fit(X_train, y_train)
y_pred_ann = ann_model.predict(X_test)
print("ANN Model Predictions:", y_pred_ann)
print("ANN Model Accuracy:", accuracy_score(y_test, y_pred_ann))

# Kmeans Clustering
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# Dispaly number of samples in each cluster
import numpy as np
unique, counts = np.unique(y_kmeans, return_counts=True)
print("KMeans Clustering Counts:", dict(zip(unique, counts))) 

print("KMeans Clustering Predictions:", y_kmeans)


#Visualize the decision tree
# plt.figure(figsize=(20,10))
# plot_tree(model, filled=True, feature_names=X.columns, class_names=['Legitimate', 'Suspicious', 'Fraudulent'], rounded=True, fontsize=8)
# plt.title("Decision Tree for Mobile Money Fraud Detection")
# plt.show()

# Attribute importance
# importances = model.feature_importances_
# # Plot feature importances
# plt.figure(figsize=(8,6))
# plt.barh(X.columns, importances)
# plt.xlabel("Feature Importance")
# plt.ylabel("Features")
# plt.title("Feature Importance in Decision Tree Model")
# plt.show()

