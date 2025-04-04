from geopy.geocoders import Nominatim
from geopy.distance import geodesic
geolocator=Nominatim(user_agent="estenomcchecdcbdhfwjdwhgywtwwtde6353637r858yuo70uoyolmkswu1234567890-")


def calcula_distancia(origem:tuple, destino:tuple):
    distancia = geodesic(origem, destino).kilometers
    return(distancia)
 
def detalhes_lugar(lugar):
    location = geolocator.geocode(lugar)
    if location:
        return location.raw.get("address", {})
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

if __name__=="__main__":
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



