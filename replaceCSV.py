def replaceCSV(nome_do_arquivo: str, char_q_vai_sair: str, char_q_vai_entrar: str):
    'Substitui caracteres em um CSV'
    arquivo = open(nome_do_arquivo, 'r')
    textoArquivo = arquivo.read()
    textoTransformado = textoArquivo.replace(char_q_vai_sair, char_q_vai_entrar)
    arquivoTemporario = open(nome_do_arquivo, 'w', encoding='utf-8')
    arquivoTemporario.write(textoTransformado)
    arquivoTemporario.close()