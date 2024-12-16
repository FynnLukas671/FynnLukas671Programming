contactInfo = {"Max": {"Telefon": "123456789", "Email": "max@example.com"},
               "Anna": {"Telefon": "987654321", "Email": "anna@example.com"},
               "Tom": {"Telefon": "456123789", "Email": "tom@example.com"}
               }

print(contactInfo["Anna"])

contactInfo.update({"Lisa": {"Telefon": "123456779", "Email": "lisa@example.com"}})
print(contactInfo)

contactInfo["Max"]["Telefon"] = "123456788"
print(contactInfo)

contactInfo.pop("Tom")
print(contactInfo)