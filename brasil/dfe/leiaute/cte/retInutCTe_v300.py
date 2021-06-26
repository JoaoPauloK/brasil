from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .inutCTeTiposBasico_v300 import *



class retInutCTe(ComplexType):
    """Schema XML de validação do retorno do Pedido de Inutilização de Numeração do CT-e"""
    pass

retInutCTe: retInutCTe = Element(retInutCTe, documentation=['Schema XML de validação do retorno do Pedido de Inutilização de Numeração do CT-e'])
