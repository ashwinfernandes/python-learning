scorpions = {"emperor", "red claw", "arizona", "forest", "fat tail"}
snakes = {"python", "cobra", "viper", "anaconda", "mamba"}
spiders = {"tarantula", "black widow", "wolf spider", "crab spider"}
vespas = {"yellow jacket", "hornet", "paper wasp"}

# Creatures that bite
creatures_that_bite = set()

# use update
creatures_that_bite.update(spiders)
creatures_that_bite.update(snakes)
print(creatures_that_bite)

# use unpacking operator
creatures_that_bite = {*spiders, *snakes}
print(creatures_that_bite)

# Creatures that sting

# use union
creatures_that_sting = scorpions.union(vespas)

# Arachnids

# use union operator
arachnids = scorpions | spiders
