# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: cteModalRodoviarioOS_v4.00.xsd
# xmlns: http://www.portalfiscal.inf.br/cte
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposGeralCTe_v400 import *
from .cteTiposBasico_v400 import *


class TTermoAutFreta(str):
    """Tipo Termo  de Autorização de Fretamento – TAF"""
    pass


class TNroRegEstadual(str):
    """Tipo Número de Registro Estadual"""
    pass


class rodoOS(ComplexType):
    """Informações do modal Rodoviário"""
    TAF: Annotated[TTermoAutFreta, Element] = None
    NroRegEstadual: Annotated[TNroRegEstadual, Element] = None
    TAF_NroRegEstadual = Choice("TAF", "NroRegEstadual")

    class _veic(ComplexType):
        """Dados do Veículo"""
        placa: Annotated[TPlaca, Element] = None
        RENAVAM: Annotated[str, Element] = None

        class _prop(ComplexType):
            """Proprietário ou possuidor do Veículo.
Só preenchido quando o veículo não pertencer à empresa emitente do CT-e OS"""
            CPF: Annotated[TCpf, Element] = None
            CNPJ: Annotated[TCnpjOpc, Element] = None
            CPF_CNPJ = Choice("CPF", "CNPJ")
            TAF: Annotated[TTermoAutFreta, Element] = None
            NroRegEstadual: Annotated[TNroRegEstadual, Element] = None
            TAF_NroRegEstadual = Choice("TAF", "NroRegEstadual")
            xNome: Annotated[str, Element] = None
            IE: Annotated[TIeDest, Element] = None
            UF: Annotated[TUf, Element] = None
            tpProp: Annotated[str, Element] = None

        prop: Annotated[_prop, Element] = None
        UF: Annotated[TUf, Element] = None

    veic: Annotated[_veic, Element] = None

    class _infFretamento(ComplexType):
        """Dados do fretamento (apenas para Transporte de Pessoas)"""
        tpFretamento: Annotated[str, Element] = None
        dhViagem: Annotated[TDateTimeUTC, Element] = None

    infFretamento: Annotated[_infFretamento, Element] = None


