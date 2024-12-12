from zooAnimales import Animal
from multimethod import multimethod
class Pez (Animal):
    
    _listado=[]
    salmones=0
    bacalaos=0
    
    @multimethod
    def __init__(self):
      super().__init__(None, 0, None, None) 
      
    @multimethod
    def __init__(self,nom:str, ed:int, hab:str, gen:bool, cesc:str, ale:int):
        super().__init__(nom, ed, hab, gen)
        self._colorEscamas=cesc
        self._cantidadAletas=ale
        self.setListado(self)
    
    @classmethod
    def cantidadPeces(cls):
        return cls._listado.len()
	
    @classmethod
    def crearSalmon (cls,nom,ed,gen):
        cls.salmones+=1
        salmon=Pez
        return salmon.__init__(nom,ed,"oceano",gen,"rojo",6)

    @classmethod
    def crearBacalao (cls,nom,ed,gen):
        cls.bacalaos+=1
        bacalao=Pez
        return bacalao.__init__(nom,ed,"oceano",gen,"gris",6)
    
    @classmethod
    def getListado(cls):
        return cls._listado
	
    @classmethod
    def setListado(cls,mam):
        cls._listado.append(mam)
        pass
    
    def getColorEscamas(self):
        return self._colorEscamas
	
    def setColorEscamas(self,col):
        self._colorEscamas=col
        pass
    
    def isCantidadAletas(self):
        return self._cantidadAletas
	
    def setCantidadAletas(self,ale):
        self._cantidadAletas=ale
        pass