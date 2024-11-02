# SEPARADOR DE XML - VERSION 3.2 - 2024/03/05

from pathlib import Path
import xml.etree.ElementTree as ET
import shutil
import zipfile
from datetime import datetime

def separar_xml():
    data = datetime.now()
    dia = data.strftime('%d')
    print(f'Organizando XMLs do dia: {dia}')
    pasta_ancora = Path(__file__).parent
    pasta_xml = pasta_ancora / dia
    pasta_xml.mkdir(exist_ok=True)
    pasta_indevida = pasta_xml / 'indevidas'
    pasta_indevida.mkdir(exist_ok=True)
    pasta_consolidados = pasta_ancora / "CONSOLIDADOS"
    pasta_consolidados.mkdir(exist_ok=True)

    arquivos_zip = list(pasta_xml.glob('*.zip'))
    if arquivos_zip:
        caminho_zip = arquivos_zip[0]
        with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
            zip_ref.extractall(pasta_xml)
            print(f'Arquivo {caminho_zip.name} extraído.')
    else:
        print("Nenhum arquivo .ZIP encontrado.")

    namespace = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}

    natops_permitidas = [
        # INSERIR DENTRO DESSA LISTA AS NATUREZAS DE OPERAÇÃO QUE DEVERÃO SER CONSIDERADAS.
        # EXEMPLO:
        # 'VENDA_CONTRIBUINTE', 'VENDA_MERCADORIA'
    ]

    for arquivo in pasta_xml.glob('*.xml'):
        arvore = ET.parse(arquivo)
        raiz = arvore.getroot()
        natOp = raiz.find('.//nfe:natOp', namespace).text if raiz.find('.//nfe:natOp', namespace) is not None else ''
        
        # Aqui ele colocará os XMLs que NÃO devem ser considerados na pasta "indevidas"
        if natOp not in natops_permitidas:
            destino_indevido = pasta_indevida / arquivo.name
            shutil.move(str(arquivo), str(destino_indevido))
            print(f'Arquivo {arquivo.name} movido para a pasta de indevidas.')
        else:
            # Aqui ele copia para a pasta CONSOLIDADOS as notas triadas. 
            destino_consolidado = pasta_consolidados / arquivo.name
            shutil.copy(str(arquivo), str(destino_consolidado))
            print(f'Arquivo {arquivo.name} copiado para a pasta CONSOLIDADOS.')

if __name__ == "__main__":
    separar_xml()