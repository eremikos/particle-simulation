import Particle

x = [Particle.main(), Particle.main()]

# Initializing data for Particle <entity_1>
x[0].setName("Earth")
x[0].setMass(5.9742*10**24)
x[0].setRadius(6.378*10**6)
x[0].setPosition(0.0,0.0,0.0)
x[0].setVelocity(0.0,0.0,0.0)
x[0].setAcceleration(0.0,0.0,0.0)

# Initializing data for Particle <entity_2>
x[1].setName("Luna")
x[1].setMass(7.342*10**22)
x[1].setRadius(1.7371*10**6)
x[1].setPosition(3.84399*10**8, 1.0, -1.0)
x[1].setVelocity(0.0,1022,0.0)
x[1].setAcceleration(0.0,0.0,0.0)

# Adjusting acceleration data for all Particle entities
for i in range(len(x)):
    clone = x[i].getAcceleration()
    if (i == (len(x)-1)):
        temp = x[i].adjustAcceleration(x[0])
    else:
        temp = x[i].adjustAcceleration(x[i+1])

    for j in range(3):
        copy = clone[j] + temp[j]
        x[i].setAccIndex(j, copy)
    
