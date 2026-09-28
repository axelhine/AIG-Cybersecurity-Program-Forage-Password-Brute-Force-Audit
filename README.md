# AIG Cybersecurity Program (Forage) — Password Brute-Force Audit

A password security simulation completed as part of the **AIG Cybersecurity Job Simulation** on [Forage](https://www.theforage.com/), a virtual work experience platform built in partnership with real companies including AIG.

## About This Project

This project simulates a real-world password security audit: attempting to brute-force a password-protected ZIP file using a common password dictionary ([`rockyou.txt`](rockyou.txt)), a wordlist widely used in security testing. The exercise demonstrates why weak or reused passwords are a serious organizational risk — a password found in a public breach dataset can often be cracked in seconds using automated tools like this one.

## Files in This Repository

- [`bruteforce.py`](bruteforce.py) — the brute-force script
- [`enc.zip`](enc.zip) — the password-protected archive being cracked
- [`rockyou.txt`](rockyou.txt) — the sample password wordlist used to guess the password
- [`ImportantFile.docx`](ImportantFile.docx) — the file recovered once the correct password is found

## How It Works

The script ([`bruteforce.py`](bruteforce.py)) opens a password-protected ZIP file and iterates through a list of candidate passwords, attempting extraction with each one until the correct password is found or the list is exhausted.

```python
def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        print(f"[+] Found password: {password.decode()}")
        exit(0)
    except:
        pass
```

## Why This Matters (Security Context)

This simulation illustrates a core GRC/security principle in practice: **password policy is a control, and weak controls are exploitable.** An organization that permits weak, common, or reused passwords is vulnerable to exactly this kind of automated attack. This is why frameworks like PCI DSS and SOC 2 explicitly require strong password management policies as a baseline control.

## How to Run

1. Clone or download this repository
2. Make sure Python 3 is installed
3. From inside the project folder, run:

​```
python bruteforce.py
​```

4. The script will attempt each password in [`rockyou.txt`](rockyou.txt) against [`enc.zip`](enc.zip) and print the correct password once found, then extract [`ImportantFile.docx`](ImportantFile.docx)

## Skills Demonstrated

- Practical understanding of brute-force attack methodology
- Python scripting fundamentals
- Password security auditing concepts
- Recognizing the real-world impact of weak password policies

---
*Completed as part of the AIG Cybersecurity Job Simulation on Forage.*
