from gestion import Zoologico
from multimethod import multimethod

class Zona:
    
    @multimethod
    def __init__(self):
      self.__init__(None, None) 
      
    @multimethod
    def __init__(self,nom:str,zoo:Zoologico):
        self._nombre=nom
        self._zoo=zoo 
        self._animales=[]
        self._animales.append(self)
    
    def agregarAnimales(self,animal):
        self._animales.append(animal)
        pass
    
    def cantidadAnimales(self):
        return self._animales.len()
	
    def setZoo(self,zoo):
        self._zoo=zoo
        pass
    
    def getZoo(self):
        return self._zoo
    
    def setNombre(self,nom):
        self._nombre=nom
        pass
    
    def getNombre(self):
        return self._nombre

    def getAnimales(self):
        return self._animales
