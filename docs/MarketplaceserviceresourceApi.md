# swagger_client.MarketplaceserviceresourceApi

All URIs are relative to *https://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_marketplace_service_using_post**](MarketplaceserviceresourceApi.md#create_marketplace_service_using_post) | **POST** /api/marketplace-services | createMarketplaceService
[**delete_marketplace_service_using_delete**](MarketplaceserviceresourceApi.md#delete_marketplace_service_using_delete) | **DELETE** /api/marketplace-services/{id} | deleteMarketplaceService
[**get_all_marketplace_services_using_get**](MarketplaceserviceresourceApi.md#get_all_marketplace_services_using_get) | **GET** /api/marketplace-services | getAllMarketplaceServices
[**get_marketplace_service_using_get**](MarketplaceserviceresourceApi.md#get_marketplace_service_using_get) | **GET** /api/marketplace-services/{id} | getMarketplaceService
[**update_marketplace_service_using_put**](MarketplaceserviceresourceApi.md#update_marketplace_service_using_put) | **PUT** /api/marketplace-services | updateMarketplaceService


# **create_marketplace_service_using_post**
> MarketplaceServiceDTO create_marketplace_service_using_post(marketplace_service_dto)

createMarketplaceService

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketplaceserviceresourceApi()
marketplace_service_dto = swagger_client.MarketplaceServiceDTO() # MarketplaceServiceDTO | marketplaceServiceDTO

try: 
    # createMarketplaceService
    api_response = api_instance.create_marketplace_service_using_post(marketplace_service_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceserviceresourceApi->create_marketplace_service_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_service_dto** | [**MarketplaceServiceDTO**](MarketplaceServiceDTO.md)| marketplaceServiceDTO | 

### Return type

[**MarketplaceServiceDTO**](MarketplaceServiceDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_marketplace_service_using_delete**
> delete_marketplace_service_using_delete(id)

deleteMarketplaceService

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketplaceserviceresourceApi()
id = 789 # int | id

try: 
    # deleteMarketplaceService
    api_instance.delete_marketplace_service_using_delete(id)
except ApiException as e:
    print("Exception when calling MarketplaceserviceresourceApi->delete_marketplace_service_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_marketplace_services_using_get**
> list[MarketplaceServiceDTO] get_all_marketplace_services_using_get()

getAllMarketplaceServices

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketplaceserviceresourceApi()

try: 
    # getAllMarketplaceServices
    api_response = api_instance.get_all_marketplace_services_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceserviceresourceApi->get_all_marketplace_services_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MarketplaceServiceDTO]**](MarketplaceServiceDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketplace_service_using_get**
> MarketplaceServiceDTO get_marketplace_service_using_get(id)

getMarketplaceService

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketplaceserviceresourceApi()
id = 789 # int | id

try: 
    # getMarketplaceService
    api_response = api_instance.get_marketplace_service_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceserviceresourceApi->get_marketplace_service_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**MarketplaceServiceDTO**](MarketplaceServiceDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_marketplace_service_using_put**
> MarketplaceServiceDTO update_marketplace_service_using_put(marketplace_service_dto)

updateMarketplaceService

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketplaceserviceresourceApi()
marketplace_service_dto = swagger_client.MarketplaceServiceDTO() # MarketplaceServiceDTO | marketplaceServiceDTO

try: 
    # updateMarketplaceService
    api_response = api_instance.update_marketplace_service_using_put(marketplace_service_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceserviceresourceApi->update_marketplace_service_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_service_dto** | [**MarketplaceServiceDTO**](MarketplaceServiceDTO.md)| marketplaceServiceDTO | 

### Return type

[**MarketplaceServiceDTO**](MarketplaceServiceDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

