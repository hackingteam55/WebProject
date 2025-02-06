dict = {"nume": "Oltean",
        "prenume": "Matei"}


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.update({"year": 2020})

x = thisdict.get("model")

print(dict)
print(dict["nume"])
print(x)
print(thisdict["year"])

