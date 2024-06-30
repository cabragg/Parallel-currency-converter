import requests #con esto importas la libreria requests, 
#basicamente lo que hace esta libreria es permitir que se manden requests (solicitudes) desde python para interactuar con una API y agarrar algun dato especifico que estes buscando, 
#en este caso son los tipos de cambio actualizados

def get_tiposdecambio(api_key):
    url = "https://v6.exchangerate-api.com/v6/" + api_key + "/latest/ARS" #link del sitio que vamos a usar para extraer los datos del tipo de cambio
    response= requests.get(url)
    data= response.json() 
    cambio_oficial= data['conversion_rates']['USD'] #dolar oficial
    blue= cambio_oficial* 1.2 #asumamos que el blue vale 20% mas
    return cambio_oficial,blue

api_key= "95203ef207a68485ebd8fdf7" #esta es la llave de la API con la que vamos a acceder a la informacion que nos interesa de la web

pesos = float(input ("Ingresar monto en pesos argentinos:"))  

cambio_oficial,blue= get_tiposdecambio(api_key) #con esta linea "agarramos" los valores en tiempo real de los tipos de cambio respectivos con la llave de la API

exchange = pesos / cambio_oficial 
parallel_ex = pesos / blue

print ("\nEquivalente a {:.2f} (Dólar oficial)".format(exchange)) #lo de {:.2f} es para que la variable que se imprima solo tenga dos decimales y no tenga muchisimos que es medio nocivo para la vista del usuario. 
print ("\nEquivalente a {:.2f} (Dólar blue)".format(parallel_ex)) #aca lo mismo, y se usa el .format que es un metodo para darle formato a strings en Python

print("\nEl cambio oficial es el valor del dólar según el gobierno") #imprimir en pantalla explicacion basica del termino dolar oficial
print("\nEl dolar blue se refiere al valor del dólar en el mercado paralelo") #imprimir en pantalla explicacion basica del termino dolar blue

print("\nMuchas gracias por usar nuestro conversor de monedas. Vuelva pronto!") #imprimir en pantalla un mensaje agradeciendo al usuario
