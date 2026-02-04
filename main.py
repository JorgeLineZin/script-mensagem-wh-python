import pywhatkit as kit

msg_num = input(
    "Digite o número de telefone com o código do país e DDD do estado (Ex: +5511999999999): "
)
msg_text = input("Digite a mensagem que deseja enviar: ")

kit.sendwhatmsg_instantly(f"{msg_num}", f"{msg_text}", tab_close=True, close_time=4)
print("Mensagem enviada!")