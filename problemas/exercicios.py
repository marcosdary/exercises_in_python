import pint
import math
ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

'''
                        Problemas
'''
'''
A milha ainda é uma unidade de comprimento muito 
usada nos Estados Unidos e na Europa. Sabendo que 1 mi é 
aproximadamente igual a 1,61 km, calcule: 

(a) o número de metros quadrados existentes em uma milha quadrada; 

(b) o número de decímetros cúbicos existentes em uma milha cúbica.
'''

DADOS_1_50 = 1.61 * ureg.km 

r_1_50_a = pow(DADOS_1_50, 2) # 2.5921 km²

r_1_50_b = Q_(pow(DADOS_1_50, 3), ureg.dm**3) # 4.186×10¹² dm³ 

'''
À medida que você come um pacote de biscoitos de 
chocolate, observa que cada biscoito é um disco circular com um 
diâmetro de 8,50 +- 0,02 cm e espessura de 0,050 +- 0,005 cm. 

(a) Ache o volume médio de um biscoito e a incerteza no volume. 

(b) Ache a razão entre o diâmetro e a espessura e a incerteza nessa razão
'''
DIAMETRO = 8.50
INCERTEZA_DIAMETRO = 0.02

ESPESSURA = 0.05 
INCERTEZA_ESPESSURA = 0.005 

# Calculando o raio e sua incerteza
raio = (DIAMETRO/2) 
incerteza_raio = (INCERTEZA_DIAMETRO /2) 
volume = (math.pi * pow(raio, 2) * ESPESSURA) * ureg.cm ** 3
volume_incerteza = volume * math.sqrt((incerteza_raio / raio)**2 + (INCERTEZA_ESPESSURA / ESPESSURA)**2) # 2.8358 ± 0.2839 cm³

# Calculando o volume e sua incerteza
razao = DIAMETRO / ESPESSURA

'''
Tecidos biológicos são tipicamente compostos de 
98% de água. Considerando-se a densidade da água como 1,0 
x 10³ kg/m3, estime a massa 

(a) do coração de um humano adulto; 

(b) de uma célula com diâmetro de 0,5 mm; 

(c) de uma abelha
'''

TECIDO_BIO = 0.98
DENSIDADE_AGUA = 1000 * ureg.kg / ureg.m ** 3

volume_coracao = 4/3 * math.pi * (4.5/100)**2 * (6/100)
r_1_56_a = DENSIDADE_AGUA * volume_coracao * ureg.kg # Massa do coração adulto é 0.508 kg

volume_celula = 4/3 * math.pi * (0.25/1000)**3
r_1_56_b = DENSIDADE_AGUA * volume_celula * ureg.kg # Massa do célula é 6.54*10^-8 kg

volume_abelha = math.pi * (0.25/100)**2 * (1.5/100)
r_1_56_c = DENSIDADE_AGUA * volume_abelha * ureg.kg # Massa do abelha é 0.000295 kg

