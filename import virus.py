import virus

population = 10000
infected = 1
can_catch_virus = population - infected
contacts_per_day = 10
recovered_chicken = 0
day = 0

while day < 90 and infected > 0:
    if day >= 14:
        contacts_per_day = 3
    # Infected chickens spread the virus to those who haven't already had it.
    newly_infected = virus.spread(
        infected, can_catch_virus, population, contacts_per_day
    )
    daily_recovered = virus.recover(infected)
    recovered_chicken += daily_recovered
    infected = infected + newly_infected - daily_recovered
    can_catch_virus = can_catch_virus - newly_infected
    day += 1
    print(str(infected) + " chickens infected.")

print("----------")
print(str(population - can_catch_virus) + " chickens caught the virus.")
print(str(recovered_chicken) + " chickens recovered.")