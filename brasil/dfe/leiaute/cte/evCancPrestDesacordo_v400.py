# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: evCancPrestDesacordo_v4.00.xsd
# xmlns: http://www.portalfiscal.inf.br/cte
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .eventoCTeTiposBasico_v400 import *


class evCancPrestDesacordo(ComplexType):
    """Schema XML de validação do evento Cancelamento Prestação do Serviço em Desacordo 610111"""
    descEvento: Annotated[str, Element] = None
    nProtEvPrestDes: Annotated[TProt, Element] = None


