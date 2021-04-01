## DJANGO-STARTER

### DEVELOPMENT SETUP
**Deleting Development Setup**
`docker-compose -f dc-local.yml down -v`

**Creating Development Setup**
`docker-compose -f dc-local.yml up --build`

### PRODUCTION SETUP
**Deleting Production Setup**
`docker-compose -f dc-production.yml down -v`

**Creating Prod Setup**
`docker-compose -f dc-production.yml up -d --build`

### PRODUCTION SSL SETUP
**Deleting Production Setup**
`docker-compose -f dc-ssl-production.yml down -v`

**Creating Prod Setup**
`docker-compose -f dc-ssl-production.yml up -d --build`

### USEFUL DOCKER COMMANDS
**Execute Command in Docker Container**
`docker-compose exec <container_name> <command>`

**Deletes all Docker components unused presently (DON'T TRY IF NOT SURE)**
`docker system prune -a`

*NOTE: Volumes persist unless deleted explicitly with "docker-compose -f <yml filename> down -v" where -v flag is for deleting the volume.*

### Reference URLs
- https://docs.docker.com/compose/django/
- https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

*NOTE: This is a starter template for django (version 3.1.5)*
*NOTE: You must update the compose/ssl_production/nginx/domain_ssl_cert.pem file with the file generated for your domain. You can generate it from Cloudflare or any other provider.*
*NOTE: You must update the compose/ssl_production/nginx/domain_ssl_private_key.key file with the file generated for your domain. You can generate it from Cloudflare or any other provider.*

FIX-URGENT: Standardize default values and mention in README.md for easy replace all.

For the following environment variables, values must match.
```
POSTGRES_DB=product_name_db
POSTGRES_USER=product_name_db_user
POSTGRES_PASSWORD=product#name#db#user#password
```
AND
```
SQL_DATABASE=product_name_db
SQL_USER=product_name_db_user
SQL_PASSWORD=product#name#db#user#password
```

TODO-NORMAL: Improve documentation (README.md).
TODO-NORMAL: Improve documentation (comments/docstring).
TODO-NORMAL: Minimize HTML/CSS/JS. 
TODO-NORMAL: Use minified CSS/JS versions in sample pages.
TODO-CASUAL: Build website based documentation.