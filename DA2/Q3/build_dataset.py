import pandas as pd
import random

# Sample road IDs (National Highways (NH) and State Highways (SH) in India)
road_ids = [
    'NH1', 'NH2', 'NH44', 'NH48', 'NH66', 'NH19', 'NH16', 'NH9', 'NH7', 'NH31',
    'SH1', 'SH2', 'SH17', 'SH21', 'SH38', 'SH50', 'NH75', 'NH58', 'NH61', 'NH20',
    'SH39', 'SH12', 'SH15', 'SH25', 'NH27', 'NH8', 'NH37', 'NH4', 'SH10', 'NH10'
]

# Realistic length values (in kilometers) and bends, traffic volume, accident risk
lengths_km = [
    100, 250, 300, 450, 500, 600, 80, 150, 200, 275,
    50, 120, 170, 220, 320, 400, 90, 160, 180, 270,
    60, 140, 190, 260, 350, 75, 130, 210, 290, 360
]

number_of_bends = [
    10, 25, 15, 30, 45, 50, 5, 12, 20, 28,
    7, 18, 22, 35, 40, 55, 9, 17, 25, 31,
    6, 14, 19, 26, 38, 8, 16, 23, 29, 33
]

traffic_volumes = [
    5000, 20000, 15000, 30000, 40000, 6000, 8000, 12000, 18000, 22000,
    7000, 9000, 13000, 25000, 35000, 4500, 11000, 16000, 2000, 10000,
    3000, 14000, 23000, 27000, 3200, 17000, 28000, 5000, 19000, 30000
]

# Accident risk categories: 'Low', 'Moderate', 'High', 'Very High', 'Extreme'
accident_risks = [
    'Low', 'Moderate', 'High', 'Very High', 'Extreme'
]

# Generate 50 records
data = []
for i in range(50):
    road_id = random.choice(road_ids)
    length = random.choice(lengths_km)
    bends = random.choice(number_of_bends)
    traffic_volume = random.choice(traffic_volumes)
    
    # Determine accident risk based on number of bends and traffic volume
    if bends > 40 or traffic_volume > 25000:
        accident_risk = 'Extreme'
    elif bends > 30 or traffic_volume > 20000:
        accident_risk = 'Very High'
    elif bends > 20 or traffic_volume > 15000:
        accident_risk = 'High'
    elif bends > 10 or traffic_volume > 10000:
        accident_risk = 'Moderate'
    else:
        accident_risk = 'Low'
    
    data.append([road_id, length, bends, traffic_volume, accident_risk])

df_road_transport = pd.DataFrame(data, columns=['Road ID', 'Length (km)', 'Number of Bends', 'Traffic Volume', 'Accident Risk'])

file_path = r'DA2\Q3\road_transport_records.csv'
df_road_transport.to_csv(file_path, index=False)