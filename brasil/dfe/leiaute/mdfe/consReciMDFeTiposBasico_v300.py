# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: consReciMDFeTiposBasico_v3.00.xsd
# xmlns: http://www.portalfiscal.inf.br/mdfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposGeralMDFe_v300 import *


class TVerConsReciMDFe(str):
    """ Tipo Versão do Consulta de MDF-e - 3.00"""
    pass


class TProtMDFe(ComplexType):
    """Tipo Protocolo de status resultado do processamento do MDF-e"""
    versao: Annotated[TVerConsReciMDFe, Attribute] = None

    class _infProt(ComplexType):
        """Dados do protocolo de status"""
        Id: Annotated[str, Attribute] = None
        tpAmb: Annotated[TAmb, Element] = None
        verAplic: Annotated[TVerAplic, Element] = None
        chMDFe: Annotated[TChMDFe, Element] = None
        dhRecbto: Annotated[TDateTimeUTC, Element] = None
        nProt: Annotated[TProt, Element] = None
        digVal: Annotated[TXML, Element] = None
        cStat: Annotated[TStat, Element] = None
        xMotivo: Annotated[TMotivo, Element] = None

    infProt: Annotated[_infProt, Element] = None

    class _infFisco(ComplexType):
        """Mensagem do Fisco"""
        cMsg: Annotated[TStat, Element] = None
        xMsg: Annotated[TMotivo, Element] = None

    infFisco: Annotated[_infFisco, Element] = None
    Signature: Annotated[XmlSignature, Element] = None


class TConsReciMDFe(ComplexType):
    """Tipo Pedido de Consulta do Recibo do MDF-e"""
    versao: Annotated[TVerConsReciMDFe, Attribute] = None
    tpAmb: Annotated[TAmb, Element] = None
    nRec: Annotated[TRec, Element] = None


class TRetConsReciMDFe(ComplexType):
    """Tipo Retorno do Pedido de  Consulta do Recibo do MDF-e"""
    versao: Annotated[TVerConsReciMDFe, Attribute] = None
    tpAmb: Annotated[TAmb, Element] = None
    verAplic: Annotated[TVerAplic, Element] = None
    nRec: Annotated[TRec, Element] = None
    cStat: Annotated[TStat, Element] = None
    xMotivo: Annotated[TMotivo, Element] = None
    cUF: Annotated[TCodUfIBGE, Element] = None
    protMDFe: Annotated[TProtMDFe, Element] = None


