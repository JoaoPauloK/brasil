# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: procCTe_v2.00.xsd
# xmlns: http://www.portalfiscal.inf.br/cte
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .cteTiposBasico_v200 import *
from .consReciCTeTiposBasico_v200 import *


class cteProc(ComplexType):
    """ CT-e processado"""
    _xmlns = "http://www.portalfiscal.inf.br/cte"
    versao: Annotated[TVerCTe, Attribute] = None
    CTe: Annotated[TCTe, Element] = None
    protCTe: Annotated[TProtCTe, Element] = None


