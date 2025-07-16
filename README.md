# MPIN-Strength-Analyzer
## 🚀 Live Demo

🔗 [Run MPIN Analyzer App on Streamlit](https://shubham0x1-mpin-strength-analyzer-app-jcji3d.streamlit.app/)

## 📓 Interactive Notebook

🔗 [Open in Google Colab](https://colab.research.google.com/drive/19wbL7FiONRK9Jy77mhFRy1c6kA8GDUUk?usp=sharing)

# 🔎 Overview
Mobile Personal Identification Numbers (MPINs) are used as secure login credentials for accessing mobile banking applications. However, users often select MPINs that are easy to guess — making their accounts vulnerable to attacks.

## 🔐 Why MPINs Are Often Weak:
Use of commonly repeated or popular patterns (e.g., 1122, 0000, 2580)

MPINs derived from personal demographic information, such as:

📅 Date of Birth (DOB)

💍 Wedding Anniversary

🧑‍🤝‍🧑 Spouse’s Date of Birth

For instance, if a user's DOB is 15-Aug-1995, possible weak MPINs might include:

1508 (Day + Month)

9508 (Year + Month)

1595 (Day + Year)

These patterns are easily predictable — especially when attackers use social engineering or data breaches to guess them.

# Challenge Statement and Implementation Parts

### Part A: Detection of Common 4-Digit MPINs

- Develop a function that evaluates whether a 4-digit MPIN is present in a predefined list of commonly used or easily guessable PINs.
- If the input MPIN matches any entry in the list, classify it as **WEAK**.
- This part should not consider any demographic data such as birthdates or anniversaries — the analysis is based solely on pattern repetition and popularity.


### Part B: MPIN Strength Evaluation Using Demographic Data (4-digit MPIN)

- Enhance the MPIN checker to accept additional user demographic inputs:
  - Date of Birth (DOB)
  - Wedding Anniversary
  - Spouse's Date of Birth
- The program should analyze whether the entered 4-digit MPIN corresponds to any recognizable patterns derived from these personal dates.
- Output the MPIN strength as **WEAK** or **STRONG**.


### Part C: MPIN Strength Analysis with Detailed Weakness Reasons (4-digit MPIN)
- Extend the program to output not just the MPIN strength, but also the specific reasons if the MPIN is identified as WEAK.
- The output should include:
  - Strength: **WEAK** or **STRONG**
  - If weak then the reason why was it considered weak: It should give from the following the reasons as an array:
     - `COMMONLY_USED`
     - `DEMOGRAPHIC_DOB_SELF`
     - `DEMOGRAPHIC_DOB_SPOUSE`
     - `DEMOGRAPHIC_ANNIVERSARY`
  - If the MPIN is considered STRONG, the reasons array must be empty.

  
### Part D: Extended Support for 6-Digit MPINs
- Enhance the system to support validation for both 4-digit and 6-digit MPINs.
- All checks from previous parts — including common pattern detection and demographic-based combinations — should be adapted accordingly for 6-digit inputs.

# 🔧 Implementation Overview
The project is implemented using Python, organized into modular functions, and can be run via a Jupyter Notebook or a Streamlit web app. The core logic resides in the file mpin_strength_analyzer_shubham_gusain.py.

### Key components of the implementation include:
  - A predefined list of commonly used MPINs for both 4-digit and 6-digit formats.
  - Utility functions to generate date-based combinations from demographic inputs such as:
     - `Day, Month, Year`
     - `Reversed year`
     - `All meaningful 4- and 6-digit patterns`
     - `Reversed Year`
   - A main evaluator function that checks:
      - `If the MPIN is commonly used`
      - `If it matches any demographic-based pattern`
      - `Returns both strength (WEAK/STRONG) and reasons`
   - A comprehensive test suite with 50 test cases to verify all conditions across Part A–D.
   - A user-friendly Streamlit interface for input and live testing.


## 🧰 Setup Instructions

### 1. Clone the Repository

```bash
git clone <https://github.com/Shubham0x1/MPIN-Strength-Analyzer>
cd <repo-directory>
```
### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```
### 3.  Run the Streamlit App

```bash
streamlit run app.py
```
# Sample Executions

## Part A – Sample Test Case
![Screenshot 2025-07-16 230457.png](https://github.com/Shubham0x1/MPIN-Strength-Analyzer/blob/main/screenshots/Screenshot%202025-07-16%20230457.png)

##  Part B – Sample Test Case
![Screenshot 2025-07-16 230737.png](https://github.com/Shubham0x1/MPIN-Strength-Analyzer/blob/main/screenshots/Screenshot%202025-07-16%20230737.png)

## Part C – Sample Test Cases with Strength & Reasons

### Test Case 1: WEAK — DOB-SELF Match
![Screenshot 2025-07-16 231023.png](https://github.com/Shubham0x1/MPIN-Strength-Analyzer/blob/main/screenshots/Screenshot%202025-07-16%20231023.png)

### Test Case 2: WEAK — (DOB-SELF + Anniversary Match)
![Screenshot 2025-07-16 231144.png](https://github.com/Shubham0x1/MPIN-Strength-Analyzer/blob/main/screenshots/Screenshot%202025-07-16%20231144.png)

### Test Case 3: STRONG MPIN
![Screenshot 2025-07-16 231321.png](https://github.com/Shubham0x1/MPIN-Strength-Analyzer/blob/main/screenshots/Screenshot%202025-07-16%20231321.png)

## Part D – Sample Test Cases (6-digit MPIN Support)

### Test Case 1: WEAK — Commonly Used 6-digit MPIN
![Screenshot 2025-07-16 232135.png](https://github.com/Shubham0x1/MPIN-Strength-Analyzer/blob/main/screenshots/Screenshot%202025-07-16%20232135.png)

### Test Case 2: WEAK — Matches Demographic(DOB-SELF Match)
![Screenshot 2025-07-16 232241.png](https://github.com/Shubham0x1/MPIN-Strength-Analyzer/blob/main/screenshots/Screenshot%202025-07-16%20232241.png)

### Test Case 3: STRONG — Secure 6-digit MPIN
![Screenshot 2025-07-16 232411.png](https://github.com/Shubham0x1/MPIN-Strength-Analyzer/blob/main/screenshots/Screenshot%202025-07-16%20232411.png)


## ✍️ Author

**Shubham Gusain**  
🔗 [GitHub](https://github.com/Shubham0x1)  
📧 shubhamgusain886@gmail.com
