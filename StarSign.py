name = input("What is your name? ")
age = int(input("How old are you? "))
star_signs = {
    "1": "Pisces",
    "2": "Aquarius",
    "3": "Aries",
    "4": "Taurus",
    "5": "Gemini",
    "6": "Cancer",
    "7": "Leo",
    "8": "Virgo",
    "9": "Libra",
    "10": "Scorpio",
    "11": "Sagittarius",
    "12": "Capricorn"
}
while True:
    birthmonth = input("What is your birth month? ")
    if birthmonth in star_signs:
        starsign = star_signs[birthmonth]
        break
    else:
        print("Please enter a valid month")
pass
age_in_10_years = age + 10
print(f"Hello {name}, in 10 years you will be {age_in_10_years} years old and your star sign is {starsign}")
