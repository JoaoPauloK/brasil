# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: retCTeSimp_v4.00.xsd
# xmlns: http://www.portalfiscal.inf.br/cte
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .cteTiposBasico_v400 import *


class retCTeSimp(TRetCTeSimp):
    """Schema XML de validação do retorno do recibo de envio do CT-e Simplificado (Modelo 57)"""
    _xmlns = "http://www.portalfiscal.inf.br/cte"


