#!/usr/bin/sh
curl --location --request POST 'https://data.mongodb-api.com/app/data-wohqc/endpoint/data/v1/action/findOne' \
--header 'Content-Type: application/json' \
--header 'Access-Control-Request-Headers: *' \
--header 'api-key: M0ZWwjDiExkbbrcyirs08kWjRO8RBX9QJmDjr0kiEcYBGEeGWXyZO1LOUSn4AezP' \
--data-raw '{
    "collection":"CNN_NEWS",
    "database":"Nakheel",
    "dataSource":"Ambalatharasu",
    "projection": {}
}'