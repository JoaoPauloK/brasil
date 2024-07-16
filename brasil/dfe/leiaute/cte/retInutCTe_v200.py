# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: retInutCTe_v2.00.xsd
# xmlns: http://www.portalfiscal.inf.br/cte
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .inutCTeTiposBasico_v200 import *


class retInutCTe(TRetInutCTe):
    """Schema XML de validação do retorno do Pedido de Inutilização de Numeração do CT-e"""
    _xmlns = "http://www.portalfiscal.inf.br/cte"


