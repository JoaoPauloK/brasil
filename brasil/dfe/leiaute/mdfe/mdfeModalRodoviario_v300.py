# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: mdfeModalRodoviario_v3.00.xsd
# xmlns: http://www.portalfiscal.inf.br/mdfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposGeralMDFe_v300 import *


class TRNTRC(str):
    """Tipo RNTRC - Registro Nacional Transportadores Rodoviários de Carga"""
    pass


class TCIOT(str):
    """Tipo CIOT - Código Identificador da Operação de Transporte"""
    pass


class rodo(ComplexType):
    """Informações do modal Rodoviário"""
    _xmlns = "http://www.portalfiscal.inf.br/mdfe"

    class _infANTT(ComplexType):
        """Grupo de informações para Agência Reguladora"""
        RNTRC: Annotated[TRNTRC, Element] = None

        class _infCIOT(ComplexType):
            """Dados do CIOT"""
            CIOT: Annotated[TCIOT, Element] = None
            CPF: Annotated[TCpf, Element] = None
            CNPJ: Annotated[TCnpjOpc, Element] = None
            CPF_CNPJ = Choice("CPF", "CNPJ")

        infCIOT: Annotated[ElementList[_infCIOT], Element] = None

        class _valePed(ComplexType):
            """Informações de Vale Pedágio
Outras informações sobre Vale-Pedágio obrigatório que não tenham campos específicos devem ser informadas no campo de observações gerais de uso livre pelo contribuinte, visando atender as determinações legais vigentes."""

            class _disp(ComplexType):
                """Informações dos dispositivos do Vale Pedágio"""
                CNPJForn: Annotated[TCnpj, Element] = None
                CNPJPg: Annotated[TCnpjOpc, Element] = None
                CPFPg: Annotated[TCpf, Element] = None
                CNPJPg_CPFPg = Choice("CNPJPg", "CPFPg")
                nCompra: Annotated[str, Element] = None
                vValePed: Annotated[TDec_1302, Element] = None
                tpValePed: Annotated[str, Element] = None

            disp: Annotated[ElementList[_disp], Element] = None
            categCombVeic: Annotated[str, Element] = None

        valePed: Annotated[_valePed, Element] = None

        class _infContratante(ComplexType):
            """Grupo de informações dos contratantes do serviço de transporte"""
            xNome: Annotated[str, Element] = None
            CPF: Annotated[TCpf, Element] = None
            CNPJ: Annotated[TCnpjOpc, Element] = None
            idEstrangeiro: Annotated[str, Element] = None
            CPF_CNPJ_idEstrangeiro = Choice("CPF", "CNPJ", "idEstrangeiro")

            class _infContrato(ComplexType):
                """Grupo de informações do contrato entre transportador e contratante"""
                NroContrato: Annotated[str, Element] = None
                vContratoGlobal: Annotated[TDec_1302Opc, Element] = None

            infContrato: Annotated[_infContrato, Element] = None

        infContratante: Annotated[ElementList[_infContratante], Element] = None

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
            indAltoDesemp: Annotated[str, Element] = None
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

    infANTT: Annotated[_infANTT, Element] = None

    class _veicTracao(ComplexType):
        """Dados do Veículo com a Tração"""
        cInt: Annotated[str, Element] = None
        placa: Annotated[TPlaca, Element] = None
        RENAVAM: Annotated[str, Element] = None
        tara: Annotated[str, Element] = None
        capKG: Annotated[str, Element] = None
        capM3: Annotated[str, Element] = None

        class _prop(ComplexType):
            """Proprietário ou possuidor do Veículo.
Só preenchido quando o veículo não pertencer à empresa emitente do MDF-e"""
            CPF: Annotated[TCpf, Element] = None
            CNPJ: Annotated[TCnpjOpc, Element] = None
            CPF_CNPJ = Choice("CPF", "CNPJ")
            RNTRC: Annotated[TRNTRC, Element] = None
            xNome: Annotated[str, Element] = None
            IE: Annotated[TIeDest, Element] = None
            UF: Annotated[TUf, Element] = None
            tpProp: Annotated[str, Element] = None

        prop: Annotated[_prop, Element] = None

        class _condutor(ComplexType):
            """Informações do(s) Condutor(es) do veículo"""
            xNome: Annotated[str, Element] = None
            CPF: Annotated[TCpf, Element] = None

        condutor: Annotated[ElementList[_condutor], Element] = None
        tpRod: Annotated[str, Element] = None
        tpCar: Annotated[str, Element] = None
        UF: Annotated[TUf, Element] = None

    veicTracao: Annotated[_veicTracao, Element] = None

    class _veicReboque(ComplexType):
        """Dados dos reboques"""
        cInt: Annotated[str, Element] = None
        placa: Annotated[TPlaca, Element] = None
        RENAVAM: Annotated[str, Element] = None
        tara: Annotated[str, Element] = None
        capKG: Annotated[str, Element] = None
        capM3: Annotated[str, Element] = None

        class _prop(ComplexType):
            """Proprietários ou possuidor do Veículo.
Só preenchido quando o veículo não pertencer à empresa emitente do MDF-e"""
            CPF: Annotated[TCpf, Element] = None
            CNPJ: Annotated[TCnpjOpc, Element] = None
            CPF_CNPJ = Choice("CPF", "CNPJ")
            RNTRC: Annotated[TRNTRC, Element] = None
            xNome: Annotated[str, Element] = None
            IE: Annotated[TIeDest, Element] = None
            UF: Annotated[TUf, Element] = None
            tpProp: Annotated[str, Element] = None

        prop: Annotated[_prop, Element] = None
        tpCar: Annotated[str, Element] = None
        UF: Annotated[TUf, Element] = None

    veicReboque: Annotated[ElementList[_veicReboque], Element] = None
    codAgPorto: Annotated[str, Element] = None

    class _lacRodo(ComplexType):
        """Lacres"""
        nLacre: Annotated[str, Element] = None

    lacRodo: Annotated[ElementList[_lacRodo], Element] = None


