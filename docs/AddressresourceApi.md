# swagger_client.AddressresourceApi

All URIs are relative to *https://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_address_using_post**](AddressresourceApi.md#create_address_using_post) | **POST** /api/addresses | createAddress
[**delete_address_using_delete**](AddressresourceApi.md#delete_address_using_delete) | **DELETE** /api/addresses/{id} | deleteAddress
[**get_address_using_get**](AddressresourceApi.md#get_address_using_get) | **GET** /api/addresses/{id} | getAddress
[**get_all_addresses_using_get**](AddressresourceApi.md#get_all_addresses_using_get) | **GET** /api/addresses | getAllAddresses
[**update_address_using_put**](AddressresourceApi.md#update_address_using_put) | **PUT** /api/addresses | updateAddress


# **create_address_using_post**
> AddressDTO create_address_using_post(address_dto)

createAddress

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddressresourceApi()
address_dto = swagger_client.AddressDTO() # AddressDTO | addressDTO

try: 
    # createAddress
    api_response = api_instance.create_address_using_post(address_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressresourceApi->create_address_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_dto** | [**AddressDTO**](AddressDTO.md)| addressDTO | 

### Return type

[**AddressDTO**](AddressDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_address_using_delete**
> delete_address_using_delete(id)

deleteAddress

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddressresourceApi()
id = 789 # int | id

try: 
    # deleteAddress
    api_instance.delete_address_using_delete(id)
except ApiException as e:
    print("Exception when calling AddressresourceApi->delete_address_using_delete: %s\n" % e)
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

# **get_address_using_get**
> AddressDTO get_address_using_get(id)

getAddress

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddressresourceApi()
id = 789 # int | id

try: 
    # getAddress
    api_response = api_instance.get_address_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressresourceApi->get_address_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**AddressDTO**](AddressDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_addresses_using_get**
> list[AddressDTO] get_all_addresses_using_get()

getAllAddresses

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddressresourceApi()

try: 
    # getAllAddresses
    api_response = api_instance.get_all_addresses_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressresourceApi->get_all_addresses_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AddressDTO]**](AddressDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_address_using_put**
> AddressDTO update_address_using_put(address_dto)

updateAddress

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddressresourceApi()
address_dto = swagger_client.AddressDTO() # AddressDTO | addressDTO

try: 
    # updateAddress
    api_response = api_instance.update_address_using_put(address_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressresourceApi->update_address_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_dto** | [**AddressDTO**](AddressDTO.md)| addressDTO | 

### Return type

[**AddressDTO**](AddressDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

