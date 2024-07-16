# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: procCTeOS_v3.00.xsd
# xmlns: http://www.portalfiscal.inf.br/cte
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .cteTiposBasico_v300 import *


class cteOSProc(ComplexType):
    """ CT-e OS processado"""
    versao: Annotated[TVerCTe, Attribute] = None
    ipTransmissor: Annotated[TIPv4, Attribute] = None
    CTeOS: Annotated[TCTeOS, Element] = None
    protCTe: Annotated[TProtCTeOS, Element] = None


