import flet as ft

def main(pagina):
    texto = ft.Text("Rafazap", size=24, color=ft.colors.BLUE_500)

    chat = ft.Column(spacing=10)

    nome_usuario = ft.TextField(label="Escreva seu nome", width=300)

    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            # adicionar a mensagem no chat
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
        else:
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat", 
                                         size=12, italic=True, color=ft.colors.ORANGE_500))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        if campo_mensagem.value.strip():  # Checa se a mensagem não está vazia
            pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value,
                                    "tipo": "mensagem"})
            # limpar o campo de mensagem
            campo_mensagem.value = ""
            pagina.update()
        else:
            pagina.dialog = ft.AlertDialog(title=ft.Text("Erro"), content=ft.Text("A mensagem não pode ser vazia."))
            pagina.dialog.open = True
            pagina.update()

    campo_mensagem = ft.TextField(label="Digite uma mensagem", on_submit=enviar_mensagem, width=400)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_popup(evento):
        if nome_usuario.value.strip():  # Checa se o nome do usuário não está vazio
            pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
            # adicionar o chat
            pagina.add(chat)
            # fechar o popup
            popup.open = False
            # remover o botao iniciar chat e o texto
            try:
                pagina.remove(botao_iniciar)
            except ValueError:
                pass
            try:
                pagina.remove(texto)
            except ValueError:
                pass
            # criar o campo de mensagem do usuario
            # criar o botao de enviar mensagem do usuario
            pagina.add(ft.Row(
                [campo_mensagem, botao_enviar_mensagem],
                alignment=ft.MainAxisAlignment.CENTER
            ))
            pagina.update()
        else:
            pagina.dialog = ft.AlertDialog(title=ft.Text("Erro"), content=ft.Text("O nome de usuário não pode ser vazio."))
            pagina.dialog.open = True
            pagina.update()

    popup = ft.AlertDialog(
        open=False, 
        modal=True,
        title=ft.Text("Bem vindo ao chat do Rafael"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)],
    )

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_chat)

    pagina.add(ft.Column([texto, botao_iniciar], alignment=ft.MainAxisAlignment.CENTER, spacing=20))

ft.app(target=main, view=ft.WEB_BROWSER, port=8000)

