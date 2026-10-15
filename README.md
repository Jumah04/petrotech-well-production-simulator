# PetroTech Well Production Simulator

> **Interactive Oil & Gas Production Forecasting & Decline Curve Analysis (DCA)**  
> *Capstone Project — PetroTech 2.0 Program*  
> **Author:** Jumah Abdulmojeed

---

## 📌 Project Overview

In petroleum and reservoir engineering, estimating future hydrocarbon recovery and forecasting production rates over time is vital for asset valuation, field development planning, and economic feasibility assessments.

The **PetroTech Well Production Simulator** is an interactive Python application and computational notebook that implements **Arps' Exponential Decline Curve Analysis (DCA)**. It enables petroleum engineers, students, and analysts to simulate single or multi-well production profiles, compute cumulative recoveries and averages, and visualize decline curves.

---

## 📐 Mathematical Formulation

The simulator uses **J.J. Arps' Empirical Exponential Decline Model** (applicable where the decline exponent $b = 0$):

$$q(t) = q_i \cdot e^{-D \cdot t}$$

Where:
* $q(t)$: Production rate at time $t$ (e.g., STB/day, MSCF/year)
* $q_i$: Initial production rate at time $t = 0$
* $D$: Nominal exponential decline rate (fraction per year)
* $t$: Elapsed time in production (years)
* $e$: Base of natural logarithms ($\approx 2.71828$)

### Key Analytics Derived:
1. **Cumulative Production ($N_p$):** Sum of annual production rates across the operational lifespan:
   $$N_p = \sum_{t=0}^{T} q(t)$$
2. **Average Annual Production ($\bar{q}$):**
   $$\bar{q} = \frac{N_p}{T + 1}$$

---

## ✨ Features

- **Multi-Well Parameter Configuration:** Register multiple wells with customized initial production rates ($q_i$), decline rates ($D$), and forecast lifespans ($t$).
- **Deterministic Production Simulation:** Automatically evaluates the Arps exponential decline equation for every operational year.
- **Production Analytics Engine:** Computes cumulative production and average annual rates per well.
- **Graphical Visualization:** Generates formatted decline curve plots ($q$ vs. $t$) using `matplotlib`.
- **Dual Execution Modes:**
  - **Jupyter Notebook (`.ipynb`):** Step-by-step interactive workflow.
  - **Standalone Python Script (`well_simulator.py`):** Self-contained, menu-driven CLI application.

---

## 📂 Repository Structure

```text
petrotech-well-production-simulator/
├── Jumah_Abdulmojeed_PetroTech_2_0_Capstone.ipynb   # Original capstone Jupyter notebook
├── well_simulator.py                               # Standalone interactive CLI script
├── .gitignore                                      # Standard Python/Jupyter ignore rules
└── README.md                                       # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.8+ installed along with `matplotlib`:

```bash
pip install matplotlib
```

*(Optional: Install `jupyter` if you wish to run the notebook)*:
```bash
pip install notebook
```

### Running the Standalone Simulator

Launch the interactive console application:

```bash
python well_simulator.py
```

### Interactive Menu Workflow

```text
==================================================
      PETROTECH WELL PRODUCTION SIMULATOR
==================================================
1. Input parameters
2. Simulate wells
3. Analyze production
4. Visualize results
5. Exit

Choose an option (1-5):
```

1. **Option 1 (Input parameters):** Prompts for the number of wells and asks for:
   - Well Name (e.g., `Alpha-1`)
   - Initial Production Rate $q_i$ (e.g., `1200`)
   - Decline Rate $D$ (e.g., `0.15`)
   - Production Horizon $t$ in years (e.g., `5`)
2. **Option 2 (Simulate wells):** Evaluates Arps' model year-by-year for each well.
3. **Option 3 (Analyze production):** Prints cumulative and average production metrics.
4. **Option 4 (Visualize results):** Displays individual decline curves using Matplotlib.
5. **Option 5 (Exit):** Closes the application.

---

## 📈 Sample Plot Output

The simulator visualizes the exponential decline curve with labeled axes, markers, and gridlines:

```text
Production Rate (q)
  ^
qi| *
  |   \
  |     *
  |       \
  |         *
  |           \
  |             *
  +------------------> Time (Years)
```

---

## 👤 Author & Acknowledgments

- **Author:** Jumah Abdulmojeed
- **Program:** PetroTech 2.0 Capstone Program
- Special thanks to the PetroTech instructors and mentors for facilitating this petroleum engineering learning journey.
