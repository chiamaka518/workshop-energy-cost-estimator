# Workshop Energy Cost Estimator

![Python Version](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Department](https://img.shields.io/badge/Department-Mechatronics%20Engineering-0052CC)
![Institution](https://img.shields.io/badge/Institution-YabaTech-green)
![Status](https://img.shields.io/badge/Project-Completed-success)

## What it does
The **Workshop Energy Cost Estimator** is a specialized engineering utility created for mechatronics and industrial workshops. It records machinery power ratings (in Watts), operating hours per day, and local electricity tariffs to accurately calculate daily and monthly energy consumption in kilowatt-hours (kWh) and total operational electricity costs.

## How to run it
Install Python 3, then run:
```bash
python workshop_energy_calculator.py
```
*(On mobile devices, open `workshop_energy_calculator.py` inside the **Pydroid 3** app and tap the yellow Play/Run button).*

## Sample output
```text
=================================================================
    WELCOME TO THE WORKSHOP ENERGY COST ESTIMATOR
        Department of Mechatronics Engineering, YabaTech
=================================================================
Accurately calculate machine energy use (kWh) and power costs.

Enter currency symbol (Press Enter for ₦, or type $, £, etc.): ₦
Enter electricity tariff per kWh in ₦: 209

How many machines do you want to record? 2

--- Machine 1 of 2 ---
Enter machine name (e.g., CNC Mill, 3D Printer, Lathe): CNC Milling Machine
Enter power rating for 'CNC Milling Machine' in Watts: 2200
Enter operating hours per day for 'CNC Milling Machine' (0.1 - 24): 6

--- Machine 2 of 2 ---
Enter machine name (e.g., CNC Mill, 3D Printer, Lathe): 3D Printer
Enter power rating for '3D Printer' in Watts: 350
Enter operating hours per day for '3D Printer' (0.1 - 24): 8

╔══════════════════════════════════════════════════════════════════════════╗
║                    WORKSHOP ENERGY CONSUMPTION REPORT                    ║
╠════════════════════════╦═══════════╦══════════╦═══════════╦══════════════╣
║ Machine Name           ║ Power (W) ║ Usage/Day║ Daily kWh ║ Monthly Cost ║
╠════════════════════════╬═══════════╬══════════╬═══════════╬══════════════╣
║ CNC Milling Machine    ║   2,200 W ║    6.0 h ║     13.20 ║  ₦ 82,764.00 ║
║ 3D Printer             ║     350 W ║    8.0 h ║      2.80 ║  ₦ 17,556.00 ║
╠════════════════════════╩═══════════╩══════════╩═══════════╬══════════════╣
║ TOTAL ESTIMATED MONTHLY BILL:                             ║ ₦ 100,320.00 ║
╚═══════════════════════════════════════════════════════════╩══════════════╝

Overview:
  • Total Daily Energy:   16.00 kWh/day
  • Total Monthly Energy: 480.00 kWh/month (30-day basis)
  • Applied Tariff Rate:  ₦ 209.00 per kWh

=================================================================
        ENERGY BREAKDOWN & EFFICIENCY ADVISORY (TWIST)
=================================================================

Energy Consumption Breakdown:
  CNC Milling Machine [██████████████░░░░]  82.5%
  3D Printer          [███░░░░░░░░░░░░░░░]  17.5%

>> Top Energy Consumer ('Energy Hog'): 'CNC Milling Machine'
   Monthly Expense: ₦ 82,764.00 (82.5% of total bill)

[Cost Optimization Recommendation]
Notice: 'CNC Milling Machine' accounts for the vast majority of your power bill.
By reducing its idle/operating runtime by just 15% (e.g., scheduled batch runs),
your workshop can save approximately ₦ 12,414.60 every single month!
=================================================================

Would you like to analyze another workshop? (y/n): n

Thank you for using the Workshop Energy Cost Estimator. Goodbye!
```

## My own twist
I added an **Interactive Energy Breakdown & Efficiency Advisory system**. 
1. The program automatically draws visual ASCII consumption bars showing each machine's proportional share of the workshop's power bill.
2. It detects the highest energy-consuming equipment ("Energy Hog") and projects exact financial savings if that machine's runtime is optimized by 15% (e.g., through idle-power reduction and scheduled batching).
3. It features dynamic currency support, formatted table reporting with thousands separators, and an interactive re-run menu loop.

## What I learned
1. How to structure modular Python functions that accept parameters and return computed values.
2. How to create defensive user inputs using `while` loops and `try/except ValueError` to prevent unexpected crashes.
3. How to organize structured datasets with lists and dictionaries to display professional, formatted reports.

## Author
Dike Maryanna Chiamaka, ND2 Mechatronics Engineering, YabaTech.
