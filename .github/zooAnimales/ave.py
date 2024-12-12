from zooAnimales import Animal
from multimethod import multimethod
class Ave (Animal):
    
    _listado=[]
    aguilas=0
    halcones=0
    
    @multimethod
    def __init__(self):
      super().__init__(None, 0, None, None) 
      
    @multimethod
    def __init__(self,nom:str, ed:int, hab:str, gen:bool, col:str):
        super().__init__(nom, ed, hab, gen)
        self._colorPlumas=col
        self.setListado(self)
    
    @classmethod
    def cantidadAves(cls):
        return cls._listado.len()
	
    @classmethod
    def crearHalcon (cls,nom,ed,gen):
        cls.halcones+=1
        halcon=Ave
        return halcon.__init__(nom,ed,"montanas",gen,"cafe glorioso")

    @classmethod
    def crearAguila (cls,nom,ed,gen):
        cls.aguilas+=1
        aguila=Ave
        return aguila.__init__(nom,ed,"montanas",gen,"blanco y amarillo")
    
    @classmethod
    def getListado(cls):
        return cls._listado
	
    @classmethod
    def setListado(cls,mam):
        cls._listado.append(mam)
        pass
    
    def getColorPlumas(self):
        return self._colorPlumas
	
    def setColorPlumas(self,col):
        self._colorPlumas=col
        pass