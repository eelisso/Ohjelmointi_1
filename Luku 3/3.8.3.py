"""
Eelis Soikkeli, Exercise 3.8.3
Program for calculating paracetamol dose
"""


def calculate_dose(weight, delta_t, daily_dose):
    """ Calculates the correct paracetamol dose """
    if delta_t >= 6 and daily_dose < 4000:
        dose = 15 * weight
        if dose > 4000 - daily_dose:
            dose = 4000 - daily_dose
            return dose
        else:
            return dose
    else:
        return 0


def main():
    weight = int(input("Patient's weight (kg): "))
    delta_t = int(input("How much time has passed from the previous dose (full hours): "))
    daily_dose = int(input("The total dose for the last 24 hours (mg): "))
    print(f"The amount of Parasetamol to give to the patient: {calculate_dose(weight, delta_t, daily_dose)}")


if __name__ == "__main__":
    main()
