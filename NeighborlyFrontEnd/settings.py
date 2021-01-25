#--------- Flask settings
SERVER_HOST = 'http://neighborly-frontend-01.azurewebsites.net' # Update this for the appropriate front-end website when up
SERVER_PORT = 8000
FLASK_DEBUG = True # Do not use debug mode in prod

# Flask-Restplus settings
SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_404_HELP = True
API_VERSION = 'v1'

#-------- Azure constants

# API_URL format: "https://[FUNCTION_APP_NAME_GOES_HERE].azurewebsites.net"
#API_URL = " https://neighborlyapi.azurewebsites.net/api/"

# for local host if Azure functions served locally
API_URL = "https://fa-neighborly-python-linux.azurewebsites.net/api"


# az webapp up --sku F1 -n neighborly-frontend-01 --resource-group rg-udacity-neighborly-project
# docker tag neighborly-functions-api registryudacityneighborly01.azurecr.io/neighborly-functions-api:v1
# docker push registryudacityneighborly01.azurecr.io/neighborly-functions-api:v1

# registryudacityneighborly01.azurecr.io


# kubectl delete deploy neighborly-cluster
# kubectl delete ScaledObject neighborly-cluster
# kubectl delete secret neighborly-cluster