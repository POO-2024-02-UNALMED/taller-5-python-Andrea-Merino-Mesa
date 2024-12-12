from zooAnimales import Animal
from multimethod import multimethod
class Anfibio (Animal):
    
    _listado=[]
    ranas=0
    salamandras=0
    
    @multimethod
    def __init__(self):
      super().__init__(None, 0, None, None) 
      
    @multimethod
    def __init__(self,nom:str, ed:int, hab:str, gen:bool, col:str, veneno:bool):
        super().__init__(nom, ed, hab, gen)
        self._colorPiel=col
        self._venenoso=veneno
        self.setListado(self)
    
    @classmethod
    def cantidadAnfibios(cls):
        return cls._listado.len()
	
    @classmethod
    def crearRana (cls,nom,ed,gen):
        cls.ranas+=1
        rana=Anfibio
        return rana.__init__(nom,ed,"selva",gen,"rojo",True)

    @classmethod
    def crearSalamandra (cls,nom,ed,gen):
        cls.salamandras+=1
        salamandra=Anfibio
        return salamandra.__init__(nom,ed,"selva",gen,"negro y amarillo",False)
    
    @classmethod
    def getListado(cls):
        return cls._listado
	
    @classmethod
    def setListado(cls,anf):
        cls._listado.append(anf)
        pass
    
    def movimiento():
        return "saltar"
    
    def getcolorPiel(self):
        return self._colorPiel
	
    def setcolorPiel(self,col):
        self._colorPiel=col
        pass
    
    def getVenenoso(self):
        return self._pelaje
	
    def setVenenoso(self,ven):
        self._venenoso=ven
        pass