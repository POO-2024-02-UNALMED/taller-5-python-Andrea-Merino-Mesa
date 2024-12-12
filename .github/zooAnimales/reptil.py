from zooAnimales import Animal
from multimethod import multimethod
class Reptil (Animal):
    
    _listado=[]
    iguanas=0
    serpientes=0
    
    @multimethod
    def __init__(self):
      super().__init__(None, 0, None, None) 
      
    @multimethod
    def __init__(self,nom:str, ed:int, hab:str, gen:bool, esc:str, larg:int):
        super().__init__(nom, ed, hab, gen)
        self._colorEscamas=esc
        self._largoCola=larg
        self.setListado(self)
    
    @classmethod
    def cantidadReptiles(cls):
        return cls._listado.len()
	
    @classmethod
    def crearIguana (cls,nom,ed,gen):
        cls.iguanas+=1
        iguana=Reptil
        return iguana.__init__(nom,ed,"humedal",gen,"verde",3)

    @classmethod
    def crearSerpiente (cls,nom,ed,gen):
        cls.serpientes+=1
        serpiente=Reptil
        return serpiente.__init__(nom,ed,"jungla",gen,"blanco",1)
    
    @classmethod
    def getListado(cls):
        return cls._listado
	
    @classmethod
    def setListado(cls,rep):
        cls._listado.append(rep)
        pass
    
    def movimiento():
        return "reptar"
    
    def getlargoCola(self):
        return self._largoCola
	
    def setlargoCola(self,larg):
        self._largoCola=larg
        pass
    
    def getColorEscamas(self):
        return self._colorEscamas
	
    def setColorEscamas(self,col):
        self._colorEscamas=col
        pass