###############Referencia de Voltaje ADC######################
Voltaje0 = 2.5
Voltaje1 = 3.5
Voltaje2 = 4.5
Ref = 5             
#################Variables Globales###########################

TM = 1000000  #Tiempo de Muestreo en "nanosegundos" 1 miliSegundo = 1 000 000 nanoSegundos; 10000 sp/s

alpha0 = 0.05 #Coeficiente de Frecuencia Fitro de Corte X Paso ALto, Paso BAjo
alpha1 = 0.25 #Fitro de Corte Y
alpha2 = 0.15 #Fitro de Corte Z
alpha3 = 0.55 #Frecuencia Fitro de Corte  I

##################Variables de Filtrado de Ruido EMA #################
S0 = 0.0
S1 = 0.0
S2 = 0.0
S3 = 0.0

################## Rangos de Operacion Normal #################

RI_A = 4.500   #Ranglo ALTO
RI_B = 0.600   #Ranglo BAJO

RX_A =  127.53 #3G Ranglo ALTO
RX_B =  29.43  #13G Ranglo BAJO
RY_A =  127.53 #Rango ALTO
RY_B =  29.43  #Rango BAJO
RZ_A =  29.4   #Rango ALTO
RZ_B =  127.53 #Rango BAJO

RrpM_A = 2800  #Rango ALTO
RrpM_B = 100   #Rango BAJO


SIMU_CH0 = 1
SIMU_CH1 = 15
SIMU_CH2 = 20
SIMU_CH3 = 25
SIMU_CH4 = 30