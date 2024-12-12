from zooAnimales.animal import Animal
class Ave (Animal):
    
    _listado=[]
    aguilas=0
    halcones=0

    def __init__(self,nom=None, ed=0, hab=None, gen=False, col=None):
        super().__init__(nom, ed, hab, gen)
        self._colorPlumas=col
        self.setListado(self)
    
    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
	
    @classmethod
    def crearHalcon (cls,nom,ed,gen):
        cls.halcones+=1
        return Ave(nom,ed,"montanas",gen,"cafe glorioso")

    @classmethod
    def crearAguila (cls,nom,ed,gen):
        cls.aguilas+=1
        return Ave(nom,ed,"montanas",gen,"blanco y amarillo")
    
    @classmethod
    def getListado(cls):
        return cls._listado
	
    @classmethod
    def setListado(cls,mam):
        cls._listado.append(mam)
        pass
    
    def movimiento():
        return "volar"
    
    def getColorPlumas(self):
        return self._colorPlumas
	
    def setColorPlumas(self,col):
        self._colorPlumas=col
        pass