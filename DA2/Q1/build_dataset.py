import pandas as pd
import numpy as np

# Generating random data for the dataset
np.random.seed(42)
genders = ['Male', 'Female']
weights = np.random.randint(50, 120, size=50)
heights = np.random.randint(150, 200, size=50)
bmis = weights / ((heights / 100) ** 2)
ages = np.random.randint(18, 70, size=50)


# Creating the DataFrame
data = pd.DataFrame({
    'Patient ID': np.arange(1, 51),
    'Gender': np.random.choice(genders, size=50),
    'Weight (kg)': weights,
    'Height (cm)': heights,
    'BMI': bmis.round(2),
    'Age': ages
})

def assign_physical_activity(age):
    if 18 <= age <= 36:
        return np.random.choice(['Very active', 'Moderately active'])
    elif 36 < age <= 54:
        return np.random.choice(['Lightly active', 'Moderately active', 'Sedentary'])
    else:
        return np.random.choice(['Sedentary', 'Lightly active'])

# Applying the function to create the new column
data['Physical Activity'] = data['Age'].apply(assign_physical_activity)

def assign_diet_needed(row):
    if (row['BMI'] > 25 ):
        return 1
    if (row['Age'] > 50 and row["Physical Activity"] == "Sedentary"):
        return 1
    
    return 0

# Applying the function to create the new column
data['Needs_Diet'] = data.apply(assign_diet_needed , axis = 1)



# Exporting the dataset to a CSV file
data.to_csv("patient_enrollment_diet.csv", index=False)