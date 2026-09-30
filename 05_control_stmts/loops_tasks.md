
# 🟢 FOR LOOP TASKS (5)

> Goal: Understand repetition

---

## Task 1: Print Numbers 1 to 10

Output:

```text id="8wbtro"
1
2
3
...
10
```

---

## Task 2: Print Even Numbers

Output:

```text id="xwot26"
2
4
6
8
10
...
50
```

---

## Task 3: Multiplication Table

Input:

```text id="iqr4b0"
5
```

Output:

```text id="yjlwm0"
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

---

## Task 4: Sum of Numbers

Calculate:

```text id="0ofjv0"
1 + 2 + 3 + ... + 100
```

---

## Task 5: Count Vowels

Input:

```text id="jh7jfe"
DigitalEdify
```

Output:

```text id="c6gvg4"
Vowels = 5
```

---

# 🟡 WHILE LOOP TASKS (5)

> Goal: Unknown number of repetitions

---

## Task 1: Countdown Timer

Input:

```text id="ydz4hq"
10
```

Output:

```text id="mjlwmj"
10
9
8
...
1
Time Up
```

---

## Task 2: ATM PIN Validation

3 attempts only.

```text id="5y5yce"
Correct PIN -> Login Success
Wrong PIN -> Try Again
```

---

## Task 3: Password Retry

Keep asking until:

```text id="cckm74"
python123
```

is entered.

---

## Task 4: Guess the Number

Secret Number:

```python id="ayf4vn"
7
```

Keep asking until user guesses correctly.

---

## Task 5: Deposit Until Target Reached

Target:

```text id="h3hvui"
10000
```

Keep accepting deposits until balance reaches target.

---

# 🟠 LOOP + BREAK TASKS (5)

---

## Task 1: Login System

Correct credentials:

```python id="ojtrz7"
username = "admin"
password = "admin123"
```

Use break when login succeeds.

---

## Task 2: Product Search

Search:

```text id="8n6jsd"
Laptop
```

Stop once found.

---

## Task 3: Student Search by ID

Find:

```text id="e5wx36"
Student ID = 105
```

Stop searching after match.

---

## Task 4: First ERROR in Log File

```python id="dmlhl6"
logs = ["INFO", "INFO", "ERROR", "INFO"]
```

Print first ERROR and stop.

---

## Task 5: Exit Menu

Menu:

```text id="lpjlwm"
1. Deposit
2. Withdraw
3. Exit
```

Use break for Exit.

---

# 🔵 LOOP + CONTINUE TASKS (5)

---

## Task 1: Skip Negative Numbers

```python id="rpb5m2"
[10, -5, 20, -8, 30]
```

Output:

```text id="lq1g5g"
10
20
30
```

---

## Task 2: Skip Failed Students

Marks:

```python id="mj8a4f"
[90, 25, 80, 30, 75]
```

Skip marks below 35.

---

## Task 3: Skip Maintenance Servers

```python id="rdg6zm"
["web1", "maintenance", "db1"]
```

Ignore maintenance server.

---

## Task 4: Skip Empty Names

```python id="zjlwm6"
["Ravi", "", "John", ""]
```

Print valid names only.

---

## Task 5: Skip Invalid PIN Length

If PIN is not 4 digits:

```text id="3otvnd"
Skip and ask again
```

---

# 🔴 NESTED LOOP TASKS (5)

> Goal: Process data inside data

---

## Task 1: Seating Arrangement

Generate:

```text id="0m1p0d"
A1 A2 A3
B1 B2 B3
C1 C2 C3
```

---

## Task 2: School Marks System

Students:

```python id="mjlwm2"
3 Students
4 Subjects
```

Accept marks for every student and every subject.

---

## Task 3: Employee Attendance

```python id="mjlwm3"
5 Employees
7 Days
```

Mark attendance for each employee every day.

---

## Task 4: DevOps Monitoring

Servers:

```python id="w1vcgt"
["web1", "web2", "db1"]
```

Services:

```python id="8xikq0"
["Apache", "Docker", "Nginx"]
```

Check every service on every server.

---

## Task 5: Multiplication Grid

Generate:

```text id="cjlwm4"
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25
```

---

# ⚫ ADVANCED NESTED LOOP TASKS (Real World)

---

## Task 1: Shopping Cart

Customers:

```python id="jlwm5"
3 Customers
```

Each customer has:

```python id="jlwm6"
5 Products
```

Calculate total bill.

---

## Task 2: ATM Transaction History

```python id="jlwm7"
5 Customers
10 Transactions Each
```

Print all transactions.

---

## Task 3: Log File Analyzer

```python id="jlwm8"
10 Files
100 Lines Each
```

Count ERROR occurrences.

---

## Task 4: Quiz Application

```python id="jlwm9"
5 Students
10 Questions
```

Store and evaluate answers.

---

## Task 5: LMS Project 

```text id="mjlwm0"
3 Students
4 Courses
```

For every student:

* Register courses
* Calculate course count
* Display report

---

# 🚀 Challenge Project (Combines Everything)

### Mini ATM System

Features:

```text id="wjlgk1"
Login
Deposit
Withdraw
Balance Check
Transaction History
Exit
```