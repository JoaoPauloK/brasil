# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: retConsStatServ_v3.10.xsd
# xmlns: http://www.portalfiscal.inf.br/nfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .leiauteConsStatServ_v310 import *


class retConsStatServ(TRetConsStatServ):
    """Schema XML de validação do Resultado da Consulta do Status do Serviço"""
    _xmlns = "http://www.portalfiscal.inf.br/nfe"


