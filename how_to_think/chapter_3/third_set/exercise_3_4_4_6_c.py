people = ["Carrie", "Charlotte", "Sam", "Miranda"]

no_names_until_sam = 0
for name in people:
    if name == "Sam":
        break
    no_names_until_sam += 1

print("There are", no_names_until_sam, "names before Sam")
