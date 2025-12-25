school_records = [] #Main List --> (All Records stored here)

while True:
    # --- Main Menu ---
    print("\n" + "=" * 40)
    print("   🏫  SCHOOL ATTENDANCE SYSTEM  🏫")
    print("=" * 40)
    print(" 1️⃣   Add New Attendance")
    print(" 2️⃣   Show Last Entry")
    print(" 3️⃣   Show All Records (Table View)")
    print(" 4️⃣   Remove a Record")
    print(" 5️⃣   Exit")
    print("=" * 40)

    # --- Error Handling ---
    try:
        num = int(input("👉 Select an option (1-5): "))
    except ValueError:
        print("❌ Error: Please enter a valid number.")
        continue

    # --- 1. Add Entry ---
    if num == 1:
        print("\n📝 --- NEW ENTRY ---")
        current_student = []

        # Name Input & Validation
        while True:
            name = input("   👤 Student Name: ").strip().title()
            if len(name) > 0 and name.replace(" ", "").isalpha():
                break
            print("   ⚠️ Invalid Name! Please use letters only.")

        # Grade Input & Validation
        while True:
            grade = input("   🎓 Class/Grade (e.g. 1A, G10): ").strip().upper()
            if len(grade) > 0:
                break
            print("   ⚠️ Grade cannot be empty.")

        # Date Input & Validation
        date = input("   📅 Date (DD/MM): ").strip()
        while True:
            if "/" in date:
                da = date.split("/")
                if len(da) == 2 and da[0].isdigit() and da[1].isdigit():
                    day = int(da[0])
                    month = int(da[1])
                    if 1 <= day <= 31 and 1 <= month <= 12:
                        date = f"{day:02d}/{month:02d}"
                        break
            date = input("   ️⚠️  ️Invalid input! Enter Date in this form (e.g. 05/12): ").strip()

        # Status Input & Validation
        status = input("   ❓ Status (Present/Absent): ").strip().capitalize()
        while status != "Present" and status != "Absent":
            print("   ⚠️ Invalid input! Choose 'Present' or 'Absent'.")
            status = input("   ❓ Status (Present/Absent): ").strip().capitalize()

        current_student = [name, grade, date, status]
        school_records.append(current_student)

        print(f"✅ Recorded successfully! ({name} is {status})")

    # --- 2. Show last Entry ---
    elif num == 2:
        if not school_records:
            print("\n📭 Database is empty.")
        else:
            last = school_records[-1]
            print("\n🔍 --- LAST RECORD ---")
            print(f"   👤 Name:   {last[0]}")
            print(f"   🎓 Class:  {last[1]}")
            print(f"   📅 Date:   {last[2]}")
            print(f"   📊 Status: {last[3]}")
            print(f"   🔢 Total Fields: {len(last)}")

    # --- 3. Show All Records ---
    elif num == 3:
        if not school_records:
            print("\n📭 Database is empty.")
        else:
            print("\n📋 --- ALL RECORDS ---")
            print("-" * 55)
            print(f"| {'ID':<3} | {'Name':<15} | {'Class':<6} | {'Date':<8} | {'Status':<8} |")
            print("-" * 55)

            for i in range(len(school_records)):
                student = school_records[i]
                print(f"| {i + 1:<3} | {student[0]:<15} | {student[1]:<6} | {student[2]:<8} | {student[3]:<8} |")

            print("-" * 55)
            print(f"📈 Total Students: {len(school_records)}")

    # --- 4. Remove a Record ---
    elif num == 4:
        if not school_records:
            print("\n📭 Nothing to delete.")
        else:
            print("\n🗑️  --- DELETE RECORD ---")
            try:
                recordNum = int(input(f"   Enter ID to delete (1-{len(school_records)}): "))
                while recordNum <= 0 or recordNum > len(school_records):
                    print("   ❌ Invalid ID.")
                    recordNum = int(input(f"   Enter Correct ID (1-{len(school_records)}): "))

                removed = school_records.pop(recordNum - 1)
                print(f"✅ Record for '{removed[0]}' deleted successfully.")

            except ValueError:
                print("❌ Please enter a valid number.")

    # --- 5. Exit ---
    elif num == 5:
        print("\n👋 Thanks for using School System. Goodbye!")
        break

    else:
        print("❌ Invalid choice! Please select 1-5.")