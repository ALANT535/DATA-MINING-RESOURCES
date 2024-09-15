import pandas as pd
import random
import numpy as np

# Load the existing 50 rows patient dataset
file_path = 'path_to_your_existing_patient_data.csv'  # Replace with the path to your existing patient dataset
df_patient = pd.read_csv(file_path)

# Generate 50 more unique rows of patient data
new_patient_data = []
for i in range(50):
    name = f"Patient_{i+51}"
    age = random.randint(17, 35)
    gender = random.choice(["Male", "Female"])
    weight = random.uniform(55, 90)
    height = random.uniform(1.5, 2.0)  # height in meters
    bmi = round(weight / (height ** 2), 2)  # BMI calculation
    blood_pressure = random.randint(90, 140)
    cholesterol = random.uniform(150, 250)
    glucose = random.uniform(70, 180)
    
    # Append the new patient data to the list
    new_patient_data.append([name, age, gender, round(weight, 2), round(height, 2), bmi, blood_pressure, cholesterol, glucose])

# Create a DataFrame for new patient data
df_new_patients = pd.DataFrame(new_patient_data, columns=df_patient.columns)

# Concatenate the original and new DataFrames to get 100 rows
df_100_patients = pd.concat([df_patient, df_new_patients], ignore_index=True)

# Add the 'Creatine' column: 60% (0.5-2) and 40% (2-5.5)
df_100_patients['Creatine'] = np.where(np.random.rand(100) < 0.6, 
                                       np.round(np.random.uniform(0.5, 2, 100), 2), 
                                       np.round(np.random.uniform(2, 5.5, 100), 2))

# Save the new dataset with 100 rows to a CSV file
file_path_100 = r'DA2\Q2\patient_da2_dataset.csv'  # Specify the path where you want to save the new dataset
df_100_patients.to_csv(file_path_100, index=False)