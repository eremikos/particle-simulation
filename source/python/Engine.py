#!/usr/bin/python
import Particle

def joinVector(vector1, vector2):
    if (type(vector1) == type(vector2)):
        if (type(vector1) == list):
            if (len(vector1) == len(vector2)):
                for i in range(len(vector1)):
                    if ((type(vector1[i]) == list) or (type(vector2[i]) == list)):
                        raise TypeError, "TypeError: input elements must all be of numeric type"
                    elif ((type(vector1[i]) == str) or (type(vector2[i]) == str)):
                        raise TypeError, "TypeError: input elements must all be of numeric type"
                    else:
                        pass
                temp = []

                for j in range(len(vector1)):
                    value = vector1[j] + vector2[j]
                    temp.append(value)
                return temp
            else:
                raise IndexError, "IndexError: input lists must of equivalent length"
        else:
            raise TypeError, "TypeError: input must be of 'list' type"
    else:
        raise TypeError, "TypeError: input must both be equivalent type"

# Adjusting acceleration data for all Particle entities
def updateAcceleration():
    for i in range(len(x)):
        x[i].setAcceleration(0.0, 0.0, 0.0)
        for j in range(len(x)):
            if (i == j):
                pass
            else:
                temp = joinVector(x[i].getAcceleration(), x[i].adjustAcceleration(x[j]))
                x[i].setAcceleration(temp[0], temp[1], temp[2])

# Adjusting velocity data for all Particle entities
def updateVelocity():
    for i in range(len(x)):
        temp = x[i].adjustVelocity()
        x[i].setVelocity(temp[0], temp[1], temp[2])

# Adjusting position data for all Particle entities
def updatePosition():
    for i in range(len(x)):
        temp = x[i].adjustPosition()
        x[i].setPosition(temp[0], temp[1], temp[2])

def outputData():
    print x[0].getAcceleration()
    print x[1].getAcceleration()
    print x[2].getAcceleration()
    print ""
    print x[0].getVelocity()
    print x[1].getVelocity()
    print x[2].getVelocity()
    print ""
    print x[0].getPosition()
    print x[1].getPosition()
    print x[2].getPosition()
    print ""
    print ""

x = [Particle.main(), Particle.main(), Particle.main()]

# Initializing data for Particle <entity_1>
x[0].setName("Earth")
x[0].setMass(5.974*10**24)
x[0].setRadius(6.378*10**6)
x[0].setPosition(0.0,0.0,0.0)
x[0].setVelocity(0.0,0.0,0.0)
x[0].setAcceleration(0.0,0.0,0.0)

# Initializing data for Particle <entity_2>
x[1].setName("Luna")
x[1].setMass(7.342*10**22)
x[1].setRadius(1.7371*10**6)
x[1].setPosition(3.84399*10**8, 0.0, 0.0)
x[1].setVelocity(0.0,1022,0.0)
x[1].setAcceleration(0.0,0.0,0.0)

# Initializing data for Particle <entity_3>
x[2].setName("Apollo")
x[2].setMass(2.88*10**4)
x[2].setRadius(10.0)
x[2].setPosition(2.88299*10**8, 0.0, 0.0)
x[2].setVelocity(0.0, 1175.996, 0.0)
x[2].setAcceleration(0.0, 0.0, 0.0)

# All zeros, as per the initialization data   
outputData()

counter = 0
flag = True

while (flag):
    if (counter == 86400*30):
        # Originally meant as a break statement.
        pass
    else:
        if ((counter % 10000) == 0):
            print  "time is: ", counter, " seconds"
            outputData()
        else:
            pass
        
    updatePosition()
    updateVelocity()
    updateAcceleration()
    counter += 1

'''
    The <collision()> function may have to be adapted into the
    <Engine.py> file in order to work out the appropriate alterations
    to the members of the Particle object list, such as deleting a
    member when a collision occurs.

        # Copied above Particle collision functions to <Engine.py>
'''
