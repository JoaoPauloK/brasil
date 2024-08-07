import os
from datetime import datetime

from lxml import etree
from OpenSSL import crypto

try:
    import signxml


    class BrasilXMLSigner(signxml.XMLSigner):
        def check_deprecated_methods(self):
            pass
except:
    pass


class Certificado(object):
    _loaded = False
    _pfx_file = None
    _pkcs12 = None
    _cert = None
    _key = None
    cert_file = None
    key_file = None

    def __init__(self, pfx, senha: str):
        self.senha = senha
        if isinstance(pfx, bytes):
            self.pfx = pfx
        else:
            self._pfx_file = pfx
            with open(pfx, 'rb') as f:
                self.pfx = f.read()
            # gerar automaticamente o par de arquivos certs
            self.cert_file, self.key_file = self.get_certificado(pfx, senha, replace=False)

    def load(self):
        if not self._loaded:
            cert = crypto.dump_certificate(crypto.FILETYPE_PEM, self.pkcs12.get_certificate())
            certificate = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
            # Obter informações do certificado
            self._emissor = dict(certificate.get_issuer().get_components())
            self._proprietario = dict(certificate.get_subject().get_components())
            self._emissao = datetime.strptime(certificate.get_notBefore().decode('utf-8'), '%Y%m%d%H%M%SZ')
            self._validade = datetime.strptime(certificate.get_notAfter().decode('utf-8'), '%Y%m%d%H%M%SZ')
            self._loaded = True

    @property
    def arquivo_certificado(self):
        self.load()
        return self._arquivo_certificado

    @property
    def arquivo_chave(self):
        self.load()
        return self._arquivo_chave

    @property
    def emissor(self):
        self.load()
        return self._emissor

    @property
    def proprietario(self):
        self.load()
        return self._proprietario

    @property
    def emissao(self):
        self.load()
        return self._emissao

    @property
    def validade(self):
        self.load()
        return self._validade

    @property
    def pkcs12(self):
        if self._pkcs12 is None:
            self._pkcs12 = crypto.load_pkcs12(self.pfx, self.senha.encode('utf-8'))
        return self._pkcs12

    @property
    def cert(self):
        if self._cert is None:
            self._cert, self._key = self._get_cert()
        return self._cert

    @property
    def key(self):
        if self._key is None:
            self._cert, self._key = self._get_cert()
        return self._key

    def _get_cert(self):
        p = self.pkcs12
        self.privatekey = p.get_privatekey()
        pkey = crypto.dump_privatekey(crypto.FILETYPE_PEM, self.privatekey)
        cert = crypto.dump_certificate(crypto.FILETYPE_PEM, p.get_certificate())
        return cert, pkey

    def split_cert(self, pfx, pwd, cert_file, key_file):
        cert, pkey = self._get_cert()
        with open(key_file, 'wb') as pem_key:
            pem_key.write(pkey)
        with open(cert_file, 'wb') as crt_file:
            crt_file.write(cert)
        return cert, pkey

    def get_certificado(self, cert, pwd, replace=True):
        cert_file = cert + '.cert'
        key_file = cert + '.key'
        if not replace and os.path.isfile(cert_file):
            return cert_file, key_file
        self.certificado, self.chave = self.split_cert(cert, pwd, cert_file, key_file)
        return cert_file, key_file

    def assinar(self, xml, ref):
        if isinstance(xml, (str, bytes)):
            xml = etree.fromstring(xml)
        signer = BrasilXMLSigner(
            method=signxml.methods.enveloped,
            signature_algorithm='rsa-sha1',
            digest_algorithm='sha1',
            c14n_algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315",
        )
        signer.namespaces = {None: signer.namespaces['ds']}
        uri = '#' + ref
        signed = signer.sign(
            xml, key=self.key, cert=self.cert, reference_uri=uri, id_attribute='Id',
        ).find(".//{http://www.w3.org/2000/09/xmldsig#}Signature")
        res = etree.tostring(signed, encoding=str)
        return res
