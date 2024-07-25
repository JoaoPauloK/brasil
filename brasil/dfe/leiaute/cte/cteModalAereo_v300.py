# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: cteModalAereo_v3.00.xsd
# xmlns: http://www.portalfiscal.inf.br/cte
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposGeralCTe_v300 import *


class aereo(ComplexType):
    """Informações do modal Aéreo"""
    _xmlns = "http://www.portalfiscal.inf.br/cte"
    nMinu: Annotated[str, Element] = None
    nOCA: Annotated[str, Element] = None
    dPrevAereo: Annotated[TData, Element] = None

    class _natCarga(ComplexType):
        """Natureza da carga"""
        xDime: Annotated[str, Element] = None
        cInfManu: Annotated[ElementList[str], Element] = None

    natCarga: Annotated[_natCarga, Element] = None

    class _tarifa(ComplexType):
        """Informações de tarifa"""
        CL: Annotated[str, Element] = None
        cTar: Annotated[str, Element] = None
        vTar: Annotated[TDec_1302, Element] = None

    tarifa: Annotated[_tarifa, Element] = None

    class _peri(ComplexType):
        """Preenchido quando for  transporte de produtos classificados pela ONU como perigosos.
O preenchimento desses campos não desobriga a empresa aérea de emitir os demais documentos que constam na legislação vigente."""
        nONU: Annotated[str, Element] = None
        qTotEmb: Annotated[str, Element] = None

        class _infTotAP(ComplexType):
            """Grupo de informações das quantidades totais de artigos perigosos
Preencher conforme a legislação de transporte de produtos perigosos aplicada ao modal"""
            qTotProd: Annotated[TDec_1104, Element] = None
            uniAP: Annotated[str, Element] = None

        infTotAP: Annotated[_infTotAP, Element] = None

    peri: Annotated[ElementList[_peri], Element] = None


