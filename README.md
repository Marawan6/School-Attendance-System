# 🏫 School Attendance System

A robust, interactive **Command Line Interface (CLI)** application built with Python to manage student attendance records efficiently. This project demonstrates the implementation of CRUD operations (Create, Read, Delete) with strict data validation and a user-friendly interface.

## ✨ Features

### 1. 📝 Smart Data Entry
* **Name Validation:** Ensures names contain letters only (rejects numbers or symbols).
* **Grade Validation:** Prevents empty inputs.
* **Date Validation:** * Enforces `DD/MM` format.
    * Validates logical dates (e.g., Days 1-31, Months 1-12).
    * Auto-formats days/months (e.g., `5/5` becomes `05/05`).
* **Status Control:** Restricts input strictly to `'Present'` or `'Absent'`.

### 2. 📊 Dynamic Table View
* Displays all records in a beautifully formatted table.
* Uses **advanced string formatting** (Padding & Alignment) to keep columns perfectly aligned regardless of data length.

### 3. 🛡️ Safe Deletion
* Allows removing records by ID.
* Includes error handling to prevent crashing if an invalid ID is entered.

### 4. 🎨 User Experience (UX)
* Clean menu-driven interface.
* Emoji support for better visual cues.
* Clear error messages guide the user to correct inputs.

---

## 🛠️ Technical Concepts Applied
This project serves as a practical application of core Computer Science and Python concepts:
* **Data Structures:** Python Lists & Nested Lists for an in-memory database.
* **Control Flow:** `While` loops for robust input validation (guard clauses).
* **Exception Handling:** `Try/Except` blocks to manage `ValueError` and prevent crashes.
* **String Manipulation:** Methods like `.strip()`, `.title()`, `.split()`, `.isalpha()`, and f-strings.

---

## 🚀 How to Run

1.  **Prerequisites:** Ensure you have Python 3.x installed.
2.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YourUsername/School-Attendance-System.git](https://github.com/Marawan6/School-Attendance-System.git)
    ```
3.  **Navigate to the folder:**
    ```bash
    cd School-Attendance-System
    ```
4.  **Run the Application:**
    ```bash
    python school_attendance.py
    ```

---

## 📸 Usage Example

```text
========================================
   🏫  SCHOOL ATTENDANCE SYSTEM  🏫
========================================
 1️⃣   Add New Attendance
 2️⃣   Show Last Entry
 3️⃣   Show All Records (Table View)
 4️⃣   Remove a Record
 5️⃣   Exit
========================================
👉 Select an option (1-5): 3

📋 --- ALL RECORDS ---
-------------------------------------------------------
| ID  | Name            | Class  | Date       | Status   |
-------------------------------------------------------
| 1   | Marawan Mohamed | G12    | 25/12      | Present  |
| 2   | Ahmed Ali       | 10A    | 05/11      | Absent   |
-------------------------------------------------------
📈 Total Students: 2
