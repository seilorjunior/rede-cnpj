# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 09:17:19 2021
@author: github rictom/rede-cnpj
"""
import configparser, argparse, os, sys
config = configparser.ConfigParser()

confPadrao = 'rede.ini'
if (os.path.exists(confPadrao)):
    config.read(confPadrao, encoding='utf8')
else:
    print('O arquivo de configuracao ' + confPadrao + ' não foi localizado. Parando...')
    sys.exit(1)

#cpfcnpjInicial = config['REDE'].get('cpfcnpj', '')
#camadaInicial = int(config['REDE'].get('camada',1))
#camadaInicial = config['REDE'].getint('camada',1)

def runParser():
    parser = argparse.ArgumentParser(description='descrição', epilog='rictom')
    parser.add_argument('-i', '--inicial', action='store', dest='cpfcnpjInicial', default='', type=str, help='1 ou mais cnpj separados por ponto e vírgula; Nome ou Razao Social Completa')
    parser.add_argument('-c', '--camada', action='store', dest='camadaInicial', type=int, default=1, help='camada')
    parser.add_argument('-k', '--conf_file', action='store', default='rede.ini',help="defina arquivo de configuração", metavar="FILE")
    parser.add_argument('-j', '--json', action='store', dest='idArquivoServidor', default='', type=str, help='nome json no servidor')
    parser.add_argument('-a', '--lista', action='store', dest='arquivoEntrada', default='',help="inserir itens de arquivo em gráfico", metavar="FILE")
    parser.add_argument('-e', '--encoding', action='store', dest='encodingArquivo', default='utf8',help="codificação do arquivo", metavar="FILE")
    #parser.add_argument('-p', '--pasta', action='store', dest='pasta_arquivos', default='arquivos',type=dir_path, help='pasta de arquivos do usuário do projeto')
    parser.add_argument('-p', '--pasta', action='store', dest='pasta_arquivos', default=config['BASE'].get('pasta_arquivos', 'arquivos'), type=str, help='pasta de arquivos do usuário do projeto')
    parser.add_argument('-f', '--porta_flask', action='store', dest='porta_flask', type=int, default=config['BASE'].getint('porta_flask',5000), help='porta da aplicação')

    parser.add_argument('-t', '--texto-embaixo', action='store_true', dest='btextoEmbaixoIcone', default=True,  help='texto em baixo do ícone' )
    parser.add_argument('-T', '--texto-ao-lado', action='store_false', dest='btextoEmbaixoIcone',  help='texto ao lado do ícone' )
    parser.add_argument('-m', '--n-mensagem', action='store_false', dest='bExibeMensagemInicial', default=config['INICIO'].getboolean('exibe_mensagem_advertencia',True),  help='não exibe mensagem inicial' )
    parser.add_argument('-M', '--mensagem',action='store_true', dest='bExibeMensagemInicial', default=config['INICIO'].getboolean('exibe_mensagem_advertencia',True), help='exibe mensagem inicial')
    parser.add_argument('-y', '--n-menuinserir', action='store_false', dest='bMenuInserirInicial', default=config['INICIO'].getboolean('exibe_menu_inserir',True), help='não exibe menu para inserir no inicio' )
    parser.add_argument('-Y', '--menuinserir', action='store_true', dest='bMenuInserirInicial', default=config['INICIO'].getboolean('exibe_menu_inserir',True), help='exibe menu para inserir no inicio' )
    parser.add_argument('-d', '--download', action='store_true', dest='bArquivosDownload', default=config['ETC'].getboolean('arquivos_download',False), help='permitir download da pasta arquivos' )
    parser.add_argument('-D', '--n-download', action='store_false', dest='bArquivosDownload', default=config['ETC'].getboolean('arquivos_download',False), help='permitir download da pasta arquivos' )

    parser.add_argument('-n', '--sheet-name', action='store', dest='excel_sheet_name',default=0, help='nome da aba do excel')
    #parser.add_argument('-r', '--header', action='store', dest='excel_header',default=None, help='aba do excel tem cabecalho ou não')
    parser.add_argument('-s', '--separador', action='store', dest='separador', default='\t', help='separador arquivo csv')

    parser.add_argument('-l', '--tipo_lista', action='store', dest='tipo_lista',default='', help='define tipo de entrada, _+  _* _>')
    return parser.parse_args()

par = runParser()
#if (par.conf_file): #se foi fornecido arquivo de configuracao pela linha de comando, recarrega configparser
if (os.path.exists(par.conf_file)):
    config.read(par.conf_file, encoding='utf8')
    par = runParser()
else:
    print('O arquivo de configuracao ' + par.conf_file + ' não existe. Parando...')
    sys.exit(1)

if par.arquivoEntrada:
    if not os.path.exists(par.arquivoEntrada):
        print('O arquivo ' + par.arquivoEntrada + ' não existe. Parando...')
        sys.exit(1)    

# def dir_path(path):
#     if os.path.isdir(path):
#         return path
#     else:
#         raise argparse.ArgumentTypeError(f"{path} não é um caminho válido")
        
referenciaBD = config['BASE'].get('referencia_bd','')
    
#dic = vars(pr) #converte para dicionario 
# cpfcnpjInicial = par.cpfcnpjInicial
# camadaInicial = par.camadaInicial
# bExibeMensagemInicial = par.bExibeMensagemInicial
# bMenuInserirInicial = par.bMenuInserirInicial
# idArquivoServidorInicial  = par.idArquivoServidor
#print('par)


'''
import pysos #data persistence
nomes_bloqueados = pysos.List('pysos_nomes_bloqueados')
urls_bloqueados = pysos.List('pysos_urls_bloqueados')
'''
