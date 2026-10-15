"""
PetroTech 2.0 Capstone: Well Production Simulator
Author: Jumah Abdulmojeed
Description: Interactive oil & gas well production simulator based on Arps' Exponential Decline Curve Analysis (DCA).
"""

import math
import matplotlib.pyplot as plt

wells = {}
initial_production_rates = []
well = []
years = []
decline_rates = []
wells_production_rates = {}


def arps_model(initial_rate, decline_rate, time):
    """
    Function to implement Arps' exponential decline model.
    Formula: q(t) = q_i * exp(-D * t)

    Arguments:
        initial_rate (float): Initial production rate (q_i)
        decline_rate (float): Nominal decline rate (D)
        time (int/float): Time elapsed (years)

    Returns:
        float: Estimated production rate at specified time
    """
    return initial_rate * math.exp(-decline_rate * time)


def input_parameters():
    """Captures well specifications from user input."""
    name_of_well = input("What is the name of the well?: ").strip()
    if not name_of_well:
        print("Well name cannot be empty.")
        return
    try:
        initial_production_rate = float(input("What is the initial production rate (qi)?: "))
        decline_rate = float(input("What is the decline rate (D)?: "))
        time = int(input("Time period (in years)?: "))
    except ValueError:
        print("Invalid numerical input. Please enter valid numbers.")
        return

    wells[name_of_well] = [initial_production_rate, decline_rate, time]
    well.append(name_of_well.capitalize())
    initial_production_rates.append(initial_production_rate)
    years.append(time)
    decline_rates.append(decline_rate)
    print(f"Parameters for well '{name_of_well.capitalize()}' saved successfully.")


def simulate_well():
    """Simulates production forecasts over time for all registered wells."""
    if not wells:
        print("No wells found. Please input parameters first (Option 1).")
        return

    for well_name, data in wells.items():
        qi = data[0]
        d = data[1]
        t = data[2]
        print(f"\n--- Simulating Well: {well_name.capitalize()} ---")
        production_rates = []
        for year in range(t + 1):
            rate = arps_model(qi, d, year)
            production_rates.append(round(rate, 2))
            print(f"Year {year}: Production Rate = {round(rate, 2)}")
        wells_production_rates[well_name.capitalize()] = production_rates


def analyze_production():
    """Computes and displays cumulative and average production statistics."""
    if not wells_production_rates:
        print("No production simulations available. Please simulate wells first (Option 2).")
        return

    print("\n" + "=" * 45)
    print("CUMULATIVE PRODUCTION FOR WELL(S):")
    print("=" * 45)
    for w_name, w_prod in wells_production_rates.items():
        print(f"  {w_name}: {round(sum(w_prod), 2)}")

    print("\n" + "=" * 45)
    print("AVERAGE ANNUAL PRODUCTION FOR WELL(S):")
    print("=" * 45)
    for w_name, w_prod in wells_production_rates.items():
        avg_prod = round(sum(w_prod) / len(w_prod), 2)
        print(f"  {w_name}: {avg_prod}")


def visualize_data():
    """Generates decline curve plots for each simulated well."""
    if not wells_production_rates:
        print("No production simulations available to plot. Please simulate wells first (Option 2).")
        return

    for well_name in wells_production_rates.keys():
        y = wells_production_rates[well_name]
        n = well.index(well_name)
        j = years[n]
        x = list(range(j + 1))

        plt.figure(figsize=(8, 5))
        plt.plot(x, y, marker="o", linestyle="-", color="#1f77b4", linewidth=2)
        plt.xlabel("Time (Years)", fontsize=12)
        plt.ylabel("Production Rate", fontsize=12)
        plt.title(f"Production Decline Curve - {well_name.upper()}", fontsize=14)
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.tight_layout()
        plt.show()


def main_menu():
    """Main interactive menu loop."""
    while True:
        print("\n" + "=" * 50)
        print("      PETROTECH WELL PRODUCTION SIMULATOR")
        print("=" * 50)
        print("1. Input parameters")
        print("2. Simulate wells")
        print("3. Analyze production")
        print("4. Visualize results")
        print("5. Exit")
        option = input("\nChoose an option (1-5): ").strip()

        if option.isdigit():
            selected = int(option)
            if selected == 1:
                try:
                    ask = int(input("How many wells do you want to input parameters for?: "))
                    for _ in range(ask):
                        input_parameters()
                except ValueError:
                    print("Please enter a valid integer.")
            elif selected == 2:
                simulate_well()
            elif selected == 3:
                analyze_production()
            elif selected == 4:
                visualize_data()
            elif selected == 5:
                print("Exiting simulator. Thank you!")
                break
            else:
                print("Input has to be between 1 and 5.")
        else:
            print("Invalid input. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main_menu()
