from zooAnimales.animal import Animal

class Mamifero (Animal):
    
    _listado=[]
    caballos=0
    leones=0

    def __init__(self,nom=None, ed=0, hab=None, gen=False, pel=None, pata=0):
        super().__init__(nom,ed,hab,gen)
        self._patas=pata
        self._pelaje=pel
        Mamifero.setListado(self)
    
    @classmethod
    def cantidadMamiferos(cls):
        return cls._listado.len()
    
    @classmethod
    def crearCaballo (cls,nom,ed,gen):
        Mamifero.caballos+=1
        return Mamifero(nom,ed,"pradera",gen,True,4)
    
    @classmethod
    def crearLeon (cls,nom,ed,gen):
        Mamifero.leones+=1
        return Mamifero(nom,ed,"selva",gen,True,4)
    
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
    
    def isPelaje(self):
        return self._pelaje
	
    def setPelaje(self,pel):
        self._pelaje=pel
        pass