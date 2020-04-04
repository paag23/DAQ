##Metodos###

from Ctes import*


class Sensores():

 	def __init__(self,nombre):
 		self.nombre = nombre


 	def filtro(self, lectura, alpha, S):

 		S = ( alpha * lectura ) + ( (1 - alpha ) * S )

 		return S

 	
 	def Caracterizacion_Corriente(self, C3 ):
 		# Sensor ACS712
    	#y = ax + b    b = - 2.5 cero positivo
    	#Sensibilidad Experiemtal 0.179
 		
 		ACI = 0.0
 		ACI = (C3 * 4096)/Ref #Cuentas

 		if ACI>=2047:
 			ACI = ACI * (5 / 4096)
 			ACI = (ACI - 2.5 ) / 0.185
 			ACI = round (ACI, 3)
 			#print ("ACI =, ACI")

 		else: ACI = 0
 		#print("______________________", ACI)

 		return ACI

 	
 	def Caracterizacion_Acelerometro(self,C):

 		AC = ( (0.8 * C) + 1.65 ) * 4096 / Ref
 		AC = AC * 9.81

 		return (AC)




class Archivo():
	
	def ArchivoTexto(self, In0, In1, In2, In3, In4, In5):

		archivo = open('Base_de_Datos.txt','a' )
		archivo.write( In0 )
		archivo.write( ',' )
		archivo.write( In1 )
		archivo.write( ',' )
		archivo.write( In2 )
		archivo.write( ',' )
		archivo.write( In3 )
		archivo.write( ',' )
		archivo.write( In4 )
		archivo.write( ',' )
		archivo.write( In5 )
		archivo.write( '\n' )
		archivo.close()

    #print ( " Archivo de impresión \n", In0, In1, In2, In4 )







    	 		