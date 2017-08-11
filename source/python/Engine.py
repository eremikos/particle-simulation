#!/usr/bin/python
import Particle

#from decimal import *
#getcontext().prec = 7


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
        '''
            Actually, I may want to make this into an
            initializer/updater function, as this will be pertinent
            to the event of a collision and a particle will be
            deleted from the Particle_list and the values of the
            accelerations acting on the new Particle_list will
            need to be updated.

            ### NEEDS EDITING. GIVES WRONG VALUES FOR N>2
                # Edit appears to be working                                    2017.08.07-22.03

                # Updater function works as desired(?)

            ### ADDITIONAL EDITING REQUIRED!                                    2017.08.08-05.23
                # It appears that the acceleration values being modified
                onto the Particle objects is being considered a cumulative
                value for epochs.
                
                EXAMPLE:
                
                    The following data is what was procured after allowing
                    updater functions (<ACC>, <VEL>, <POS>) to proceed
                    through approximately 80,000 (1-second) epochs.



                    time is: 80000 seconds

                    [0.7819421832570453, 9.620201612485454, -2.0341941140691503e-09]
                    [-63.62679094543965, -782.7977182417723, 1.6552277957318247e-07]
                    [-232.41266381594386, 634.3899658460448, 0.29340498878414933]

                    [58171.614822717725, 683320.0689375215, -0.00015133133754902393]
                    [-4733435.8658931535, -55600867.89167205, 0.012313861029484246]
                    [-17162038.504106753, 46240514.58502746, 21396.934850714857]

                    [2164022722.5871325, 24268718131.544968, -5.629626306458026]
                    [-175702560265.43665, -1974668659320.0513, 457.0838120413686]
                    [-633565385986.1945, 1685266951898.2249, 780217187.3613478]



                    As what can be seen here is the fact that the acceleration data
                    is much too high for what should be expected on any of the given
                    Particle objects. This flaw can also be observed on the velocity
                    and position data as well.

                    I believe the fault lies in how the <ACC> updater function operates
                    and this requires some modifications to determine whether that truly
                    is the case.

            ### UpdateAcceleration() function works now.
        '''
        
        x[i].setAcceleration(0.0, 0.0, 0.0)
        # was needed here.
        
        for j in range(len(x)):
            if (i == j):
                pass
            else:
                '''
                    I suspect the problem lies here.
                '''
                #x[i].setAcceleration(0.0, 0.0, 0.0)
                temp = joinVector(x[i].getAcceleration(), x[i].adjustAcceleration(x[j]))
                x[i].setAcceleration(temp[0], temp[1], temp[2])


def updateVelocity():
    for i in range(len(x)):
        temp = x[i].adjustVelocity() #joinVector(x[i].getVelocity(), x[i].adjustVelocity())
        x[i].setVelocity(temp[0], temp[1], temp[2])
        
def updatePosition():
    for i in range(len(x)):
        temp = x[i].adjustPosition()
        x[i].setPosition(temp[0], temp[1], temp[2])

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
print x[0].getAcceleration()
print x[1].getAcceleration()
print x[2].getAcceleration()
print ""
print x[0].getVelocity()
print x[1].getVelocity()
print x[2].getVelocity()
print""
print x[0].getPosition()
print x[1].getPosition()
print x[2].getPosition()
print ""
print ""
print ""

#updateAcceleration()
#updateVelocity()
#updatePosition()

counter = 0
flag = True

while (flag):
    if (counter == 86400*30):
        flag = False
    else:
        if ((counter % 10000) == 0):
            print "time is:", counter, "seconds"
            print ""
            print x[0].getAcceleration()
            print x[1].getAcceleration()
            print x[2].getAcceleration()
            print ""
            print x[0].getVelocity()
            print x[1].getVelocity()
            print x[2].getVelocity()
            print""
            print x[0].getPosition()
            print x[1].getPosition()
            print x[2].getPosition()
            print ""
            print ""
            print ""            
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
