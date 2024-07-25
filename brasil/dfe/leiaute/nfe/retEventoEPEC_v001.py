# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: retEventoEPEC_v0.01.xsd
# xmlns: http://www.portalfiscal.inf.br/nfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposBasico_v310 import *


class TVerEvento(str):
    """Tipo Versão do Evento"""
    pass


class TCOrgaoIBGE(str):
    """Tipo Código de orgão (UF da tabela do IBGE + 91 RFB)"""
    pass


class retEnvEvento(ComplexType):
    _xmlns = "http://www.portalfiscal.inf.br/nfe"
    versao: Annotated[TVerEvento, Attribute] = None
    idLote: Annotated[str, Element] = None
    tpAmb: Annotated[TAmb, Element] = None
    verAplic: Annotated[TVerAplic, Element] = None
    cOrgao: Annotated[TCOrgaoIBGE, Element] = None
    cStat: Annotated[TStat, Element] = None
    xMotivo: Annotated[TMotivo, Element] = None

    class _retEvento(ComplexType):
        """TAG de grupo do resultado do processamento do Evento"""
        versao: Annotated[TVerEvento, Attribute] = None

        class _infEvento(ComplexType):
            """Grupo de informações do registro do Evento"""
            Id: Annotated[str, Attribute] = None
            tpAmb: Annotated[TAmb, Element] = None
            verAplic: Annotated[TVerAplic, Element] = None
            cOrgao: Annotated[TCOrgaoIBGE, Element] = None
            cStat: Annotated[TStat, Element] = None
            xMotivo: Annotated[TMotivo, Element] = None
            chNFe: Annotated[TChNFe, Element] = None
            tpEvento: Annotated[str, Element] = None
            xEvento: Annotated[str, Element] = None
            nSeqEvento: Annotated[str, Element] = None
            cOrgaoAutor: Annotated[TCodUfIBGE, Element] = None
            dhRegEvento: Annotated[TDateTimeUTC, Element] = None
            nProt: Annotated[TProt, Element] = None
            chNFePend: Annotated[ElementList[TChNFe], Element] = None

        infEvento: Annotated[_infEvento, Element] = None
        Signature: Annotated[XmlSignature, Element] = None

    retEvento: Annotated[ElementList[_retEvento], Element] = None


