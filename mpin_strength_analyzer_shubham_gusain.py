"""MPIN_Strength_Analyzer_Shubham_Gusain
Original file is located at
    https://colab.research.google.com/drive/19wbL7FiONRK9Jy77mhFRy1c6kA8GDUUk
"""

COMMONLY_USED_MPINS_4 = {
    "1234", "0000", "1111", "2222", "3333", "4444",
    "5555", "6666", "7777", "8888", "9999", "1122",
    "1212", "1313", "6969", "4321", "1004", "2000",
    "2580", "0987", "1010", "1478", "3690", "0110", "1221"
}

COMMONLY_USED_MPINS_6 = {
    "123456", "000000", "111111", "654321", "121212",
    "112233", "999999", "159753", "123123", "789456",
    "101010", "123321", "456789", "121314", "111222",
    "314159", "777777", "010101"
}

# Determine if the given MPIN is widely known or predictable based on common usage patterns.
def is_predictable_mpin(pin):
    length = len(pin)

    if length == 4:
        return pin in COMMONLY_USED_MPINS_4
    elif length == 6:
        return pin in COMMONLY_USED_MPINS_6

    return False

# Demographic-based 4-digit MPIN pattern combinations derived from user dates:

# 1. Day + Month → e.g., DOB 02-04-1998 → "0204"
# 2. Month + Day → reversed version of above → "0402"
# 3. Last two digits of year + Day → e.g., 1998 & 11 → "9811"
# 4. Day + Last two digits of year → reversed form of above → "1198"
# 5. Last two digits of year + Month → e.g., 1998 & Dec (12) → "9812"
# 6. Month + Last two digits of year → reverse → "1298"
# 7. Repeat of year_short (last two digits of year) → e.g., 1998 → "9898"
# 8. Repeat of day → e.g., Day 09 → "0909"
# 9. Repeat of month → e.g., Month 08 → "0808"
# 10. Reversed last two digits of year + Day → e.g., 1998 → "89" + Day 13 → "8913"
# 11. Day + reversed last two digits of year → reverse of above → "1389"
# 12. Month + Month + Day + Day → e.g., 06-06-15 → "060615" (used in 6-digit but can be sliced)
# 13. Full year (1998) sliced as first 2 digits + last 2 digits → "1998" → "1998" (direct use)
# 14. Common symmetrical patterns derived from dates → "1221", "2112", etc.
# These combinations are commonly used due to their memorability and direct personal connection,
# but pose a risk because they are easily guessable by someone who knows user’s birth or anniversary data.

def extract_date_combinations(date, pin_length=None):
    """
    Extracts all possible 4- and 6-digit MPIN combinations from a given date
    using realistic user patterns based on day, month, and year.

    Args:
        date (str): Input date in 'DD-MM-YYYY' format.
        pin_length (int): Optional filter to return only 4-digit or 6-digit patterns.

    Returns:
        List[str]: A list of MPIN-like combinations derived from the date.
    """
    if not date or len(date.split('-')) != 3:
        return []

    day, month, year = date.strip().split('-')
    day = day.zfill(2)
    month = month.zfill(2)
    year_short = year[-2:]
    year_short_rev = year_short[::-1]

    combos = set()

    # Common 4-digit patterns (used by users to create MPINs)
    four_digit = {
        day + month,         # 0204
        month + day,         # 0402
        year_short + day,    # 9802
        day + year_short,    # 0298
        year_short + month,  # 9812
        month + year_short,  # 1298
        year_short + year_short,  # 9898
        day + day,           # 0202
        month + month,       # 0404
        year_short_rev + day,  # 8998 -> 8998 (reverse 98 = 89 + day)
        day + year_short_rev,  # 1389
    }

    # Extended 6-digit patterns
    six_digit = {
        day + month + year_short,       # 020498
        day + year_short + month,       # 029804
        month + day + year_short,       # 040298
        month + year_short + day,       # 049802
        year_short + day + month,       # 980204
        year_short + month + day,       # 980402
        year_short + year_short + day,  # 989802
        day + day + year_short,         # 020298
        day + month + year_short_rev,   # 020489
        month + month + year_short,     # 040498
        year_short + day + day,         # 9802 + 02
        month + day + day,              # 0402 + 02
        day + day + month,              # 0202 + 04
        year_short + year_short + year_short,  # 989898
    }

    if pin_length == 4:
        combos.update(four_digit)
    elif pin_length == 6:
        combos.update(six_digit)
    else:
        combos.update(four_digit)
        combos.update(six_digit)

    return sorted(combos)

def is_commonly_used_pin(pin):
    """
    Checks if the given MPIN is considered commonly used (i.e., weak due to predictability).

    A pin is flagged as 'common' if:
    - It's a well-known or frequently chosen 4-digit MPIN (e.g., 1234, 0000)
    - Or a predictable 6-digit MPIN (e.g., 123456, 111111)

    Args:
        pin (str): The MPIN to check (should be a 4- or 6-digit numeric string)

    Returns:
        bool: True if the pin is in the known list of commonly used MPINs, else False
    """
    if len(pin) == 4:
        return pin in COMMONLY_USED_MPINS_4
    elif len(pin) == 6:
        return pin in COMMONLY_USED_MPINS_6
    return False  # For any other lengths, assume it's not common

def check_strength(pin, DOB=None, Spouse_DOB=None, Wedding_Anniversary=None):
    """
    Evaluates the strength of a given MPIN based on:
    - Whether it is commonly used
    - Whether it matches any pattern from user demographics

    Args:
        pin (str): The MPIN to evaluate.
        DOB (str): User's date of birth in DD-MM-YYYY format.
        Spouse_DOB (str): Spouse's DOB (optional).
        Wedding_Anniversary (str): Anniversary date (optional).

    Returns:
        Tuple[str, List[str]]: A tuple containing:
            - Strength: 'WEAK', 'STRONG', or 'INVALID_LENGTH'
            - Reasons: A list of matched weakness reasons (empty if strong)
    """
    if len(pin) not in [4, 6]:
        return "INVALID_LENGTH", []

    reasons = []

    # Check for common patterns
    if is_commonly_used_pin(pin):
        reasons.append("COMMONLY_USED")

    # Check demographic matches
    if DOB and pin in extract_date_combinations(DOB, len(pin)):
        reasons.append("DEMOGRAPHIC_DOB_SELF")

    if Spouse_DOB and pin in extract_date_combinations(Spouse_DOB, len(pin)):
        reasons.append("DEMOGRAPHIC_DOB_SPOUSE")

    if Wedding_Anniversary and pin in extract_date_combinations(Wedding_Anniversary, len(pin)):
        reasons.append("DEMOGRAPHIC_ANNIVERSARY")

    if reasons:
        return "WEAK", reasons
    else:
        return "STRONG", []

def check_strength_reason(pin, DOB=None, Spouse_DOB=None, Wedding_Anniversary=None):
    """
    Analyzes the strength of a given MPIN (4 or 6 digits) based on:
    1. Commonly used PIN patterns
    2. Demographic-based matches from DOB, Spouse DOB, and Wedding Anniversary

    Args:
        pin (str): The MPIN to evaluate.
        DOB (str, optional): User's Date of Birth in 'DD-MM-YYYY' format.
        Spouse_DOB (str, optional): Spouse's Date of Birth in 'DD-MM-YYYY' format.
        Wedding_Anniversary (str, optional): Wedding Anniversary in 'DD-MM-YYYY' format.

    Returns:
        Tuple[str, List[str]]:
            - Strength as 'WEAK', 'STRONG', or 'INVALID_LENGTH'
            - Reasons for weakness (empty if strong)
    """
    reasons = []

    if len(pin) not in [4, 6]:
        return "INVALID_LENGTH", []

    if is_commonly_used_pin(pin):
        reasons.append("COMMONLY_USED")

    date_sources = [
        (DOB, "DEMOGRAPHIC_DOB_SELF"),
        (Spouse_DOB, "DEMOGRAPHIC_DOB_SPOUSE"),
        (Wedding_Anniversary, "DEMOGRAPHIC_ANNIVERSARY")
    ]

    for date, label in date_sources:
        if date:
            combos = extract_date_combinations(date, len(pin))
            if pin in combos:
                reasons.append(label)

    strength = "WEAK" if reasons else "STRONG"
    return strength, reasons

def run_test_cases():
    """
    Runs a suite of 50 test cases for the MPIN strength evaluator.
    Each test checks both the predicted strength and the exact list of weakness reasons.
    """

    tests = [
        # Commonly used 4-digit PINs
        ("0000", None, None, None, "WEAK", ["COMMONLY_USED"]),
        ("2580", None, None, None, "WEAK", ["COMMONLY_USED"]),
        ("4321", None, None, None, "WEAK", ["COMMONLY_USED"]),
        ("1212", None, None, None, "WEAK", ["COMMONLY_USED"]),
        ("1313", None, None, None, "WEAK", ["COMMONLY_USED"]),

        # Commonly used 6-digit PINs
        ("000000", None, None, None, "WEAK", ["COMMONLY_USED"]),
        ("010101", None, None, None, "WEAK", ["COMMONLY_USED"]),
        ("112233", None, None, None, "WEAK", ["COMMONLY_USED"]),
        ("123456", None, None, None, "WEAK", ["COMMONLY_USED"]),
        ("123123", None, None, None, "WEAK", ["COMMONLY_USED"]),

        # Demographic match (DOB 4-digit)
        ("0201", "02-01-1998", None, None, "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
        ("1004", "04-10-2000", None, None, "WEAK", ["COMMONLY_USED", "DEMOGRAPHIC_DOB_SELF"]),
        ("1212", "12-12-2012", None, None, "WEAK", ["COMMONLY_USED", "DEMOGRAPHIC_DOB_SELF"]),
        ("0102", "02-01-1998", None, None, "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
        ("9802", "02-01-1998", None, None, "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),

        # Demographic match (DOB 6-digit)
        ("020198", "02-01-1998", None, None, "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
        ("021998", "02-01-1998", None, None, "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
        ("981102", "02-11-1998", None, None, "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
        ("891302", "02-03-1989", None, None, "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
        ("1389", "13-08-1989", None, None, "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),

        # Spouse DOB matches
        ("101290", None, "10-12-1990", None, "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
        ("1990", None, "10-12-1990", None, "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
        ("100419", None, "10-04-2019", None, "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
        ("0212", None, "02-12-1990", None, "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
        ("9803", None, "03-08-1998", None, "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),

        # Wedding Anniversary matches
        ("150815", None, None, "15-08-2015", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
        ("1506", None, None, "15-06-2015", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
        ("060615", None, None, "06-06-2015", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
        ("0808", None, None, "08-08-2008", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
        ("888888", None, None, "08-08-1988", "WEAK", ["COMMONLY_USED", "DEMOGRAPHIC_ANNIVERSARY"]),

        # Multiple demographics
        ("0212", "02-12-1990", "12-02-1990", None, "WEAK", ["DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_DOB_SPOUSE"]),
        ("1515", "15-08-1992", None, "15-08-2015", "WEAK", ["DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_ANNIVERSARY"]),
        ("0202", "02-02-1990", "02-02-1990", "02-02-1990", "WEAK", ["DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_DOB_SPOUSE", "DEMOGRAPHIC_ANNIVERSARY"]),
        ("9999", "09-09-1999", None, None, "WEAK", ["COMMONLY_USED", "DEMOGRAPHIC_DOB_SELF"]),
        ("1001", "01-10-1998", None, "10-01-1998", "WEAK", ["COMMONLY_USED", "DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_ANNIVERSARY"]),

        # Invalid PIN lengths
        ("12", None, None, None, "INVALID_LENGTH", []),
        ("123", None, None, None, "INVALID_LENGTH", []),
        ("12345", None, None, None, "INVALID_LENGTH", []),
        ("1234567", None, None, None, "INVALID_LENGTH", []),
        ("", None, None, None, "INVALID_LENGTH", []),

        # Strong MPINs
        ("8392", "01-02-1990", "03-04-1991", "05-06-1992", "STRONG", []),
        ("839201", "01-02-1990", "03-04-1991", "05-06-1992", "STRONG", []),
        ("7594", None, None, None, "STRONG", []),
        ("930284", None, None, None, "STRONG", []),
        ("987654", None, None, None, "STRONG", []),
        ("101938", "01-01-2000", None, None, "STRONG", []),
        ("001122", "03-06-2001", None, None, "STRONG", []),
        ("293847", None, None, None, "STRONG", []),
        ("029384", None, None, None, "STRONG", []),
        ("646464", None, None, None, "STRONG", []),
    ]

    passed_tests = 0
    total_tests = len(tests)

    for i, (pin, dob, spouse_dob, anniversary, expected_strength, expected_reasons) in enumerate(tests, 1):
        strength, reasons = check_strength_reason(pin, dob, spouse_dob, anniversary)
        strength_match = (strength == expected_strength)
        reasons_match = (sorted(reasons) == sorted(expected_reasons))
        passed = strength_match and reasons_match

        result = "✅ Passed" if passed else "❌ Failed"
        print(f"Test {i:02}: PIN={pin}, Strength={strength}, Reasons={reasons} → {result}")

        if passed:
            passed_tests += 1

    print(f"\n📊 Summary: {passed_tests}/{total_tests} tests passed.")

if __name__ == "__main__":
    run_test_cases()