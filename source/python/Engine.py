#!/usr/bin/python
import Particle

x = [Particle.main(), Particle.main(), Particle.main()]

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

# Initializing data for Particle <entity_3>
x[2].setName("Apollo")
x[2].setMass(2.88*10**4)
x[2].setRadius(10.0)
x[2].setPosition(2.88299*10**8, 6.2197*10**7, 1.61803*10**4)
x[2].setVelocity(0.0, 1175.996, 0.0)
x[2].setAcceleration(0.0, 0.0, 0.0)

# Adjusting acceleration data for all Particle entities
def updateAcceleration():
    for i in range(len(x)):
        '''
            Actually, I may want to make this into an
            initializer/updater function, as this will be pertinent
            to the event of a collision and a particle will be
            deleted from the Particle_list and the values of the
            accelerations acting on the new Particle_list will
            need to be updated.

            ### NEEDS EDITING. GIVES WRONG VALUES FOR N>2
                # Edit appears to be working 2017.08.07-22.03

                # Updater function works as desired
        '''

        for j in range(len(x)):
            if (j == i):
                continue
            else:
                clone = x[i].getAcceleration()
                temp = x[i].adjustAcceleration(x[j])

                for k in range(3):
                    copy = clone[k] + temp[k]
                    x[i].setAccIndex(k, copy)

# All zeros, as per the initialization data   
print x[0].getAcceleration()
print x[1].getAcceleration()
print x[2].getAcceleration()

updateAcceleration()

# New values, as per the graviational influences exerted 
print x[0].getAcceleration()
print x[1].getAcceleration()
print x[2].getAcceleration()
'''
    The <collision()> function may have to be adapted into the
    <Engine.py> file in order to work out the appropriate alterations
    to the members of the Particle object list, such as deleting a
    member when a collision occurs.
'''
