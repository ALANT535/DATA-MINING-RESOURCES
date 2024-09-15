import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv(r"DA2\Q2\patient_enrollment_diet.csv")

le = LabelEncoder()

data['Physical Activity'] = le.fit_transform(data['Physical Activity'])
data = pd.get_dummies(data, columns=['Gender'], drop_first=True)

print(data.head())

data.to_csv(r"DA2\Q1\patient_enrollment_diet.csv", index=False)