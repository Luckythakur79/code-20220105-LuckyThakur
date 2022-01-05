import pandas as pd

a = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82},
     {"Gender": "Female", "HeightCm": 175, "WeightKg": 75}   ]


df = pd.DataFrame(a)
bmi  =[]
health_risk=[]
for i in range (0,len(df['HeightCm'])):
    x =round(int(df["WeightKg"][i])/((int(df["HeightCm"][i])/100) * (int(df["HeightCm"][i])/100)),2)
    bmi.append(x)
    if x<=18.4:
        health_risk.append('Malnutrition risk')
    elif x>=18.5 and x<=24.9:
        health_risk.append('Low risk')
    elif x>=25 and x<=29.9:
        health_risk.append('Enhanced risk')
    elif x >= 30 and x <= 34.9:
        health_risk.append('Medium risk')
    elif x >= 35 and x <= 39.9:
        health_risk.append('High risk')
    elif x >=40:
        health_risk.append('Very high risk')

df.insert(loc=3,column='BMI',value=bmi)
df.insert(loc=4,column='health_risk',value=health_risk)
print(df)
