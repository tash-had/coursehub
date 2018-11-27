from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend
from flask import abort
import jwt

from api.user.user import User

CERT_STR = """-----BEGIN CERTIFICATE-----
MIIDATCCAemgAwIBAgIJYSI1kZU4KgmYMA0GCSqGSIb3DQEBCwUAMB4xHDAaBgNV
BAMTE2NvdXJzZWh1Yi5hdXRoMC5jb20wHhcNMTgxMTI0MDUzNDAzWhcNMzIwODAy
MDUzNDAzWjAeMRwwGgYDVQQDExNjb3Vyc2VodWIuYXV0aDAuY29tMIIBIjANBgkq
hkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA7tkBUc+fnrbx34WtGd3ZqoYdXaPIsCwy
FF77I5bZMA2Yct+XpS2L/Wjxj9ZVR86GYR35oK1X3Gq+UfPJVT0W7rdf4QmlZPvq
Gt0DyADgMFPXyizt+euE5BLjNf+O8w/p6I0OsSP+/sA46KijHwWzYVcsZu8hHn91
S5xLWaBtibESVy+lrTqzmmcOsWIqxieL70C33cbalsrBjrDK6FzxHX6Qx/zdfWfU
nTOxU1TJ9eo7hO6cuIbpSR3iZw8AwKtEorcv/EOTv+nHgAMygnbUApiqFjddbwVj
6y/+F3bkxS/2yZh7X84oZoJrmYzp+3AkuP6AKHaVJOZVQOiu9d9H5wIDAQABo0Iw
QDAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBSQTTUUB9/k+dUwyl0GPsmlJsEf
+zAOBgNVHQ8BAf8EBAMCAoQwDQYJKoZIhvcNAQELBQADggEBAEA638Cae/AkyjO2
SSUYZD2jFtM7HWvLjaCkNjLfpPsE4vFSA5Ci6D5EI98l4w/7OFlD6HwUIC71xR49
rJwJs//ReNa3HqOibQb+BU6+mZVGxIO+kQyvyg0ORSXq31NLkGRbc3g3zXGLvMSp
j/pvW63CrM3/RUIHsY5h52O0HIPhK7eFkHGl9NVbYnehISzletZ7Vi/5jUXcqXRG
UyUysHuJCpkixxenLHLYIL1HUAY/jH78KCvgu1UWwLEqS0/uGz3h+q2h8Cg9xZbu
CE/gaQA6kBcW2sKbrrMBVIMhUnOj1axSp9VTg441e80gKlPZ08dpwtLl4CY/Hwah
HzSgo34=
-----END CERTIFICATE-----"""


def decode_jwt(jwt_str):
    try:
        cert_obj = load_pem_x509_certificate(str.encode(CERT_STR), default_backend())
        public_key = cert_obj.public_key()
        return jwt.decode(jwt_str, public_key, algorithms=["RS256"], audience="3B3L1WG7c9WyVhi117UJqXSiOmfLWoH7")
    except Exception as e:
        print(e)


def get_user_data(req):
    id_token = req.headers.get("Authorization")
    user_data = decode_jwt(id_token)
    if not id_token or not user_data:
        abort(403)
    return user_data


def get_user_with_request(req):
    user_data = get_user_data(req)
    return User(user_data["sub"][6:], user_data["nickname"], user_data["name"], user_data["picture"])
