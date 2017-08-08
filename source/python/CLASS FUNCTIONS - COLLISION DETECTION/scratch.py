### CLASS FUNCTIONS - COLLISION DETECTION/RESPONSE
'''
    I may need to make the subsequent functions of the Particle class
    for the collision detection part of the file for the actual running
    of the program (or rather, <Engine.py>) since it seems that the function
    for particle collision will not delete a constructed class object from
    inside of the class file itself, but it seems it will allow for it if
    it is done inside of the <Engine.py> file.

    Will need to ascertain the possibility of keeping the <collision> method
    inside of its pertainig class.
'''
# Unnecessary, may delete
def proximityAlert(flag):
    flag_list = ["0th Degree Contact: Avoidance.",
                 "1st Degree Contact: Wide Miss.",
                 "2nd Degree Contact: Near Miss.",
                 "3rd Degree Contatc: Collision!"]
    try:
        print flag_list[flag]
    except:
        raise AttributeError, "AttributeError: flag type"
        
def detectProximity(self, other, active = True):
    if (active):
        # If for some reason I do not wish for this to run always.
        proximity = self.distance(other)
        contact = self.getRadius() + other.getRadius()

        if (proximity < (10*contact)):
            proximityAlert(1)

            if (proximity < (3*contact)):
                proximityAlert(2)

                if (proximity <= contact):
                    proximityAlert(3)
                    collision(other)
                    
        else:
            proximityAlert(0)
    else:
        pass
