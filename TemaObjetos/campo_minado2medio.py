class Campo_minado_medio:
       def configuracoes(self):
        while True:
            dificuldade = input("""seja bem vindo(a) ao campo minado! Agora me diga, qual o nivel de dificuldade que voce gostaria de jogar?
                fácil
                        
                médio
                        
                dificil
                        
                complicado
                        
                entediado

                horas livres
                            
                            """).lower()

            if dificuldade == "facil":
                dicionario = {"linhas": 4, "colunas": 4, "minas": 2}
                return dicionario

            if dificuldade == "fácil":
                dicionario = {"linhas": 4, "colunas": 4, "minas": 2}
                return dicionario

            if dificuldade == "médio":
                dicionario = {"linhas": 6, "colunas": 6, "minas": 4}
                return dicionario

            if dificuldade == "medio":
                dicionario = {"linhas": 6, "colunas": 6, "minas": 4}
                return dicionario

            if dificuldade == "difícil":
                dicionario = {"linhas": 9, "colunas": 9, "minas": 8}
                return dicionario

            if dificuldade == "dificil":
                dicionario = {"linhas": 9, "colunas": 9, "minas": 8}
                return dicionario

            if dificuldade == "complicado":
                dicionario = {"linhas": 13, "colunas": 13, "minas": 15}
                return dicionario

            if dificuldade == "entediado":
                dicionario = {"linhas": 16, "colunas": 16, "minas": 25}
                return dicionario
            if dificuldade == "horas livres":
                dicionario = {"linhas": 20, "colunas": 20, "minas": 40}
                return dicionario

