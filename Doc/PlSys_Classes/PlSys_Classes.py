import numpy as np
import scipy.constants as sci

class Star:
    """
    This class builds the framework to create a *Star* object
    with certain mass and radius.
    
    Class to create objects related stars. 
    
    Args:
	massin (float)   : Stellar Mass \n
	radiusin (float) : Radius of the star \n
    
    """
    grav = sci.G  # Gravitational constant

    def __init__(self, massin, radiusin):
        self.mass = massin
        self.radius = radiusin

    def get_surface_gravity(self):
        """
        Computes the surface gravity of the star from the mass and radius.
        """
        return Star.grav * self.mass / self.radius ** 2

    def __str__(self):
        """
        Prints the star object that is created in a fancy manner.
        """
        string = ''
        string += 'Mass is\t\t\t %.2f\n' % self.mass
        string += 'Radius is\t\t %.2f\n' % self.radius
        string += 'Surface gravity is\t %le\n' % self.get_surface_gravity()
        return string

    def __add__(self, other):
        """
        The formulae to add the masses and radii of two star objects.
        """
        return Star(self.mass + other.mass, np.sqrt(self.radius + other.radius))

    @staticmethod
    def get_spectral_types():
        """
        The static method that is common to all stars and defines the 
        spectral type of the star.
        """
        return ['O', 'B', 'A', 'F', 'G', 'K', 'M']


class Planet:
    """
    Framework to create a Planet class. 
    
    Args:
        p_name (str)   : Name of the Planet \n
        p_m    (float) : Mass of the Planet \n
        p_r    (float) : Radius of the Planet \n
        p_ecc  (float) : Eccentricity of the planet \n
        p_per  (float) : Period of the planet \n
        p_dist (float) : Distance of the planet \n
        has_life (bool): Flag indicating exsistence of Life
        
    Methods:
        get_surface_gravity - Computes the surface gravity from mass and radius
        
    StaticMethods:
        get_planetary_type  - Lists different types of planets. 
        
    Syntax:
        pl1 = Planet('ABC',2.0,4.0,6.0,8.0,10.0,False)
    
    """
    grav = sci.G
    
    def __init__(self, p_name, p_m, p_r, p_ecc, p_per, p_dist, has_life):
        self.p_name = p_name
        self.p_mass = p_m
        self.p_rad = p_r
        self.p_ecc = p_ecc
        self.p_per = p_per
        self.p_dist = p_dist
        self.has_life = has_life

    def get_surface_gravity(self):
	return Planet.grav*(self.p_mass/(self.p_rad**2))

    @staticmethod
    def get_planetary_type():
	return ['rocky','Puffy','Gas Giant', 'Unknown','Water World']

