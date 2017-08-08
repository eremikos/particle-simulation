#!/usr/bin/python
from math import pi

attractor = 6.67384*(10**-11)
delta = pow(10.0, 0.0)

class main(object):

    def __init__(self):
    #class constructor(?)
            # private class members(?)
        #self.attractor = 6.67384*(10**-11) #meters^3 / kg * s^2
        #self.delta = pow(10.0, -3.0)
        '''
            I may not want the above two variables where they are located,
            especially so for <attractor> as it should remain static upon
            runtime of the code.
        '''

        self.name = None
        self.mass = None
        self.radius = None

        self.position = [None, None, None]
        self.velocity = [None, None, None]
        self.acceleration = [None, None, None]

### INPUT VALIDATORS

    def isCharacter(self, inputVar):
        if (type(inputVar) == str):
            pass
        else:
            raise TypeError, "TypeError: unsupported input type"
        return True

    def isNumeric(self, inputVar):
        if (type(inputVar) == int):
            pass
        elif(type(inputVar) == float):
            pass
        elif(type(inputVar) == long):
            pass
        else:
            if (type(inputVar) == str):
                raise TypeError, "TypeError: unsupported input 'str' type"
            elif (inputVar is None):
                raise TypeError, "TypeError: unsupported input 'NoneType'"
            elif (type(inputVar) == list):
                raise TypeError, "TypeError: unsupported input 'list' type"
            elif (type(inputVar) == dict):
                raise TypeError, "TypeError: unsupported input 'dict' type"
            else:
                raise TypeError, "UnknownTypeError: unsupported input type"
        return True

### ASSIGN/RECALL CLASS MEMBER PROPERTY

    def setName(self, var):
        if self.isCharacter(var):
            self.name = var
            
    def getName(self):
        try:
            return self.name
        except AttributeError:
            raise AttributeError, "AttributeError: Particle <name> type"
    
    def setMass(self, var):
        if self.isNumeric(var):
            self.mass = var
            
    def getMass(self):
        try:
            return self.mass
        except AttributeError:
            raise AttributeError, "AttributeError: Particle <mass> type"

    def setRadius(self, var):
        if self.isNumeric(var):
            self.radius = var
            
    def getRadius(self):
        try:
            return self.radius
        except AttributeError:
            raise AttributeError, "AttributeError: Particle <radius> type"

    # POSITION
    def setPosIndex(self, index, var):
        if self.isNumeric(var):
            if (0 <= index < 3):
                self.position[index] = var
            else:
                raise IndexError, "IndexError: list index out of range"

    def getPosIndex(self, index):
        try:
            return self.position[index]
        except AttributeError:
            raise AttributeError, "AttributeError: Particle <position> type"

    def setPosition(self, posX, posY, posZ):
        self.setPosIndex(0, posX)
        self.setPosIndex(1, posY)
        self.setPosIndex(2, posZ)

    def getPosition(self):
        try:
            return self.position
        except:
            raise AttributeError, "AttributeError: Particle <position> vector type"

    # VELOCITY     
    def setVelIndex(self, index, var):
        if self.isNumeric(var):
            if (0 <= index < 3):
                self.velocity[index] = var
            else:
                raise IndexError, "IndexError: list index out of range"

    def getVelIndex(self, index):
        try:
            return self.velocity[index]
        except AttributeError:
            raise AttributeError, "AttributeError: Particle <velocity> type"

    def setVelocity(self, velX, velY, velZ):
        self.setVelIndex(0, velX)
        self.setVelIndex(1, velY)
        self.setVelIndex(2, velZ)

    def getVelocity(self):
        try:
            return self.velocity
        except:
            raise AttributeError, "AttributeError: Particle <velocity> vector type"

    def getVelScalar(self):
        try:
            velX = self.getVelIndex(0)
            velY = self.getVelIndex(1)
            velZ = self.getVelIndex(2)
            
            return (((velX**2) + (velY**2) + (velZ**2))**0.5)
        except:
            raise AttributeError, "AttributeError: Particle <velocity> scalar type"

    # ACCELERATION
    def setAccIndex(self, index, var):
        if self.isNumeric(var):
            if (0 <= index < 3):
                self.acceleration[index] = var
            else:
                raise IndexError, "IndexError: list index out of range"

    def getAccIndex(self, index):
        try:
            return self.acceleration[index]
        except AttributeError:
            raise AttributeError, "AttributeError: Particle <acceleration> type"

    def setAcceleration(self, accX, accY, accZ):
        self.setAccIndex(0, accX)
        self.setAccIndex(1, accY)
        self.setAccIndex(2, accZ)

    def getAcceleration(self):
        try:
            return self.acceleration
        except:
            raise AttributeError, "AttributeError: Particle <acceleration> vector type"

    def getAccScalar(self):
        try:
            accX = self.getAccIndex(0)
            accY = self.getAccIndex(1)
            accZ = self.getAccIndex(2)

            return (((accX**2) + (accY**2) + (accZ**2))**0.5)
        except:
            raise AttributeError, "AttributeError: Particle <acceleration> scalar type" 
                
### CLASS FUNCTIONS - BASIC PHYSICS

    def radialVector(self, other):
        clone = [self.position, other.position]
        rX = clone[0][0] - clone[1][0]
        rY = clone[0][1] - clone[1][1]
        rZ = clone[0][2] - clone[1][2]

        vector = [rX, rY, rZ]
        return vector
    
    def distance(self, other):
        clone = self.radialVector(other)
        return (((clone[0]**2) + (clone[1]**2) + (clone[2]**2))**0.5)

    def adjustAcceleration(self, other):
        '''
            Calculates the acceleration vector of <other> on <self> in the form:
            
            <self>.adjustAcceleration(<other>)
        '''
        gravitate = (attractor*other.getMass())/pow(self.distance(other), 3.0)
        
        clone = other.radialVector(self)
        clone[0] *= gravitate
        clone[1] *= gravitate
        clone[2] *= gravitate

        return clone

    def adjustVelocity(self):

        temp = list()
        
        for i in range(3):
            var = self.getVelIndex(i) + (self.getAccIndex(i)*delta)
            temp.append(var)

        return temp

    def adjustPosition(self):

        temp = list()

        for i in range(3):
            var = self.getPosIndex(i) + (self.getVelIndex(i)*delta) + (0.5*self.getAccIndex(i)*(delta**2))
            temp.append(var)

        return temp


        
            
                
