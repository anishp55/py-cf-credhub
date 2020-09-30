from flask import json
from app import app
from  OpenSSL import crypto
import json
import os

@app.route('/')
def enter():
    services = json.loads(os.getenv("VCAP_SERVICES"))
    cert = crypto.load_certificate( crypto.FILETYPE_PEM,
                                    services['credhub'][0]['credentials']['cert1'] )
    chain = crypto.load_certificate( crypto.FILETYPE_PEM,
                                     services['credhub'][0]['credentials']['chain1'] )
    data = { "cert1" : 
                        {
                            "issuer": cert.get_issuer().CN, 
                            "subject": cert.get_subject().CN    
                        },
             "chain1":                        
                        {
                            "issuer": chain.get_issuer().CN, 
                            "subject": chain.get_subject().CN    
                        }
            }

    certFile = open("chain.pem","w")
    certFile.write(services['credhub'][0]['credentials']['chain1'])
    certFile.close()  

    AZURE_CLIENT_ID = services['credhub'][0]['credentials']['AZURE_CLIENT_ID']
    AZURE_CLIENT_SECRET = services['credhub'][0]['credentials']['AZURE_CLIENT_SECRET']
    AZURE_TENANT_ID = services['credhub'][0]['credentials']['AZURE_TENANT_ID']
    vaultUri = services['credhub'][0]['credentials']['vaultUri']

    return (data)

@app.route("/health", methods=['GET'])
@app.route("/healthz", methods=['GET'])
def health():
    return "OK"