from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposDistDFe_v100 import *



class distDFeInt(ComplexType):
    """Schema de pedido de distribuição de DF-e de interesse"""
    _choice = [['CNPJ', 'CPF'], ['distNSU', 'consNSU']]
    tpAmb: TAmb = Element(TAmb, documentation=['\n            Identificação do Ambiente:\n            1 - Produção\n            2 - Homologação\n            '])
    cUFAutor: TCodUfIBGE = Element(TCodUfIBGE, documentation=['Código da UF do Autor'])
    CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do interessado no DF-e'])
    CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['CPF do interessado no DF-e'])

    class distNSU(ComplexType):
        """Grupo para distribuir DF-e de interesse"""
        ultNSU: TNSU = Element(TNSU, documentation=['Último NSU recebido pelo ator. Caso seja informado com zero, ou com um NSU muito antigo, a consulta retornará unicamente as informações resumidas e documentos fiscais eletrônicos que tenham sido recepcionados pelo Ambiente Nacional nos últimos 3 meses.'])
    distNSU: distNSU = Element(distNSU, documentation=['Grupo para distribuir DF-e de interesse'])

    class consNSU(ComplexType):
        """Grupo para consultar um DF-e a partir de um NSU específico"""
        NSU: TNSU = Element(TNSU, documentation=['Número Sequencial Único. Geralmente esta consulta será utilizada quando identificado pelo interessado um NSU faltante. O Web Service retornará o documento ou informará que o NSU não existe no Ambiente Nacional. Assim, esta consulta fechará a lacuna do NSU identificado como faltante.'])
    consNSU: consNSU = Element(consNSU, documentation=['Grupo para consultar um DF-e a partir de um NSU específico'])
    versao: str = Attribute(TVerDistDFe)

distDFeInt: distDFeInt = Element(distDFeInt, documentation=['Schema de pedido de distribuição de DF-e de interesse'])
