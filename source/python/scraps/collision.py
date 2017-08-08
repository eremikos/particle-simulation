def collision(self, other):
    '''
        Probably should delete this an just make the actions performed within
        this function a condition within the loop body.
    '''
    new_mass = self.getMass() + other.getMass()
    print new_mass
    new_radius = pow((((self.getRadius())**3.0)+((other.getRadius())**3.0)), 1/3.)
    print new_radius
    new_velocity = [0, 0, 0]

    for i in range(3):
        new_velocity[i] = self.getVelIndex(i) + other.getVelIndex(i)

    if (self.getMass() > other.getMass()):
        # Particle <self> is more massive; delete Particle <other>
        #del other
        flag = 1
    else:
        # Particle <other> is more massive; delete Particle <self>
        #del self
        flag = 0

    self.setMass(new_mass)

    return flag
