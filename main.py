import re
import unicodedata
import os
import shutil
from tkinter.filedialog import askdirectory
from tkinter import messagebox

def remover_acentos(texto):
    nfkd = unicodedata.normalize('NFKD', texto)
    texto_sem_acentos = ''.join([c for c in nfkd if not unicodedata.combining(c)])
    return texto_sem_acentos

def remover_caracteres_especiais(texto):
    texto = texto.lower()
    texto = remover_acentos(texto)
    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto)
    return texto_limpo

def principal():
    messagebox.showinfo('Começando o programa', 'Selecione uma pasta de arquivo para renomear os documentos e tirar todos os caracteres especiais')

    pasta_origem = askdirectory(title="Pasta com arquivos para renomear")
    if pasta_origem == '':
        messagebox.showerror('Erro', 'Você não selecionou uma pasta')
        exit()

    lista_origem = os.listdir(pasta_origem)
    if len(lista_origem) == 0:
        messagebox.showerror('Erro', 'Você selecionou uma pasta com nenhum arquivo')

    for item in os.listdir(pasta_origem):
        item_path = os.path.join(pasta_origem, item)
        if os.path.isdir(item_path):
            messagebox.showerror('Erro', f'A pasta selecionada contém outra pasta: {item}')
            break
    messagebox.showinfo('Sucesso', 'A pasta está correta e contém apenas arquivos. Agora selecione a pasta destino, lembre-se, que a pasta destino deve estar vazia, ou com arquivos com nomes diferente, senão haverá a substituição')

    while True:
        pasta_destino = askdirectory(title="Pasta de destino para arquivos renomeados")
        if pasta_destino == '':
            messagebox.showerror('Erro', 'Você não selecionou uma pasta de destino')
            exit()
        if pasta_origem == pasta_destino:
            messagebox.showerror("Erro",'A pasta de destino não pode ser a pasta de origem, favor crie uma pasta nova e use ela')
        if pasta_destino != pasta_origem:
            break

    # Renomear e copiar os arquivos
    for item in os.listdir(pasta_origem):
        origem_caminho = os.path.join(pasta_origem, item)
        nome_base, extensao = os.path.splitext(item)
        novo_nome = remover_caracteres_especiais(nome_base) + extensao
        novo_path = os.path.join(pasta_destino, novo_nome) 
        # Copiar o arquivo
        shutil.copy2(origem_caminho, novo_path)

    messagebox.showinfo('Concluído', 'Arquivos foram copiados e renomeados com sucesso.')
 


principal()
