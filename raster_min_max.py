carpeta = "C:/Python/Informacion/e14a38"

def raster_min_max(layer):
    '''
    Esta funcion regresa los valores maximo y minimo de una capa raster
    con una sola banda
    '''
    provider = layer.dataProvider()
    stats = provider.bandStatistics(1,QgsRasterBandStats.All)

    v_min = stats.minimumValue
    v_max = stats.maximumValue
    return v_min, v_max
    os.chdir(carpeta) # cambiar el directorio de trabajo
    print() # una linea en blanco

for archivo in os.listdir(carpeta): # recorre los archivos en la carpeta
    if archivo.endswith(".tif"): # filtra los .tif
        nombre = archivo[:-4] # obtiene el nombre quitando la extension
        capa = QgsRasterLayer(archivo, nombre) # crea la capa como un objeto QgsRasterLayer 
        suESPG = capa.crs().authid() # obtiene el ESPG
        suTipo = capa.dataProvider().sourceDataType(1) # obtiene el tipo de raster
        suMin, suMax = raster_min_max(capa) # obtiene el minimo y el maximo
        print(nombre, suESPG,"  Tipo:", suTipo) # imprime la info de la capa
        print("    Min:", round(suMin,1), "  Max:", round(suMax,1))