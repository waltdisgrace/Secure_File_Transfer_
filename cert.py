#!/usr/bin/env python3

from certauth.certauth import main, CertificateAuthority, FileCache, LRUCache, ROOT_CA

ca = CertificateAuthority('My Custom CA', 'cert.pem', cert_cache='/tmp/certs')
filename = ca.cert_for_host('test.server')

print(ca)
print(filename)
