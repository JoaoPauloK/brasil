# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: evCancCTe_v3.00.xsd
# xmlns: http://www.portalfiscal.inf.br/cte
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .eventoCTeTiposBasico_v300 import *


class evCancCTe(ComplexType):
    """Schema XML de validação do evento do cancelamento 
110111"""
    descEvento: Annotated[str, Element] = None
    nProt: Annotated[TProt, Element] = None
    xJust: Annotated[TJust, Element] = None


