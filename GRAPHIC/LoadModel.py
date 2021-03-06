from direct.showbase.ShowBase import ShowBase
from panda3d.core import VBase4
from opensimplex import OpenSimplex
import math
import random
import copy

switch_exa = {
        "grass": "exa_grass.egg",
        "ice": "exa_ice.egg",
        "yellow": "Exa_yellow.egg",
        "desert": "exa_desert.egg",
        "rock": "exa_rock.egg",
        "water": "exa_water.egg"
        }

switch_animal = {
    "bear": "Bear.egg",
    "cow": "Cow.egg",
    "panther": "Panther.egg",
    "rabbit": "Rabbit.egg",
    "wolf": "Wolf.egg"
}

switch_plant = {
    "fir": "Fir.egg",
    "grass": "Grass.egg",
    "oak": "Oak.egg",
    "berry_bush": "Berry_bush.egg"
}

class Model:
    exa_obj=  {
        "grass": None, 
        "ice": None, 
        "yellow": None, 
        "desert" : None,
        "rock": None, 
        "water": None
        }
    animal_obj= {
        "bear": None, 
        "cow": None, 
        "panther": None, 
        "rabbit": None,
        "wolf": None
        }
    plant_obj= {
        "fir": None, 
        "grass": None, 
        "oak": None, 
        "berry_bush": None
        }
    char=None
    render=None

    def initialize(self, instance):
        for k in self.exa_obj:
            self.exa_obj[k]= instance.loader.loadModel("GRAPHIC/Models/" + switch_exa[k])
        for k in self.animal_obj:
            self.animal_obj[k]= instance.loader.loadModel("GRAPHIC/Models/" + switch_animal[k])
        for k in self.plant_obj:
            self.plant_obj[k]= instance.loader.loadModel("GRAPHIC/Models/" + switch_plant[k])
        self.char = instance.loader.loadModel("GRAPHIC/Models/Char.egg")
        self.render=instance.render
            
    def loadExaTile(self, parent, x, y, z, type):
        exa = copy.copy(self.exa_obj[type])
        exa.reparentTo(parent)
        exa.setPos(x, y, z)
        return exa

    def loadCharacter(self, x, y, z):
        self.char.reparentTo(self.render)
        self.char.setPos(x, y, z)
        return self.char

    def loadAnimal(self, parent, x, y, z, type):
        animal = copy.copy(self.animal_obj[type])
        animal.reparentTo(parent)
        animal.setPos(x, y, z)
        animal.setH(random.randint(0, 360))
        return animal

    def loadPlant(self, parent, x, y, z, type):
        plant = copy.copy(self.plant_obj[type])
        plant.reparentTo(parent)
        plant.setPos(x, y, z)
        plant.setH(random.randint(0, 360))
        return plant