from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v200 import *

from .consReciCTeTiposBasico_v200 import *

from .cancCTeTiposBasico_v200 import *

from .eventoCTeTiposBasico_v200 import *

from .xmldsig_core_schema_v101 import *



class TConsSitCTe(Element):
    """Tipo Pedido de Consulta da Situação Atual do Conhecimento de Transporte eletrônico"""
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    xServ: TServ = Element(TServ, documentation=['Serviço Solicitado'])
    chCTe: TChNFe = Element(TChNFe, documentation=['Chaves de acesso da CT-e, compostas por: UF do emitente, AAMM da emissão da CT-e, CNPJ do emitente, modelo, série e número da CT-e e código numérico + DV.'])
    versao: str = Attribute(None)



class TVerConsSitCTe(str):
    """Tipo Versão do Consulta situação de CT-e - 2.00"""
    _restriction = Restriction(base=r"xs:string", pattern=r"2\.00", enumeration=[])
    pass



class TRetConsSitCTe(Element):
    """Tipo Retorno de Pedido de Consulta da Situação Atual do Conhecimento de Transporte eletrônico"""
    _choice = [['protCTe', 'retCancCTe']]
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que processou o CT-e'])
    cStat: TStat = Element(TStat, documentation=['Código do status da mensagem enviada.'])
    xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do serviço solicitado.'])
    cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['código da UF de atendimento'])
    protCTe: TProtCTe = Element(TProtCTe)
    retCancCTe: TRetCancCTe = Element(TRetCancCTe)
    procEventoCTe: List[TProcEvento] = Element(TProcEvento, max_occurs=-1)
    versao: str = Attribute(TVerConsSitCTe)


