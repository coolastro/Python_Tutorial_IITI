from PlSys_Classes import Star
from PlSys_Classes import Planet

class PlanetarySystem:
    """
     Class to construct the Planetary system by combining the Star and Planet Class.

     Args:
        name (str)                : Name of Planetary System \n
        central_star (Star class) : Instance created using the Star class \n
        planetlist (list)         : List of Instances created using the Planet Class.

    """
    def __init__(self, name, central_star, planetlist):
        self.name = name
        self.star = central_star
        self.planets = planetlist

    def __str__(self):
        string = ''
        string += '\n' + '*' * 33 + '\n'
        string += '*** Welcome to the %s ***\n' % self.name
        string += '*' * 33 + '\n'
        string += 'The central star has following properties\n'
        string += 'Mass : %.2f,  Radius : %.2f\n\n'%(self.star.mass, self.star.radius)
        string += 'That has %d planets with names - \n'% len(self.planets)
        for p in self.planets:
            string += '%s \n' % p.p_name

        string += 'Out of which following planets have life - \n'
        for plf in self.get_planets_with_life():
            string += '%s\n'%plf

        return string
    
    def get_planets_with_life(self):
	"""
	Prints the planet name which has exsistence of life from the given list.

	Returns:
	    A list of planet names with life.

	"""
        pl_w_life = []
        for planet in self.planets:
            if planet.has_life == True:
                pl_w_life.append(planet.p_name)
        return pl_w_life

if __name__=="__main__":
    Sun = Star(1.0,1.0)
    pl1 = Planet('Mercury', 0.03, 0.2, 0.01, 0.1, 5.0, False)
    pl2 = Planet('Venus', 0.06, 0.5, 0.1, 0.5, 7.0, False)
    pl3 = Planet('Earth', 1.0, 2.0, 0.1, 1.0, 10.0, True)
    pl4 = Planet('Jupiter', 50.0, 20.0, 0.1, 10.0, 100.0, False)
    pllist = [pl1, pl2, pl3, pl4]
    ps = PlanetarySystem('Solar System',Sun, pllist)
    print ps
