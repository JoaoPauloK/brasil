# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: retEnvSuframaVistoria_v1.00.xsd
# xmlns: http://www.portalfiscal.inf.br/nfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .leiauteSuframaVistoria_v100 import *


class retEnvEvento(TRetEnvEvento):
    """Schema XML de Retorno da envio do evento do Vistoria SUFRAMA 990900"""
    _xmlns = "http://www.portalfiscal.inf.br/nfe"


