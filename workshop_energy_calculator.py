# ==============================================================================
# Project: Workshop Energy Cost Estimator
# Author: Dike Maryanna Chiamaka
# Department: Mechatronics Engineering, YabaTech
# Description: Calculates energy consumption (kWh) and costs for workshop 
#              equipment, featuring an ASCII summary table, visual energy bars,
#              and an Energy Efficiency Advisory twist.
# ==============================================================================

# ANSI Color Codes for terminal styling (clean and modern)
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"


# Function 1: Calculates daily energy consumed in kilowatt-hours (kWh)
# Formula: (Power in Watts * Hours used) / 1000
def calculate_daily_kwh(watts, hours):
    return (watts * hours) / 1000.0


# Function 2: Calculates total cost based on energy and electricity tariff
def calculate_cost(kwh, tariff_rate):
    return kwh * tariff_rate


# Function 3: Helper function to safely get positive numbers from the user
# Prevents program crash if someone types letters instead of numbers.
def get_valid_positive_number(prompt):
    while True:
        user_input = input(prompt).strip()
        try:
            value = float(user_input)
            if value <= 0:
                print(f"{YELLOW}>> Error: Please enter a number greater than 0.{RESET}")
            else:
                return value
        except ValueError:
            print(f"{YELLOW}>> Error: Invalid input! Please enter a valid number (e.g., 500 or 2.5).{RESET}")


# Function 4: Generates a visual ASCII percentage bar (e.g., [████████░░░░░░░░░░] 45.0%)
def draw_bar(percentage, total_blocks=20):
    filled = int((percentage / 100.0) * total_blocks)
    filled = max(0, min(total_blocks, filled))  # Keep within 0 and total_blocks
    empty = total_blocks - filled
    return "█" * filled + "░" * empty


# Function 5: Displays the Workshop Summary Table
def display_summary_table(machines, tariff, currency):
    print("\n" + CYAN + BOLD + "╔" + "═" * 74 + "╗")
    print("║" + " " * 20 + "WORKSHOP ENERGY CONSUMPTION REPORT" + " " * 20 + "║")
    print("╠" + "═" * 24 + "╦" + "═" * 11 + "╦" + "═" * 10 + "╦" + "═" * 11 + "╦" + "═" * 14 + "╣")
    print("║ Machine Name           ║ Power (W) ║ Usage/Day║ Daily kWh ║ Monthly Cost ║")
    print("╠" + "═" * 24 + "╬" + "═" * 11 + "╬" + "═" * 10 + "╬" + "═" * 11 + "╬" + "═" * 14 + "╣" + RESET)

    total_daily_kwh = 0.0
    total_monthly_kwh = 0.0
    total_monthly_cost = 0.0

    for item in machines:
        name_col = item["name"][:22].ljust(22)
        power_col = f"{item['watts']:,.0f} W".rjust(9)
        hours_col = f"{item['hours']:.1f} h".rjust(8)
        kwh_col = f"{item['daily_kwh']:.2f}".rjust(9)
        cost_col = f"{currency} {item['monthly_cost']:,.2f}".rjust(12)

        print(f"║ {name_col} ║ {power_col} ║ {hours_col} ║ {kwh_col} ║ {cost_col} ║")

        total_daily_kwh += item["daily_kwh"]
        total_monthly_kwh += item["monthly_kwh"]
        total_monthly_cost += item["monthly_cost"]

    total_cost_str = f"{currency} {total_monthly_cost:,.2f}".rjust(12)

    print(CYAN + BOLD + "╠" + "═" * 24 + "╩" + "═" * 11 + "╩" + "═" * 10 + "╩" + "═" * 11 + "╬" + "═" * 14 + "╣")
    print(f"║ TOTAL ESTIMATED MONTHLY BILL:                           ║ {total_cost_str} ║")
    print("╚" + "═" * 59 + "╩" + "═" * 14 + "╝" + RESET)

    print(f"\n{BOLD}Overview:{RESET}")
    print(f"  • Total Daily Energy:   {total_daily_kwh:.2f} kWh/day")
    print(f"  • Total Monthly Energy: {total_monthly_kwh:.2f} kWh/month (30-day basis)")
    print(f"  • Applied Tariff Rate:  {currency} {tariff:,.2f} per kWh")

    return total_monthly_cost


# Function 6: The Twist - Energy Hog and Cost Optimization Advisor
def show_energy_advisor(machines, total_monthly_cost, tariff, currency):
    print("\n" + CYAN + BOLD + "=" * 65)
    print("        ENERGY BREAKDOWN & EFFICIENCY ADVISORY (TWIST)")
    print("=" * 65 + RESET)

    # 1. Visual Breakdown of energy consumption per machine
    print(f"\n{BOLD}Energy Consumption Breakdown:{RESET}")
    highest_machine = machines[0]

    for machine in machines:
        if total_monthly_cost > 0:
            pct = (machine["monthly_cost"] / total_monthly_cost) * 100
        else:
            pct = 0.0

        bar = draw_bar(pct, total_blocks=18)
        machine_name = machine["name"][:18].ljust(18)
        print(f"  {machine_name} [{CYAN}{bar}{RESET}] {pct:5.1f}%")

        if machine["monthly_cost"] > highest_machine["monthly_cost"]:
            highest_machine = machine

    if total_monthly_cost > 0:
        top_pct = (highest_machine["monthly_cost"] / total_monthly_cost) * 100
    else:
        top_pct = 0.0

    # 2. Highlight Top Energy Consumer
    print(f"\n{YELLOW}{BOLD}>> Top Energy Consumer ('Energy Hog'): '{highest_machine['name']}'{RESET}")
    print(f"   Monthly Expense: {currency} {highest_machine['monthly_cost']:,.2f} ({top_pct:.1f}% of total bill)")

    # 3. Calculate 15% optimization savings
    optimized_hours = highest_machine["hours"] * 0.85
    new_daily_kwh = calculate_daily_kwh(highest_machine["watts"], optimized_hours)
    new_monthly_kwh = new_daily_kwh * 30
    new_monthly_cost = calculate_cost(new_monthly_kwh, tariff)
    savings = highest_machine["monthly_cost"] - new_monthly_cost

    print(f"\n{GREEN}{BOLD}[Cost Optimization Recommendation]{RESET}")
    if top_pct >= 40:
        print(f"Notice: '{highest_machine['name']}' accounts for the vast majority of your power bill.")
    else:
        print(f"Notice: Managing '{highest_machine['name']}' offers the best opportunity to reduce expenses.")

    print(f"By reducing its idle/operating runtime by just {BOLD}15%{RESET} (e.g., scheduled batch runs),")
    print(f"your workshop can save approximately {GREEN}{BOLD}{currency} {savings:,.2f}{RESET} every single month!")
    print(CYAN + "=" * 65 + RESET)


# Main workflow function
def run_estimator():
    print(CYAN + BOLD + "\n" + "=" * 65)
    print("    WELCOME TO THE WORKSHOP ENERGY COST ESTIMATOR")
    print("        Department of Mechatronics Engineering, YabaTech")
    print("=" * 65 + RESET)
    print("Accurately calculate machine energy use (kWh) and power costs.\n")

    # Ask for preferred currency symbol (defaults to Naira ₦)
    curr_input = input("Enter currency symbol (Press Enter for ₦, or type $, £, etc.): ").strip()
    currency = curr_input if curr_input != "" else "₦"

    # Get electricity tariff rate
    tariff = get_valid_positive_number(f"Enter electricity tariff per kWh in {currency}: ")

    # Get number of machines
    while True:
        try:
            count_input = input("\nHow many machines do you want to record? ").strip()
            num_machines = int(count_input)
            if num_machines > 0:
                break
            print(f"{YELLOW}>> Error: You must enter at least 1 machine.{RESET}")
        except ValueError:
            print(f"{YELLOW}>> Error: Please enter a whole number (e.g., 2, 3, 5).{RESET}")

    machines = []

    # Collect data for each machine
    for i in range(num_machines):
        print(f"\n{BOLD}--- Machine {i + 1} of {num_machines} ---{RESET}")
        
        while True:
            name = input("Enter machine name (e.g., CNC Mill, 3D Printer, Lathe): ").strip()
            if name != "":
                break
            print(f"{YELLOW}>> Error: Machine name cannot be left blank.{RESET}")

        watts = get_valid_positive_number(f"Enter power rating for '{name}' in Watts: ")
        
        while True:
            hours = get_valid_positive_number(f"Enter operating hours per day for '{name}' (0.1 - 24): ")
            if hours <= 24:
                break
            print(f"{YELLOW}>> Error: A day only has 24 hours! Please enter 24 or less.{RESET}")

        daily_kwh = calculate_daily_kwh(watts, hours)
        monthly_kwh = daily_kwh * 30  # 30-day billing cycle
        daily_cost = calculate_cost(daily_kwh, tariff)
        monthly_cost = calculate_cost(monthly_kwh, tariff)

        machines.append({
            "name": name,
            "watts": watts,
            "hours": hours,
            "daily_kwh": daily_kwh,
            "monthly_kwh": monthly_kwh,
            "daily_cost": daily_cost,
            "monthly_cost": monthly_cost
        })

    # Display report table
    total_monthly_cost = display_summary_table(machines, tariff, currency)

    # Run the Twist: Energy breakdown & savings advisor
    show_energy_advisor(machines, total_monthly_cost, tariff, currency)


# Main program loop
def main():
    while True:
        run_estimator()
        
        # Ask user if they wish to perform another calculation
        choice = input(f"\n{BOLD}Would you like to analyze another workshop? (y/n): {RESET}").strip().lower()
        if choice not in ["y", "yes"]:
            print(f"\n{CYAN}Thank you for using the Workshop Energy Cost Estimator. Goodbye!{RESET}\n")
            break


if __name__ == "__main__":
    main()
