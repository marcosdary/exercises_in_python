import pint
ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

'''
                        Utilização e conversão de unidades
'''

'''
A densidade do ouro é 19,3 g/cm3. Qual é esse valor 
em quilogramas por metro cúbico?
'''
qts_1_2 = 19.3 * ureg.g/ureg.cm**3
r_1_2 = Q_(qts_1_2, ureg.kg/ureg.m**3) # 19300.0 kg / m³

'''
Um campo quadrado que mede 100,0 m por 100,0 m 
possui uma área de 1,0 hectare. Um acre corresponde a uma 
área de 4.046,84 m2. Se um terreno possui uma área de 12,0 
acres, qual é sua área em hectares?
'''

qts_1_6 = 12 * 4_046.84 * ureg.m ** 2 
r_1_6 = Q_(qts_1_6, ureg.ha) # 4.856208 hectare

'''
Ao dirigir em um país exótico, você vê um aviso 
de limite máximo de velocidade de 100 mi/h 
na rodovia. Expresse esse limite em km/h e em m/s.
'''

qts_1_8 = 100 * ureg.mi / ureg.h
r_1_8_1 = Q_(qts_1_8, ureg.km / ureg.h) # 160.9344 km / h
r_1_8_2 = Q_(qts_1_8, ureg.m / ureg.s) # 44.704 m / s


''' As seguintes conversões ocorrem com frequência em 
física e são muito úteis. 

(a) Considere 1 mi 5.280 pés e 1 h 
3.600 s para converter 60 mph em unidades de pés/s. 

(b) A aceleração de um objeto em queda livre 
é de 32 pés/s2. Considere 1 pé = 30,48 cm para 
expressar essa aceleração em unidades de m/s2

(c) A densidade da água é 1,0 g/cm3. Converta 
essa densidade em unidades de kg/m3.'''

qts_1_10_a = 60 * ureg.mi / ureg.h 
r_1_10_a = Q_(qts_1_10_a, ureg.ft / ureg.s) # 88.0 pés / s

qts_1_10_b = 32 * ureg.ft / ureg.s ** 2
r_1_10_b = Q_(qts_1_10_b, ureg.m / ureg.s ** 2) # 9.7536 m / s²

qts_1_10_c = 1 * ureg.g / ureg.cm ** 3
r_1_10_c = Q_(qts_1_10_c, ureg.kg / ureg.m ** 3) # 999.99 kg / m³ ou 1000.0 kg / m³

'''
(a) A dose diária recomendada (DDR) do metal de 
magnésio é 410 mg/dia para homens. Expresse essa quantidade 
em g/dia. 

(b) Para adultos, a DDR do aminoácido lisina é de 12 
mg por kg de massa corporal. Quantos gramas por dia um adulto 
de 75 kg deveria receber? 

(c) Uma cápsula multivitamínica pode 
conter 2,0 mg de vitamina B2(riboflavina) e 
a DDR é de 0,0030 g/dia. Quantas dessas cápsulas 
uma pessoa deverá tomar a cada 
dia para obter a quantidade adequada dessa vitamina, 
se não receber nada de outras fontes? 

(d) A DDR para o microelemento 
selênio é 0,000070 g/dia. Expresse essa dose em mg/dia.'''

qts_1_12_a = 410 * ureg.mg / ureg.day 
r_1_12_a = Q_(qts_1_12_a, ureg.g / ureg.day) # 0.410 g / dia

qts_1_12_b = 12 * ureg.mg / ureg.kg
ddr_g_kg_corporal = Q_(qts_1_12_b, ureg.g / ureg.kg) 
r_1_12_b = 75 * ddr_g_kg_corporal # DDR diária para adulto é 0.9

qts_1_12_c = 0.0030 * ureg.g / ureg.day 
r_1_12_c = Q_(qts_1_12_c, ureg.mg / ureg.day) / 2 # Cápsulas/dia é 1.5

qts_1_12_d = 0.000070 * ureg.g / ureg.day 
r_1_12_d = Q_(qts_1_12_d, ureg.mg / ureg.day) # 0.0699 mg / dia

'''
Usando uma régua de madeira, você mede o comprimento 
de uma placa metálica retangular e encontra 12 mm. 
Usando um micrômetro para medir a largura da placa, 
você encontra 5,98 mm. Forneça as respostas dos seguintes itens com 
o número correto de algarismos significativos. 

(a) Qual a área do retângulo? 

(b) Qual a razão entre a largura do retângulo e seu comprimento? 

(c) Qual o perímetro do retângulo? 

d) Qual a diferença entre o comprimento do retângulo e sua largura?  

(e) Qual a razão entre o comprimento do retângulo e sua largura?
'''

DADOS_1_14 = 12 * ureg.mm , 5.98 * ureg.mm

r_1_14_a = DADOS_1_14[0] * DADOS_1_14[1] # 71.76 mm²

r_1_14_b = DADOS_1_14[1] / DADOS_1_14[0] # razão é igual a 0.498

r_1_14_c = 2*DADOS_1_14[1] + 2*DADOS_1_14[0] # perímetro é 35.96 mm

r_1_14_d = DADOS_1_14[0] - DADOS_1_14[1] # diferença entre largura e comprimento: 6.02 mm

r_1_14_e = DADOS_1_14[0] / DADOS_1_14[1] # razão é igual a 2.00669 

'''
Quantos litros de gasolina são consumidos no Brasil 
em um dia? Suponha que haja um carro para cada quatro 
pessoas, que cada carro seja dirigido por uma média de 10.000 
quilômetros por ano e que um carro percorra em média 
14 quilômetros por litro de gasolina.
'''
# Suposições
POP_TOTAL_BR = 213_300_000
DISTANCIA_MEDIA_CARRO = 10_000 * ureg.km / ureg.year
CONSUMO_MEDIO_GASOLINA = 14 * ureg.km / ureg.l

# Números totais de carros no Brasil
NUM_CARROS_TOTAL =  POP_TOTAL_BR / 4

#  Distância total percorrida por todos os carros em um dia
distancia_total_km_dia = Q_(DISTANCIA_MEDIA_CARRO, ureg.km / ureg.day) * NUM_CARROS_TOTAL


# Litros de gasolina por carro por dia
litro_gasolina_por_carro_dia = Q_(DISTANCIA_MEDIA_CARRO, ureg.km / ureg.day) / CONSUMO_MEDIO_GASOLINA

# Litros de gasolina consumidos no Brasil em um dia
litro_gasolina_consumidos_no_br_dia = NUM_CARROS_TOTAL * litro_gasolina_por_carro_dia # Consumo: 104282780.87415664 l/dia 

'''
Você está usando gotas de água para diluir pequenas 
quantidades de um produto químico no laboratório. 
Quantas gotas de água há em uma garrafa de 1 L? 
(Dica: comece estimando o diâmetro de uma gota de água.)
'''

DADOS_1_23 = 1000 * ureg.cm ** 3
diametro_medio_gota_agua = 0.1 * ureg.cm
volume_gota = 4/3 * 3.14 * pow(diametro_medio_gota_agua, 3)
r_1_23 = DADOS_1_23 / volume_gota # Quantidade de gotas é 238853.503



