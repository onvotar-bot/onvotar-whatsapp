from yowsup.layers.interface import YowInterfaceLayer
from yowsup.layers.interface import ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities.message_text import TextMessageProtocolEntity
from onvotar import calculate


class EchoLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):

        if messageProtocolEntity.getType() == 'text':
            self.onTextMessage(messageProtocolEntity)
            print('text')
            text = messageProtocolEntity.getBody()
            if len(text) != 24:
                response = (
                    'Hola! Per saber el teu local, '
                    'fes servir aquest format: \n'
                    'DNI DATA_NAIXEMENT CODI_POSTAL\n\n'
                    'Exemple:\n00000000Z AAAAMMDD 01234'
                )
            else:
                text_split = text.split(' ')
                result = calculate(*text_split)
                if result:
                    response = (
                        '{}\n{}\n{}\n\n'
                        'Districte: {}\n'
                        'Secció: {}\n'
                        'Mesa: {}'
                    ).format(*result)
                else:
                    response = (
                        'Alguna de les dades entrades no és correcta.\n'
                        'Revisa-les, si us plau.'
                    )

            self.toLower(TextMessageProtocolEntity(
                response,
                to=messageProtocolEntity.getFrom()
            ))
        else:
            print('no_text')

        self.toLower(messageProtocolEntity.ack())
        self.toLower(messageProtocolEntity.ack(True))

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        self.toLower(entity.ack())

    def onTextMessage(self, messageProtocolEntity):
        # just print info
        print("Message recieved from {}".format(
            messageProtocolEntity.getFrom(False))
        )
