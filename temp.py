current_temperature = int(input("Enter today's temperature: "))
if current_temperature > 30:
    print("""
It's a hot day
Wear light clothes 
    """)
elif current_temperature < 10:
    print("It's a cold day.")
    print("Wear heavy clothes")
else:
    print("It's neither hot nor cold")