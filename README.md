# Python Numerical Methods Toolbox

A small collection of **interactive Python apps** that demonstrate classic numerical‑analysis techniques:

| Folder | Topic | Purpose |
|--------|-------|---------|
| `Modular_Integral/` | **Modular Integration** | Compute definite integrals using a selectable rule (Trapezoidal, Simpson, etc.) |
| `Finding_Function_Roots/` | **Root Finding** | Locate zeros of a nonlinear function (Bisection, Newton‑Raphson, Secant) |
| `Linear_Regression/` | **Linear Regression** | Fit a straight line to a CSV dataset and visualise the results |

All GUIs were built with **TkInter**, and the numerical core relies on **NumPy**, **SymPy**, **Pandas**, and **Matplotlib**.

---

## 🚀 Features

- **Point‑and‑click interface** for every algorithm (TkInter + Matplotlib canvas)  
- **Real‑time plots** that update as iterations progress  
- **Flexible function input** (SymPy parses the expression typed by the user)  
- **CSV import/export** for regression datasets  
- **Step‑by‑step tables** rendered with `tabulate` for easier report writing  
- **Decimal rounding control** for more precise classroom experiments  

---

## 🛠️ Tech Stack

| Category   | Libraries / Tools |
|------------|------------------|
| Language   | Python 3.10+ |
| GUI        | TkInter |
| Math       | NumPy, SymPy, Decimal |
| Data I/O   | Pandas, Tabulate |
| Plotting   | Matplotlib |
| Dev        | VS Code, `venv` |

---

## ⚙️ Installation

```bash
# clone the repo
git clone ...
cd python‑numerical‑methods

# create a virtual environment
python -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate

# install dependencies
pip install -r requirements.txt      # or install manually:
# pip install numpy sympy pandas matplotlib tabulate
```

---

## ▶️ Usage

Run the GUI of the topic you want to explore:

```bash
# Modular Integral
python Modular_Integral/gui.py

# Function Roots
python Finding_Function_Roots/testeGui.py

# Linear Regression
python Linear_Regression/gui.py
```

Each window guides you through the required inputs and shows a live chart of the computation.

---

## 📂 Project Structure

```text
PYTHON_NUMERICAL_METHODS/
├── Modular_Integral/
│   ├── gui.py
│   └── integral_modular.py
├── Finding_Function_Roots/
│   ├── testeGui.py
│   └── zeros_funcao.py
├── Linear_Regression/
│   ├── gui.py
│   └── regressao_linear.py
└── docs/
    └── images/     # screenshots & GIFs for the README
```

---

## 👥 Authors

| Name |
|------|
| João Pedro Figols |
| Júlia Schmidt |
| Leonardo Grupioni |

> **Course:** Numerical Methods (B.Sc. Computer Science – PUC‑SP)  
