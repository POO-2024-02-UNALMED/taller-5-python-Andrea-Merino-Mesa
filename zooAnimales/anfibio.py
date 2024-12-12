from zooAnimales.animal import Animal
class Anfibio (Animal):
    
    _listado=[]
    ranas=0
    salamandras=0

    def __init__(self,nom=None, ed=0, hab=None, gen=False, col=None, veneno=False):
        super().__init__(nom, ed, hab, gen)
        self._colorPiel=col
        self._venenoso=veneno
        Anfibio.setListado(self)
    
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    
    @classmethod
    def crearRana (cls,nom,ed,gen):
        Anfibio.ranas+=1
        return Anfibio(nom,ed,"selva",gen,"rojo",True)
    
    @classmethod
    def crearSalamandra (cls,nom,ed,gen):
        Anfibio.salamandras+=1
        return Anfibio(nom,ed,"selva",gen,"negro y amarillo",False)
    
    @classmethod
    def getListado(cls):
        return cls._listado
	
    @classmethod
    def setListado(cls,anf):
        cls._listado.append(anf)
        pass
    
    def movimiento():
        return "saltar"
    
    def getColorPiel(self):
        return self._colorPiel
	
    def setColorPiel(self,col):
        self._colorPiel=col
        pass
    
    def getVenenoso(self):
        return self._pelaje
	
    def setVenenoso(self,ven):
        self._venenoso=ven
        pass