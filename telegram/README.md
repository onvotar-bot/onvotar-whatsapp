# OnVotar-Telegram #

Versió telegram del bot de:
onvotar-bot/onvotar-whatsapp

Per funcionar cal que hi hagi un director /db/ que tingui el mateix
contingut que el db/ de:

https://github.com/referendum1oct/referendum1oct.github.io


## Docker


Per construir un contenidor per docker:

docker build . -t onvotar-telegram

Si s'empra Fedora/CentOS el directori /db ha de ser accessible pel contenidor
docker, en aquest cas:

chcon -Rt svirt_sandbox_file_t <pathtodb>

Per executar (mapejant el directori db)

docker run -d -e BOT_NAME='<botname>' \
           -e API_TOKEN='<apitoken>' \
           -v <pathtodb>:/db \
            onvotar-telegram
