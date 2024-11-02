import os
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

def processar_var():
    data = datetime.now()
    dia = data.strftime('%d')
    print(f'Rodando VAR para o dia: {dia}')
    pasta_ancora = Path(__file__).parent
    pasta_xml = pasta_ancora / dia

    namespace = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}

    naturezas_operacao_permitidas = [
        # INSERIR DENTRO DESSA LISTA AS NATUREZAS DE OPERAÇÃO QUE DEVERÃO SER CONSIDERADAS.
        # EXEMPLO:
        # 'VENDA_CONTRIBUINTE', 'VENDA_MERCADORIA'
    ]

    produtos_pesquisados = {
        # INSERIR NESSE DICIONÁRIO O PAR DE DADOS: 'NOME DO PRODUTO' , FLOAT 0.0.
        # EXEMPLO:
        # 'Tenis Mizuno modelo X' : '0.0',
        # 'Tenis Asics modelo Y' : '0.0',
    }

    for arquivo in os.listdir(pasta_xml):
        if arquivo.endswith('.xml'):
            caminho_completo = os.path.join(pasta_xml, arquivo)
            
            tree = ET.parse(caminho_completo)
            root = tree.getroot()
            
            natOp = root.find('.//nfe:natOp', namespace).text if root.find('.//nfe:natOp', namespace) is not None else ''
            serie = root.find('.//nfe:serie', namespace).text if root.find('.//nfe:serie', namespace) is not None else ''
            
            if natOp in naturezas_operacao_permitidas and serie != '70':
                for det in root.findall('.//nfe:det', namespace):
                    xProd = det.find('.//nfe:xProd', namespace).text if det.find('.//nfe:xProd', namespace) is not None else ''
                    qCom = float(det.find('.//nfe:qCom', namespace).text) if det.find('.//nfe:qCom', namespace) is not None else 0.0
                    
                    for produto in produtos_pesquisados:
                        if produto in xProd.upper():
                            produtos_pesquisados[produto] += qCom

    for produto, quantidade in produtos_pesquisados.items():
        print(f'Total de qCom para {produto}: {quantidade}')

if __name__ == "__main__":
    processar_var()