from zooAnimales.animal import Animal

class Reptil (Animal):
    
    _listado=[]
    iguanas=0
    serpientes=0

    def __init__(self,nom=None, ed=0, hab=None, gen=False, esc=None, larg=0):
        super().__init__(nom, ed, hab, gen)
        self._colorEscamas=esc
        self._largoCola=larg
        Reptil.setListado(self)
    
    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)
	
    @classmethod
    def crearIguana (cls,nom,ed,gen):
        Reptil.iguanas+=1
        return Reptil(nom,ed,"humedal",gen,"verde",3)

    @classmethod
    def crearSerpiente (cls,nom,ed,gen):
        Reptil.serpientes+=1
        return Reptil(nom,ed,"jungla",gen,"blanco",1)
    
    @classmethod
    def getListado(cls):
        return cls._listado
	
    @classmethod
    def setListado(cls,rep):
        cls._listado.append(rep)
        pass
    
    def movimiento():
        return "reptar"
    
    def getLargoCola(self):
        return self._largoCola
	
    def setLargoCola(self,larg):
        self._largoCola=larg
        pass
    
    def getColorEscamas(self):
        return self._colorEscamas
	
    def setColorEscamas(self,col):
        self._colorEscamas=col
        pass