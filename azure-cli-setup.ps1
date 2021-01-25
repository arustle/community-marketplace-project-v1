az functionapp create \
--resource-group <your-resource-group> \
--plan <your-plan-name> \
--name <your-app-name> \
--storage-account <your-storage-account> \
--os-type Linux \
--consumption-plan-location <your-region> \
--runtime python

az functionapp create `
--resource-group rg-udacity-neighborly-project `
--name fa-neighborly-py-01 `
--storage-account "storage-udacity-neighborly-project" `
--os-type Linux `
--consumption-plan-location "eastus" `
--runtime python `
--functions-version 3