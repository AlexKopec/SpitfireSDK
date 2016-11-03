# swagger_client.MarketplaceuserresourceApi

All URIs are relative to *https://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_marketplace_user_using_post**](MarketplaceuserresourceApi.md#create_marketplace_user_using_post) | **POST** /api/marketplace-users | createMarketplaceUser
[**delete_marketplace_user_using_delete**](MarketplaceuserresourceApi.md#delete_marketplace_user_using_delete) | **DELETE** /api/marketplace-users/{id} | deleteMarketplaceUser
[**get_all_marketplace_users_using_get**](MarketplaceuserresourceApi.md#get_all_marketplace_users_using_get) | **GET** /api/marketplace-users | getAllMarketplaceUsers
[**get_marketplace_user_using_get**](MarketplaceuserresourceApi.md#get_marketplace_user_using_get) | **GET** /api/marketplace-users/{id} | getMarketplaceUser
[**update_marketplace_user_using_put**](MarketplaceuserresourceApi.md#update_marketplace_user_using_put) | **PUT** /api/marketplace-users | updateMarketplaceUser


# **create_marketplace_user_using_post**
> MarketplaceUserDTO create_marketplace_user_using_post(marketplace_user_dto)

createMarketplaceUser

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketplaceuserresourceApi()
marketplace_user_dto = swagger_client.MarketplaceUserDTO() # MarketplaceUserDTO | marketplaceUserDTO

try: 
    # createMarketplaceUser
    api_response = api_instance.create_marketplace_user_using_post(marketplace_user_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceuserresourceApi->create_marketplace_user_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_user_dto** | [**MarketplaceUserDTO**](MarketplaceUserDTO.md)| marketplaceUserDTO | 

### Return type

[**MarketplaceUserDTO**](MarketplaceUserDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_marketplace_user_using_delete**
> delete_marketplace_user_using_delete(id)

deleteMarketplaceUser

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketplaceuserresourceApi()
id = 789 # int | id

try: 
    # deleteMarketplaceUser
    api_instance.delete_marketplace_user_using_delete(id)
except ApiException as e:
    print("Exception when calling MarketplaceuserresourceApi->delete_marketplace_user_using_delete: %s\n" % e)
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

# **get_all_marketplace_users_using_get**
> list[MarketplaceUserDTO] get_all_marketplace_users_using_get()

getAllMarketplaceUsers

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketplaceuserresourceApi()

try: 
    # getAllMarketplaceUsers
    api_response = api_instance.get_all_marketplace_users_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceuserresourceApi->get_all_marketplace_users_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MarketplaceUserDTO]**](MarketplaceUserDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketplace_user_using_get**
> MarketplaceUserDTO get_marketplace_user_using_get(id)

getMarketplaceUser

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketplaceuserresourceApi()
id = 789 # int | id

try: 
    # getMarketplaceUser
    api_response = api_instance.get_marketplace_user_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceuserresourceApi->get_marketplace_user_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**MarketplaceUserDTO**](MarketplaceUserDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_marketplace_user_using_put**
> MarketplaceUserDTO update_marketplace_user_using_put(marketplace_user_dto)

updateMarketplaceUser

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketplaceuserresourceApi()
marketplace_user_dto = swagger_client.MarketplaceUserDTO() # MarketplaceUserDTO | marketplaceUserDTO

try: 
    # updateMarketplaceUser
    api_response = api_instance.update_marketplace_user_using_put(marketplace_user_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceuserresourceApi->update_marketplace_user_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_user_dto** | [**MarketplaceUserDTO**](MarketplaceUserDTO.md)| marketplaceUserDTO | 

### Return type

[**MarketplaceUserDTO**](MarketplaceUserDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

