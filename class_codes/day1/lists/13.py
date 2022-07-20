# functions
avengers = ["ironman", "hawkeye", "Dr Strange", "black widow", "thor"]
marvel = ["mystique", "magneto"]

print("marvel =", marvel)
marvel.append(avengers)
print("after appending")
print("marvel =", marvel)

print("-------")

avengers = ["ironman", "hawkeye", "Dr Strange", "black widow", "thor"]
marvel = ["mystique", "magneto"]

print("marvel =", marvel)
marvel.extend(avengers)
print("after extending")
print("marvel =", marvel)



