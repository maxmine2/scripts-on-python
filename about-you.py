# Made By maxmine2
# Thanks for download
from math import *
def bmi_kg(weight_in_kg, height_in_m):
    return  round(weight_in_kg / (height_in_m * height_in_m), 2)
def water_needs(weight_in_kg=70):
    return weight_in_kg * 30
def water_needs_glasses(weight_in_kg, glass_size_in_ml = 200):
    return ceil(water_needs(weight_in_kg) / glass_size_in_ml)
def decrypt_bmi(bmi):
    if bmi < 16.0:
        return f"{bmi} :Big Deficiency of body weight"
    if 16.0 <= bmi <= 18.54:
        return f"{bmi} :A bit deficiency of body weight"
    if 18.55 <= bmi <= 24.99:
        return f"{bmi} :BMI Good"
    if 25 <= bmi <= 29.99:
        return f"{bmi} :Pre-obesity"
    if 30 <= bmi <= 34.99:
        return f"{bmi} :First-stage obesity!"
    if 35 <= bmi <= 39.99:
        return f"{bmi} :Second-stage obesity!"
    if bmi >= 40:
        return f"{bmi} :Morbid obesity!!"