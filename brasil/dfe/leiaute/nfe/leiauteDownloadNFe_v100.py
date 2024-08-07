# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: leiauteDownloadNFe_v1.00.xsd
# xmlns: http://www.portalfiscal.inf.br/nfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposBasico_v103 import *


class TVerDownloadNFe(str):
    """ Tipo Versão da consultaNFeDest"""
    pass


class TDownloadNFe(ComplexType):
    """Tipo Pedido de Download de NF-e"""
    versao: Annotated[TVerDownloadNFe, Attribute] = None
    tpAmb: Annotated[TAmb, Element] = None
    xServ: Annotated[str, Element] = None
    CNPJ: Annotated[TCnpj, Element] = None
    chNFe: Annotated[ElementList[TChNFe], Element] = None


class TRetDownloadNFe(ComplexType):
    """Tipo Retorno do pedido de Download de NF-e"""
    versao: Annotated[TVerDownloadNFe, Attribute] = None
    tpAmb: Annotated[TAmb, Element] = None
    verAplic: Annotated[TVerAplic, Element] = None
    cStat: Annotated[TStat, Element] = None
    xMotivo: Annotated[TMotivo, Element] = None
    dhResp: Annotated[datetime, Element] = None

    class _retNFe(ComplexType):
        """Conjunto de informação das  NF-e localizadas"""
        chNFe: Annotated[TChNFe, Element] = None
        cStat: Annotated[TStat, Element] = None
        xMotivo: Annotated[TMotivo, Element] = None

        class _procNFeGrupoZip(ComplexType):
            NFeZip: Annotated[base64Binary, Element] = None
            protNFeZip: Annotated[base64Binary, Element] = None

        procNFeGrupoZip: Annotated[_procNFeGrupoZip, Element] = None
        procNFeZip: Annotated[base64Binary, Element] = None

        class _procNFe(ComplexType):
            """XML do procNFe"""
            schema: Annotated[str, Attribute] = None

        procNFe: Annotated[_procNFe, Element] = None
        procNFeGrupoZip_procNFeZip_procNFe = Choice("procNFeGrupoZip", "procNFeZip", "procNFe")

    retNFe: Annotated[ElementList[_retNFe], Element] = None


