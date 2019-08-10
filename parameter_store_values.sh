#!/usr/bin/env bash

# Write RDS demo parameters to Parameter Store

# Put parameters into Parameter Store
aws ssm put-parameter \
  --name /rds_demo/db_name \
  --type String \
  --value "pagila" \
  --description "Demo database name" \
  --overwrite

aws ssm put-parameter \
  --name /rds_demo/master_username \
  --type String \
  --value "masteruser" \
  --description "Master Username for database" \
  --overwrite

aws ssm put-parameter \
  --name /rds_demo/master_password \
  --type SecureString \
  --value "5up3r53cr3tPa55w0rd" \
  --description "Master Password for database" \
  --overwrite

aws ssm put-parameter \
  --name /rds_demo/alert_phone \
  --type String \
  --value "your_mobile_phone_number" \
  --description "RDS alert SMS phone number" \
  --overwrite

# Get parameters from Parameter Store
aws ssm get-parameter \
  --name /rds_demo/db_name \
  #--query Parameter.Value

aws ssm get-parameter \
  --name /rds_demo/master_username \
  #--query Parameter.Value

aws ssm get-parameter \
  --with-decryption \
  --name /rds_demo/master_password \
  #--query Parameter.Value

aws ssm get-parameter \
  --name /rds_demo/alert_phone \
  #--query Parameter.Name
