[app]
# (String) Nome do aplicativo
title = Campo Minado
# (String) Nome do pacote
package.name = campo_minado
# (String) Domínio do pacote
package.domain = com.super_nani
# (String) Versão do aplicativo
version = 1.0
# (String) Número da versão
version.code = 1
# (List) Dependências do aplicativo
requirements = kivy, random, unidecode

# (List) Permissões do Android
android.permissions = INTERNET, ACCESS_NETWORK_STATE

[buildozer]
# Se você está criando para Android, defina isso
android = True
# Caminho para o Android SDK (deixe como está se o SDK estiver corretamente instalado)
# android.sdk_path = /path/to/android/sdk
# Caminho para o Android NDK (deixe como está se o NDK estiver corretamente instalado)
# android.ndk_path = /path/to/android/ndk
# Versão mínima do Android
android.minapi = 21
# Defina o target do Android
android.target = android-30
# Habilite a depuração
# android.debug = True
# android.release = False
# (Boolean) Se você deseja usar uma tela de inicialização personalizada, habilite isso.
# screen.orientation = portrait

[android]
# (String) Caminho para o arquivo de ícones (se tiver)
# icon.filename = %(source.dir)s/icon.png
# Caminho para o arquivo da tela de inicialização (se tiver)
# screen.orientation = portrait

# Defina as permissões necessárias
android.permissions = INTERNET, ACCESS_FINE_LOCATION

[android]
# Caminho para o arquivo da chave (keystore)
android.keystore = campo_minado.keystore
# Alias da chave
android.keyalias = campo_minado
# Senha do keystore
android.keystorepassword = ${KESTORE_PASSWORD}
android.keypassword = ${KEY_PASSWORD}