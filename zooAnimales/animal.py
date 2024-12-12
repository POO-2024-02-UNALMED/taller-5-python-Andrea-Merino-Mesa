class Animal (object):
    _totalAnimales=0
    def __init__(self,nom=None, ed=0, hab=None, gen=False):
        self._nombre=nom
        self._edad=ed
        self._habitat=hab
        self._genero=gen
        self._zona=None
        self.setTotalAnimales(1)
        
    def movimiento():
     return "desplazarse"
    
    def totalPorTipo():
        return "Mamiferos: "+str(Mamifero.cantidadMamiferos())+"\n"+"Aves: "+str(Ave.cantidadAves())+"\n"+"Reptiles: "+str(Reptil.cantidadReptiless())+"\n"+"Peces: "+str(Pez.cantidadPeces())+"\n"+"Anfibios: "+str(Anfibio.cantidadAnfibios());	
	
    def __str__(self):
        if self.zona==None or self.zona.getZoo()==None:
            return "Mi nombre es "+self.nombre+", tengo una edad de "+self.edad+", habito en "+self.habitat+" y mi genero es "+self.genero
        return "Mi nombre es "+self.nombre+", tengo una edad de "+self.edad+", habito en "+self.habitat+" y mi genero es "+self.genero+", la zona en la que me ubico es "+self.zona.getNombre()+", en el"+self.zona.getZoo().getNombre()+"."
	
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
	
    @classmethod
    def setTotalAnimales(cls,tAnimales):
        cls._totalAnimales+=tAnimales
        pass
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self,nom):
        self._nombre=nom
        pass
    
    def getEdad(self):
        return self._edad
    
    def setEdad(self,edad):
        self._edad=edad
        pass
 
    def getHabitat(self):
        return self._habitat
    
    def setHabitat(self, hab):
        self._habitat=hab
        pass
    
    def getGenero(self):
        return self._genero
    
    def setGenero(self,gen):
        self._genero=gen
        pass
    
    def getZona(self):
        return self._zona
    
    def setZona(self,zona):
        self._zona=zona
        pass

