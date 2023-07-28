Month_Conversions = {
    "Jan": "January:",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
# Keys don't have to be strings, they can be numbers or anything else, they just need to be unique. 
print(Month_Conversions)

print(Month_Conversions["Nov"])
print(Month_Conversions.get("Dec"))
print(Month_Conversions.get("eee"))
print(Month_Conversions.get("EEE", "Not a valid month abbreviation."))
