# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: retEnvCancelPProrrogNFe_v1.0.xsd
# xmlns: http://www.portalfiscal.inf.br/nfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposBasico_v310 import *


class TCOrgaoIBGE(str):
    """Tipo Código de orgão (UF da tabela do IBGE + 91 RFB)"""
    pass


class retEnvEvento(ComplexType):
    """TAG raiz do Resultado do Envio do Evento"""
    _xmlns = "http://www.portalfiscal.inf.br/nfe"
    versao: Annotated[str, Attribute(pattern=r'[0-9]{2}\.[0-9]{2}')] = None
    idLote: Annotated[str, Element] = None
    tpAmb: Annotated[TAmb, Element] = None
    verAplic: Annotated[TVerAplic, Element] = None
    cOrgao: Annotated[TCOrgaoIBGE, Element] = None
    cStat: Annotated[TStat, Element] = None
    xMotivo: Annotated[TMotivo, Element] = None

    class _retEvento(ComplexType):
        """TAG de grupo do resultado do processamento do Evento"""
        versao: Annotated[str, Attribute(pattern=r'[0-9]{2}\.[0-9]{2}')] = None

        class _infEvento(ComplexType):
            """Grupo de informações do registro do Evento"""
            Id: Annotated[str, Attribute(pattern=r'ID[0-9]{52}')] = None
            tpAmb: Annotated[TAmb, Element] = None
            verAplic: Annotated[TVerAplic, Element] = None
            cOrgao: Annotated[TCOrgaoIBGE, Element] = None
            cStat: Annotated[TStat, Element] = None
            xMotivo: Annotated[TMotivo, Element] = None
            chNFe: Annotated[TChNFe, Element] = None
            tpEvento: Annotated[str, Element] = None
            xEvento: Annotated[str, Element] = None
            nSeqEvento: Annotated[str, Element] = None
            CNPJDest: Annotated[TCnpjOpc, Element] = None
            emailDest: Annotated[str, Element] = None
            dhRegEvento: Annotated[TDateTimeUTC, Element] = None
            nProt: Annotated[TProt, Element] = None

        infEvento: Annotated[_infEvento, Element] = None
        Signature: Annotated[XmlSignature, Element] = None

    retEvento: Annotated[ElementList[_retEvento], Element] = None


