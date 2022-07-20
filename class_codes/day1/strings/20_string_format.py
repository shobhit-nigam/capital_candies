name = "beth"
incentive = 12

print(name, "gets a", incentive, "percent incentive")

# newer style
print(f"{name.upper()} gets a {incentive-1} percent incentive")

# older style
print("{} gets a {} percent incentive".format(name.upper(), incentive))
