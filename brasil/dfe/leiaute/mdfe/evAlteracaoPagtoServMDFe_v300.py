# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: evAlteracaoPagtoServMDFe_v3.00.xsd
# xmlns: http://www.portalfiscal.inf.br/mdfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .eventoMDFeTiposBasico_v300 import *


class evAlteracaoPagtoServMDFe(ComplexType):
    """Schema XML de validação do evento de alteração do pagamento do serviçp de transporte 110118"""
    _xmlns = "http://www.portalfiscal.inf.br/mdfe"
    descEvento: Annotated[str, Element] = None
    nProt: Annotated[TProt, Element] = None

    class _infPag(ComplexType):
        """Informações do Pagamento do Frete"""
        xNome: Annotated[str, Element] = None
        CPF: Annotated[TCpf, Element] = None
        CNPJ: Annotated[TCnpjOpc, Element] = None
        idEstrangeiro: Annotated[str, Element] = None
        CPF_CNPJ_idEstrangeiro = Choice("CPF", "CNPJ", "idEstrangeiro")

        class _Comp(ComplexType):
            """Componentes do Pagamentoi do Frete"""
            tpComp: Annotated[str, Element] = None
            vComp: Annotated[TDec_1302, Element] = None
            xComp: Annotated[str, Element] = None

        Comp: Annotated[ElementList[_Comp], Element] = None
        vContrato: Annotated[TDec_1302, Element] = None
        indPag: Annotated[str, Element] = None
        vAdiant: Annotated[TDec_1302, Element] = None
        indAntecipaAdiant: Annotated[str, Element] = None

        class _infPrazo(ComplexType):
            """Informações do pagamento a prazo. 
Informar somente se indPag for à Prazo"""
            nParcela: Annotated[str, Element] = None
            dVenc: Annotated[TData, Element] = None
            vParcela: Annotated[TDec_1302Opc, Element] = None

        infPrazo: Annotated[ElementList[_infPrazo], Element] = None
        tpAntecip: Annotated[str, Element] = None

        class _infBanc(ComplexType):
            """Informações bancárias"""
            codBanco: Annotated[str, Element] = None
            codAgencia: Annotated[str, Element] = None
            CNPJIPEF: Annotated[TCnpjOpc, Element] = None
            PIX: Annotated[str, Element] = None
            CNPJIPEF_PIX = Choice("CNPJIPEF", "PIX")

        infBanc: Annotated[_infBanc, Element] = None

    infPag: Annotated[ElementList[_infPag], Element] = None


