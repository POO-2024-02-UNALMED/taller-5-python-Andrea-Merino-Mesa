from zooAnimales.animal import Animal
class Pez (Animal):
    
    _listado=[]
    salmones=0
    bacalaos=0

    def __init__(self,nom=None, ed=0, hab=None, gen=False, cesc=None, ale=0):
        super().__init__(nom, ed, hab, gen)
        self._colorEscamas=cesc
        self._cantidadAletas=ale
        self.setListado(self)
    
    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)
	
    @classmethod
    def crearSalmon (cls,nom,ed,gen):
        cls.salmones+=1
        return Pez(nom,ed,"oceano",gen,"rojo",6)

    @classmethod
    def crearBacalao (cls,nom,ed,gen):
        cls.bacalaos+=1
        return Pez(nom,ed,"oceano",gen,"gris",6)
    
    @classmethod
    def getListado(cls):
        return cls._listado
	
    @classmethod
    def setListado(cls,mam):
        cls._listado.append(mam)
        pass
    
    def movimiento():
        return "nadar"
        
    def getColorEscamas(self):
        return self._colorEscamas
	
    def setColorEscamas(self,col):
        self._colorEscamas=col
        pass
    
    def getCantidadAletas(self):
        return self._cantidadAletas
	
    def setCantidadAletas(self,ale):
        self._cantidadAletas=ale
        pass