# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: retConsStatServMDFe_v3.00.xsd
# xmlns: http://www.portalfiscal.inf.br/mdfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .consStatServTiposBasico_v300 import *


class retConsStatServMDFe(TRetConsStatServ):
    """Schema XML de validação do Resultado da Consulta do Status do Serviço de MDF-e"""
    _xmlns = "http://www.portalfiscal.inf.br/mdfe"


