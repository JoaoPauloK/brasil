# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: retConsMDFeNaoEnc_v3.00.xsd
# xmlns: http://www.portalfiscal.inf.br/mdfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .consMDFeNaoEncTiposBasico_v300 import *


class retConsMDFeNaoEnc(TRetConsMDFeNaoEnc):
    """Schema XML de validação do retorno da consulta MDF-e não encerrados"""
    _xmlns = "http://www.portalfiscal.inf.br/mdfe"


