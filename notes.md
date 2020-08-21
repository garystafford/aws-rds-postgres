```bash
aws cloudformation validate-template \
  --template-body file://cfn-templates/rds.template

cfn-lint -t cfn-templates/rds.template

aws cloudformation create-stack \
  --template-body file://cfn-templates/event.template \
  --stack-name RDSEventDemoStack

aws cloudformation create-stack \
  --template-body file://cfn-templates/rds.template \
  --stack-name RDSDemoStack

# alternative
aws cloudformation create-stack \
  --template-body file://cfn-templates/rds_only.template \
  --stack-name RDSDemoStack

aws cloudformation delete-stack \
  --stack-name RDSDemoStack

aws rds describe-db-instances \
  --db-instance-identifier demo-instance

pip3 install --upgrade -r requirements.txt

cd python-scripts
time python3 ./create_pagila_data.py
# python3 ./create_pagila_data.py  0.11s user 0.06s system 2% cpu 7.341 total

time python3 ./query_postgres.py

# https://www.pgadmin.org/download/pgadmin-4-container/
docker pull dpage/pgadmin4
docker run -p 8180:80 \
  -e "PGADMIN_DEFAULT_EMAIL=user@domain.com" \
  -e "PGADMIN_DEFAULT_PASSWORD=SuperSecret" \
  -d dpage/pgadmin4

```
