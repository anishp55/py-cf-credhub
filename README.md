simple cf app that loads pem files from credhub  
export your certs and anything you want in your json as env vars  
ie: `export cert=$( awk 'NF {sub(/\r/, ""); printf "%s\\n",$0;}' <cert> )`  
create the json for credhub
```
export JSON=$(jq -n \                                       
--arg cert1 "$cert1" \
--arg chain1 "$chain1" \
--arg AZURE_CLIENT_ID "$AZURE_CLIENT_ID" \
--arg AZURE_CLIENT_SECRET "$AZURE_CLIENT_SECRET" \
--arg  AZURE_TENANT_ID "$AZURE_TENANT_ID" \
--arg vaultUri "$vaultUri" \
 '{cert1 : $cert1, AZURE_CLIENT_ID : $AZURE_CLIENT_ID, AZURE_CLIENT_SECRET : $AZURE_CLIENT_SECRET, AZURE_TENANT_ID : $AZURE_TENANT_ID ,  vaultUri: $vaultUri, chain1 : $chain1 }')
```
update the credhub service instance
```
echo $JSON > json.data
cf update-service <service instance name> -c json.data
```

push the app and see who issued the certs.