import os

def MainMenuSelection():
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print("*"*70)
        print("************ Medical Calculator ***************")
        print("1. BMI Calculator")
        print("2. Blood Pressure Calculator")
        print("3. Cardiovascular Fitness")
        try:
            main_input = int(input("Enter a number to select a calculator here --> : "))
            return main_input
        except ValueError:
            print("Invalid option selected please try again!")

#Calculator 1
def BMICalculator(height_m, weight_kg):

    height_squared = height_m ** 2 
    bmi_total = weight_kg / height_squared
    rounded_bmi = round(bmi_total, 1) 
    
    if rounded_bmi < 18.5:
        category = "Underweight"
        advice = "It is advised to seek help from a medical professional."
    elif rounded_bmi < 25.0:
        category = "Normalweight"
        advice = "You are in a healthy state."
    elif rounded_bmi < 30.0:
        category = "Overweight"
        advice = "It is advised to seek help from a medical professional."
    else:
        category = "Obese"
        advice = "It is advised to seek help from a medical professional."

    return rounded_bmi, category, advice

#Calculator 2
def BloodPressureCalculator(systolic, diastolic):
    MeanArterialPressure = (systolic + (2 * diastolic)) / 3
    rounded_map = round(MeanArterialPressure, 1)

    if rounded_map < 60:
        status = "Low"
        advice = "This Mean Arterial Pressure is too low! Please Seek immediate medical help."
    elif 60 <= rounded_map <= 100:
        status = "Normal"
        advice = "Your Mean Arterial Pressure is at normal levels. Your heart is very healthy!"
    elif rounded_map > 120:
        status = "Critical"
        advice = "Your Meanial Arterial Pressure is critically high. Seek medical help immediately!"
    else: 
        status = "High"
        advice = "Your Meanial Arterial pressure is higher than usual. If you are resting, please raise an alarm."    
        
    return rounded_map, status, advice

#Calculator 3
def CardiovascularFitness(distance_m, gender, age):
    ConstantX = 504.9
    ConstantY = 44.73
    
    CalculateVo2Max = distance_m - ConstantX
    FinalVO2Value = round(CalculateVo2Max / ConstantY, 1)
    
    category = "Unknown"
    if gender == 'M':
        if age < 30:
            if FinalVO2Value < 35: category = "Low"
            elif FinalVO2Value <= 43: category = "Normal"
            else: category = "High"
        elif age <= 39:
            if FinalVO2Value < 34: category = "Low"
            elif FinalVO2Value <= 41: category = "Normal"
            else: category = "High"
        elif age <= 49:
            if FinalVO2Value < 32: category = "Low"
            elif FinalVO2Value <= 39: category = "Normal"
            else: category = "High"
        else:
            if FinalVO2Value < 29: category = "Low"
            elif FinalVO2Value <= 36: category = "Normal"
            else: category = "High"
            
    elif gender == 'F':
        if age < 30:
            if FinalVO2Value < 31: category = "Low"
            elif FinalVO2Value <= 37: category = "Normal"
            else: category = "High"
        elif age <= 39:
            if FinalVO2Value < 30: category = "Low"
            elif FinalVO2Value <= 36: category = "Normal"
            else: category = "High"
        elif age <= 49:
            if FinalVO2Value < 28: category = "Low"
            elif FinalVO2Value <= 33: category = "Normal"
            else: category = "High"
        else:
            if FinalVO2Value < 24: category = "Low"
            elif FinalVO2Value <= 29: category = "Normal"
            else: category = "High"

    return FinalVO2Value, category


if __name__ == "__main__":
    MainMenu = MainMenuSelection()
    if MainMenu == 1:
        h = float(input("Enter height (m): "))
        w = float(input("Enter weight (kg): "))
        bmi, cat, adv = BMICalculator(h, w)
        print(f"Your BMI is {bmi}. Category: {cat}. {adv}")
    elif MainMenu == 2:
        s = int(input("Enter Systolic: "))
        d = int(input("Enter Diastolic: "))
        m_val, stat, adv = BloodPressureCalculator(s, d)
        print(f"MAP: {m_val} mmHg. Status: {stat}. {adv}")
    elif MainMenu == 3:
        dist = float(input("Enter Distance (m): "))
        g = input("Gender (M/F): ")
        a = int(input("Age: "))
        vo2, cat = CardiovascularFitness(dist, g, a)
        print(f"VO2 Max: {vo2}. Level: {cat}")