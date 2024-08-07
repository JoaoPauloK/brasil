# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: cteModalFerroviario_v3.00.xsd
# xmlns: http://www.portalfiscal.inf.br/cte
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposGeralCTe_v300 import *
from .cteTiposBasico_v300 import *


class TEnderFer(ComplexType):
    """Tipo Dados do Endereço"""
    xLgr: Annotated[str, Element] = None
    nro: Annotated[str, Element] = None
    xCpl: Annotated[str, Element] = None
    xBairro: Annotated[str, Element] = None
    cMun: Annotated[TCodMunIBGE, Element] = None
    xMun: Annotated[str, Element] = None
    CEP: Annotated[str, Element] = None
    UF: Annotated[TUf, Element] = None


class ferrov(ComplexType):
    """Informações do modal Ferroviário"""
    tpTraf: Annotated[str, Element] = None

    class _trafMut(ComplexType):
        """Detalhamento de informações para o tráfego mútuo"""
        respFat: Annotated[str, Element] = None
        ferrEmi: Annotated[str, Element] = None
        vFrete: Annotated[TDec_1302, Element] = None
        chCTeFerroOrigem: Annotated[TChNFe, Element] = None

        class _ferroEnv(ComplexType):
            """Informações das Ferrovias Envolvidas"""
            CNPJ: Annotated[TCnpj, Element] = None
            cInt: Annotated[str, Element] = None
            IE: Annotated[TIe, Element] = None
            xNome: Annotated[str, Element] = None
            enderFerro: Annotated[TEnderFer, Element] = None

        ferroEnv: Annotated[ElementList[_ferroEnv], Element] = None

    trafMut: Annotated[_trafMut, Element] = None
    fluxo: Annotated[str, Element] = None


