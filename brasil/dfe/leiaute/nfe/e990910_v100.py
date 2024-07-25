# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: e990910_v1.00.xsd
# xmlns: http://www.portalfiscal.inf.br/nfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposBasico_v103 import *


class detEvento(ComplexType):
    """Schema XML de validação do evento do Confirmação de Internalização da Mercadoria na SUFRAMA 990910"""
    _xmlns = "http://www.portalfiscal.inf.br/nfe"
    versao: Annotated[str, Attribute(enumeration=['1.00'])] = None
    descEvento: Annotated[str, Element] = None
    PINe: Annotated[str, Element] = None
    dVistoria: Annotated[TDateTimeUTC, Element] = None
    locVistoria: Annotated[str, Element] = None
    postoVistoria: Annotated[str, Element] = None
    xHistorico: Annotated[str, Element] = None


