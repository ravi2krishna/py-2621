These tasks are designed specifically for **beginners who have learned conditionals** and gradually move from simple to real-world scenarios.

---

# 🟢 IF Statement Tasks (5)

> Use only `if` (no else)

### Task 1: Positive Number Checker

Ask the user to enter a number.

* If the number is positive, print:

```text
Positive Number
```

---

### Task 2: Voting Eligibility

Ask for age.

* If age is 18 or above, print:

```text
Eligible to Vote
```

---

### Task 3: Discount Coupon

Ask for purchase amount.

* If amount is greater than 5000, print:

```text
Coupon Applied
```

---

### Task 4: Free Delivery

Ask for order value.

* If order value is greater than 1000, print:

```text
Free Delivery Available
```

---

### Task 5: Login Notification

Ask for username.

* If username is `"admin"`, print:

```text
Welcome Admin
```

---

# 🟡 IF-ELSE Tasks (5)

> Two possible outcomes

### Task 1: Even or Odd

Ask for a number.

* If even → print "Even"
* Else → print "Odd"

---

### Task 2: ATM PIN Validation

Store:

```python
actual_pin = 1234
```

Ask user for PIN.

* Correct → Transaction Success
* Wrong → Transaction Failed

---

### Task 3: Pass or Fail

Ask marks.

* Marks >= 35 → Pass
* Else → Fail

---

### Task 4: Login Validation

Store:

```python
password = "python123"
```

Ask user password.

* Correct → Login Successful
* Else → Incorrect Password

---

### Task 5: Balance Check

Ask withdrawal amount.

Balance:

```python
balance = 5000
```

* Amount <= balance → Withdrawal Success
* Else → Insufficient Balance

---

# 🟠 ELIF Tasks (5)

> Multiple conditions

### Task 1: Grade Calculator

```text
90+ → A
75+ → B
50+ → C
35+ → D
Else → Fail
```

---

### Task 2: Income Tax Slab

```text
Income > 10 Lakhs → 30%
Income > 5 Lakhs → 20%
Income > 2 Lakhs → 10%
Else → No Tax
```

---

### Task 3: Employee Bonus

```text
Experience >= 10 → 30% Bonus
Experience >= 5 → 20% Bonus
Experience >= 2 → 10% Bonus
Else → No Bonus
```

---

### Task 4: Internet Speed Rating

```text
Speed >= 100 → Excellent
Speed >= 50 → Good
Speed >= 20 → Average
Else → Slow
```

---

### Task 5: Movie Ticket Pricing

```text
Age < 5 → Free
Age < 18 → ₹100
Age < 60 → ₹200
Else → ₹150
```

---

# 🔵 MATCH-CASE Tasks (5)

> Best for menus and fixed options

### Task 1: Day Finder

Input:

```text
1 → Monday
2 → Tuesday
3 → Wednesday
...
```

---

### Task 2: ATM Menu

```text
1 → Deposit
2 → Withdraw
3 → Balance
4 → Exit
```

Use `match-case`.

---

### Task 3: Food Ordering System

```text
1 → Burger
2 → Pizza
3 → Pasta
4 → Sandwich
```

Print selected item.

---

### Task 4: Student Course Selection

```text
1 → Python
2 → Java
3 → DevOps
4 → Data Science
```

Display course details.

---

### Task 5: Calculator Menu

```text
1 → Addition
2 → Subtraction
3 → Multiplication
4 → Division
```

Take two numbers and perform the selected operation using `match-case`.

---

# 🚀 Challenge Task (Combines Everything)

### Student Login Portal

1. Ask username and password
2. Validate using `if-else`
3. After successful login show menu using `match-case`

```text
1. View Profile
2. Change Password
3. Logout
```

4. Use `elif` for role-based access:

```text
Marks >= 90 → Gold Student
Marks >= 75 → Silver Student
Marks >= 50 → Bronze Student
```

* `if`
* `if-else`
* `elif`
* `match-case`
* input handling
* real-world logic

Perfect as a mini assignment after completing conditionals.
