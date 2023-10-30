##importacion de libreria
import rivescript as rv
##creacion de objeto tipo rv - metodos de la clase rv
bot = rv.RiveScript()
#


##carga el archivo con los datos del bot
bot.load_file('respuesta.rive')
##ordena el archivo
bot.sort_replies()
#recorre el archivo
while True:
    ##variable que captura los datos del usuario
    mensaje = input('Usuario: ')
    if mensaje == 'salir':
        break
    #respuesta del usuario
    respuesta = bot.reply('usuario',mensaje)
    #respuesta del bot
    print('Botcapuchino:\n'+str(respuesta))
    
    
    
    
