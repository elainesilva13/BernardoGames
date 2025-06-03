from unidecode import unidecode


palavras_com_acento = "Quero que você faça café!"
palavras_sem_acento = unidecode(palavras_com_acento)

print(palavras_sem_acento)
