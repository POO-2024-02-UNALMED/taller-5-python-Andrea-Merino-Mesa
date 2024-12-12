
class Zoologico:

    def __init__(self,nom=None,ubi=None):
        self._nombre=nom
        self._ubicacion=ubi
        self._zonas=[]
    
    def cantidadTotalAnimales(self):
        ca=0
        for i in range (self._zonas.len()):
            ca+=self.getZona().get(i).cantidadAnimales()
        return ca
    
    def setNombre(self,nom):
        self._nombre=nom
        pass
    
    def getNombre(self):
        return self._nombre
    
    def setUbicacion(self,ubi):
        self._ubicacion=ubi
        pass
    
    def getUbicacion(self):
        return self._ubicacion	
    
    def getZona(self):
        return self._zonas
    
    def agregarZonas(self,zona):
        self._zonas.append(zona)
        pass
    
    def cantidadAnimales(self):
        return self._zonas