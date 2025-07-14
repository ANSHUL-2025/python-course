def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  # convert height to meters
    bmi = weight / (height_m ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("=== BMI CHECKER ===")
    
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in cm: "))
        
        if weight <= 0 or height <= 0:
            print("Please enter positive values for weight and height.")
            return
        
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")
    
    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()
