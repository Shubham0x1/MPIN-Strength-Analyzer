# MPIN-Strength-Analyzer

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
![Screenshot 2025-07-16 195042.png](https://github.com/Shubham0x1/MPIN-Strength-Analyzer/blob/main/screenshots/Screenshot%202025-07-16%20195042.png)

