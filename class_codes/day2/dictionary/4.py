avengers = {"ironman":"suit", "hawkeye":"arrows", "captain":["shield", "hammer"], "thor":"hammer"}
xmen = ["magneto", "wolverine"]

marvel = {"xmen":xmen, "ave":avengers}

print("marvel =", marvel)
print("-"*20)
print("marvel['ave'] =", marvel['ave'])
print("-"*20)
print("marvel['ave']['captain'] =", marvel['ave']['captain'])
print("marvel['ave']['captain'][0] =", marvel['ave']['captain'][0])
print("marvel['ave']['captain'][0][1] =", marvel['ave']['captain'][0][1])

