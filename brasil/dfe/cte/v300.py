import decimal
import os

from lxml import etree

import brasil.dfe.leiaute.cte.cte_v300
import brasil.dfe.leiaute.cte.procCTe_v300
from brasil.dfe.leiaute.cte.cteModalRodoviario_v300 import rodo
from brasil.utils.text import remover_acentos


class CTe(brasil.dfe.leiaute.cte.cte_v300.CTe):
    _config = None
    _schema = None

    def _validate_schema(self):
        if CTe._schema is None:
            CTe._schema = etree.XMLSchema(
                file=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'schemas', 'cte',
                                  'cte_v3.00.xsd')
            )
        if not self._schema.validate(etree.fromstring(self._xml())):
            return self._schema.error_log.last_error.message

    @property
    def rodo(self) -> rodo:
        return self.infCte.infCTeNorm.infModal.rodo

    def _prepare(self):
        if self._config:
            config = self._config
            if self.infCte.ide.tpAmb == '2':
                if str(self.infCte.ide.tpEmis) == '8' and config.orgao in (31, 41, 50, 51):
                    url = config.services.get('URL-QRCode', config.get_uf_emis(), config.amb)
                else:
                    url = config.services.get('URL-QRCode', config.uf, config.amb)
            else:
                url = config.services.get('URL-QRCode', config.uf, config.amb)
            if '?' not in url:
                url += '?'
            url += f'chCTe={self.chave}&tpAmb={config.amb}'
            self.infCTeSupl.qrCodCTe = f'<![CDATA[{url}]]>'

    def _xml(self, name=None):
        self._prepare()
        return remover_acentos(super()._xml(name)).decode('utf-8')

