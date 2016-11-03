# swagger_client.QuantitytyperesourceApi

All URIs are relative to *https://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_quantity_type_using_post**](QuantitytyperesourceApi.md#create_quantity_type_using_post) | **POST** /api/quantity-types | createQuantityType
[**delete_quantity_type_using_delete**](QuantitytyperesourceApi.md#delete_quantity_type_using_delete) | **DELETE** /api/quantity-types/{id} | deleteQuantityType
[**get_all_quantity_types_using_get**](QuantitytyperesourceApi.md#get_all_quantity_types_using_get) | **GET** /api/quantity-types | getAllQuantityTypes
[**get_quantity_type_using_get**](QuantitytyperesourceApi.md#get_quantity_type_using_get) | **GET** /api/quantity-types/{id} | getQuantityType
[**update_quantity_type_using_put**](QuantitytyperesourceApi.md#update_quantity_type_using_put) | **PUT** /api/quantity-types | updateQuantityType


# **create_quantity_type_using_post**
> QuantityTypeDTO create_quantity_type_using_post(quantity_type_dto)

createQuantityType

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuantitytyperesourceApi()
quantity_type_dto = swagger_client.QuantityTypeDTO() # QuantityTypeDTO | quantityTypeDTO

try: 
    # createQuantityType
    api_response = api_instance.create_quantity_type_using_post(quantity_type_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuantitytyperesourceApi->create_quantity_type_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quantity_type_dto** | [**QuantityTypeDTO**](QuantityTypeDTO.md)| quantityTypeDTO | 

### Return type

[**QuantityTypeDTO**](QuantityTypeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_quantity_type_using_delete**
> delete_quantity_type_using_delete(id)

deleteQuantityType

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuantitytyperesourceApi()
id = 789 # int | id

try: 
    # deleteQuantityType
    api_instance.delete_quantity_type_using_delete(id)
except ApiException as e:
    print("Exception when calling QuantitytyperesourceApi->delete_quantity_type_using_delete: %s\n" % e)
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

# **get_all_quantity_types_using_get**
> list[QuantityTypeDTO] get_all_quantity_types_using_get()

getAllQuantityTypes

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuantitytyperesourceApi()

try: 
    # getAllQuantityTypes
    api_response = api_instance.get_all_quantity_types_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuantitytyperesourceApi->get_all_quantity_types_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[QuantityTypeDTO]**](QuantityTypeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quantity_type_using_get**
> QuantityTypeDTO get_quantity_type_using_get(id)

getQuantityType

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuantitytyperesourceApi()
id = 789 # int | id

try: 
    # getQuantityType
    api_response = api_instance.get_quantity_type_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuantitytyperesourceApi->get_quantity_type_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**QuantityTypeDTO**](QuantityTypeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_quantity_type_using_put**
> QuantityTypeDTO update_quantity_type_using_put(quantity_type_dto)

updateQuantityType

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuantitytyperesourceApi()
quantity_type_dto = swagger_client.QuantityTypeDTO() # QuantityTypeDTO | quantityTypeDTO

try: 
    # updateQuantityType
    api_response = api_instance.update_quantity_type_using_put(quantity_type_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuantitytyperesourceApi->update_quantity_type_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quantity_type_dto** | [**QuantityTypeDTO**](QuantityTypeDTO.md)| quantityTypeDTO | 

### Return type

[**QuantityTypeDTO**](QuantityTypeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

