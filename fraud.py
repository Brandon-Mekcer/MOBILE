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


#Visualize the decision tree
# plt.figure(figsize=(20,10))
# plot_tree(model, filled=True, feature_names=X.columns, class_names=['Legitimate', 'Suspicious', 'Fraudulent'], rounded=True, fontsize=8)
# plt.title("Decision Tree for Mobile Money Fraud Detection")
# plt.show()

# # Attribute importance
# importances = model.feature_importances_
# # Plot feature importances
# plt.figure(figsize=(10,6))
# plt.barh(X.columns, importances)
# plt.xlabel("Feature Importance")
# plt.ylabel("Features")
# plt.title("Feature Importance in Decision Tree Model")
# plt.show()

