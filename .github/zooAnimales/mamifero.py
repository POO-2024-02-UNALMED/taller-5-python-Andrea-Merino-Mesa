from zooAnimales import Animal
from multimethod import multimethod
class Mamifero (Animal):
    
    _listado=[]
    caballos=0
    leones=0
    
    @multimethod
    def __init__(self):
      super().__init__(None, 0, None, None) 
      
    @multimethod
    def __init__(self,nom:str, ed:int, hab:str, gen:bool, pel:str, pata:int):
        super().__init__(nom, ed, hab, gen)
        self._patas=pata
        self._pelaje=pel
        self.setListado(self)
    
    @classmethod
    def cantidadMamiferos(cls):
        return cls._listado.len()
	
    @classmethod
    def crearCaballo (cls,nom,ed,gen):
        cls.caballos+=1
        caballo=Mamifero
        return caballo.__init__(nom,ed,"pradera",gen,True,4)

    @classmethod
    def crearLeon (cls,nom,ed,gen):
        cls.leones+=1
        leon=Mamifero
        return leon.__init__(nom,ed,"selva",gen,True,4)
    
    @classmethod
    def getListado(cls):
        return cls._listado
	
    @classmethod
    def setListado(cls,mam):
        cls._listado.append(mam)
        pass
    
    def getPatas(self):
        return self._patas
	
    def setPatas(self,pat):
        self._patas=pat
        pass
    
    def getPelaje(self):
        return self._pelaje
	
    def setPelaje(self,pel):
        self._pelaje=pel
        pass