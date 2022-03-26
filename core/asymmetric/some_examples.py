# -*- coding: UTF-8 -*-
# common
from cryptography.hazmat.backends import default_backend
# asym
from cryptography.hazmat.primitives.asymmetric import padding as asym_padding
from cryptography.hazmat.primitives import serialization
from cryptography import x509


class AsymCrypto:
    ##########################################################
    # asymmetric cryptography
    ##########################################################
    def checkAsymPubKey(self, rsa_key):
        public_key = serialization.load_der_public_key(rsa_key, backend=default_backend())
        pass

    def checkAsymPrivKey(self, rsa_key, password=None):
        private_key = serialization.load_der_private_key(rsa_key, password=password, backend=default_backend())
        pass

    def checkSertificate(self, cert):
        certificate = x509.load_der_x509_certificate(cert, backend=default_backend())
        pass
