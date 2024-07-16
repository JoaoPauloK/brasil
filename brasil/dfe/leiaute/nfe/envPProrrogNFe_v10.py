# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: envPProrrogNFe_v1.0.xsd
# xmlns: http://www.portalfiscal.inf.br/nfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposBasico_v310 import *


class detEvento(ComplexType):
    """Informações do Pedido de Prorrogação"""
    versao: Annotated[str, Attribute(enumeration=['1.00'])] = None
    descEvento: Annotated[str, Element] = None
    nProt: Annotated[TProt, Element] = None

    class _itemPedido(ComplexType):
        """Item do Pedido de Prorrogação. Recomenda-se agrupar a maior quantidade de itens em cada Pedido de Prorrogação"""
        numItem: Annotated[str, Attribute(pattern=r'[0-9]{1,3}')] = None
        qtdeItem: Annotated[TDec_1104v, Element] = None

    itemPedido: Annotated[ElementList[_itemPedido], Element] = None


