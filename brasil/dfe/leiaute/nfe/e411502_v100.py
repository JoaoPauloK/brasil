# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: e411502_v1.00.xsd
# xmlns: http://www.portalfiscal.inf.br/nfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposBasico_v103 import *


class TRespCancPedido(ComplexType):
    """Resposta a um tpEvento 111502 ou 111503."""
    statCancPedido: Annotated[str, Element] = None
    justStatus: Annotated[str, Element] = None
    justStaOutra: Annotated[str, Element] = None


class detEvento(ComplexType):
    """Informações do Fisco"""
    versao: Annotated[str, Attribute(enumeration=['1.00'])] = None
    descEvento: Annotated[str, Element] = None
    idPedido: Annotated[str, Element] = None
    respCancPedido: Annotated[TRespCancPedido, Element] = None


