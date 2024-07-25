# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: evGTV_v4.00.xsd
# xmlns: http://www.portalfiscal.inf.br/cte
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .eventoCTeTiposBasico_v400 import *


class evGTV(ComplexType):
    """Schema XML de validação do evento informações da GTV 110170"""
    _xmlns = "http://www.portalfiscal.inf.br/cte"
    descEvento: Annotated[str, Element] = None

    class _infGTV(ComplexType):
        """Grupo de Informações das GTV"""
        nDoc: Annotated[str, Element] = None
        id: Annotated[str, Element] = None
        serie: Annotated[str, Element] = None
        subserie: Annotated[str, Element] = None
        dEmi: Annotated[TData, Element] = None
        nDV: Annotated[str, Element] = None
        qCarga: Annotated[TDec_1104, Element] = None

        class _infEspecie(ComplexType):
            """Informações das Espécies transportadas"""
            tpEspecie: Annotated[str, Element] = None
            vEspecie: Annotated[TDec_1302, Element] = None

        infEspecie: Annotated[ElementList[_infEspecie], Element] = None

        class _rem(ComplexType):
            """Informações do Remetente da GTV"""
            CNPJ: Annotated[TCnpjOpc, Element] = None
            CPF: Annotated[TCpf, Element] = None
            CNPJ_CPF = Choice("CNPJ", "CPF")
            IE: Annotated[TIeDest, Element] = None
            UF: Annotated[TUf, Element] = None
            xNome: Annotated[str, Element] = None

        rem: Annotated[_rem, Element] = None

        class _dest(ComplexType):
            """Informações do Destinatário da GTV"""
            CNPJ: Annotated[TCnpjOpc, Element] = None
            CPF: Annotated[TCpf, Element] = None
            CNPJ_CPF = Choice("CNPJ", "CPF")
            IE: Annotated[TIeDest, Element] = None
            UF: Annotated[TUf, Element] = None
            xNome: Annotated[str, Element] = None

        dest: Annotated[_dest, Element] = None
        placa: Annotated[TPlaca, Element] = None
        UF: Annotated[TUf, Element] = None
        RNTRC: Annotated[str, Element] = None

    infGTV: Annotated[ElementList[_infGTV], Element] = None


