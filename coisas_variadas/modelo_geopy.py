from geopy.geocoders import Nominatim
from geopy.distance import geodesic



def calcula_distancia(origem:tuple, destino:tuple):
    distancia = geodesic(origem, destino).kilometers
    return(distancia)
 
def detalhes_lugar(lugar):
    geolocator=Nominatim(user_agent=lugar)
    location = geolocator.geocode(lugar)
    if location:
        return location.raw
    return None


def endereco_para_coordenadas(endereco:str):
    try:
        location = geolocator.geocode( endereco )
        return(location.latitude, location.longitude)
    except:
        return None
    
def coordenadas_para_endereco():
    location = geolocator.reverse((48.8566, 2.3522))
    print(location.address)
    print(location.raw)

def pergunta_e_verifica_endereco(mensagem_input):
    while True:
        endereco=input(mensagem_input    )
        # origem=input()
        coordenada=endereco_para_coordenadas(endereco)
        if coordenada==None:
              continue
        return coordenada

    




    #perguntar endereço de origem
    # perguntar o destino
    # pegar as coordenadas de cada endereço
    # calcular a distancia entre as coordenadas 

def teste_de_calculo_de_frete():
    while True:
        coordenada_de_origem=pergunta_e_verifica_endereco(mensagem_input="Escreva o endereço de origem:    ")
        coordenada_de_destino=pergunta_e_verifica_endereco(mensagem_input="Agora, diga o seu destino:     ")       
 
        distancia=calcula_distancia(origem=coordenada_de_origem, destino=coordenada_de_destino)
        print(distancia)
        valor_por_km=1.50
        valor_total=distancia* valor_por_km
        print(f"O valor do frete será {round(valor_total,2)}")
        continuar=input("Gostaria de fazer mais alguma pesquisa?    ")
        if continuar=="nao":
            break
        
        print("Um de seus endereços é inválido. Tente novamente.")
        continue    

paises_capitais_america = {
'ggddfgfhfhfhkfkhfekhfhergerffehvfhfhrfejgfgfhfhfherfg': 'Saint John\'s',
'Argentina': 'Buenos Aires',
'Bahamas': 'Nassau',
'Barbados': 'Bridgetown',
'Belize': 'Belmopan',
'Bolívia': 'Sucre',
'Brasil': 'Brasília',
'Chile': 'Santiago',
'Colômbia': 'Bogotá',
'Costa Rica': 'San José',
'Cuba': 'Havana',
'Dominica': 'Roseau',
'Equador': 'Quito',
'El Salvador': 'San Salvador',
'Granada': 'Saint George\'s',
'Gcdcffffff': 'Cidade da Guatemala',
'Guyana': 'Georgetown',
'Haiti': 'Porto Príncipe',
'Honduras': 'Tegucigalpa',
'Jamaica': 'Kingston',
'Mdddfefefr': 'Cidade do México',
'Nicarágua': 'Manágua',
'Panamá': 'Cidade do Panamá',
'Paraguai': 'Assunção',
'Peru': 'Lima',
'República Dominicana': 'Santo Domingo',
'São Cristóvão e Nevis': 'Basseterre',
'São Vicente e Granadinas': 'Kingstown',
'Suriname': 'Paramaribo',
'Trinidad e Tobago': 'Porto de Espanha',
'Uruguai': 'Montevidéu',
'Venezuela': 'Caracas'
}

if __name__=="__main__":
    for pais in paises_capitais_america.keys():
        geolocator=Nominatim(user_agent=pais)
        informacoes_retornadas=detalhes_lugar(lugar=pais)
        # tipo_de_endereco=informacoes_retornadas["addresstype"]
        if informacoes_retornadas==None:
            print(f"O local {pais} é invalido")
            continue
        tipo_de_endereco=informacoes_retornadas.get("addresstype","Addresstype não encontrado")
        print(f"{pais}: {tipo_de_endereco}")