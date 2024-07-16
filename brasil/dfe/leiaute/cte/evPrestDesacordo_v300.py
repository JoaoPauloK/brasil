# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: evPrestDesacordo_v3.00.xsd
# xmlns: http://www.portalfiscal.inf.br/cte
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .eventoCTeTiposBasico_v300 import *


class evPrestDesacordo(ComplexType):
    """Schema XML de validação do evento Prestação do Serviço em Desacordo 610110"""
    descEvento: Annotated[str, Element] = None
    indDesacordoOper: Annotated[str, Element] = None
    xObs: Annotated[str, Element] = None


