age = int(input("What Is Your Age ?  ").strip())

unit = input("""Which Unit You want TO calculate Your Age?
Months
Weeks
Days
hours
All
""").strip().lower()

# الحسابات بتتعمل مرة واحدة هنا لكل البرنامج
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24

# غيرنا الاسم من all لـ age_outputs عشان نبعد عن الكلمات المحجوزة
age_outputs = [months, weeks, days, hours] 

if unit == "months": 
  print("The Chosen Unit Is Months")
  print(f"Your Age In Months Is {months}")

elif unit == "weeks":
  print("The Chosen Unit Is Weeks")
  print(f"Your Age In Weeks Is {weeks}")

elif unit == "days":
  print("The Chosen Unit Is Days")
  print(f"Your Age In Days Is {days}")

elif unit == "hours":
  print("The Chosen Unit Is Hours")
  print(f"Your Age In Hours Is {hours}")

elif unit == "all":
  print("The Chosen Unit Is All")
  print(f"Your Age In Months Is: {months}")
  print(f"Your Age In Weeks Is: {weeks}")
  print(f"Your Age In Days Is: {days}")
  print(f"Your Age In Hours Is: {hours}")

else:
  print("Invalid Unit")
