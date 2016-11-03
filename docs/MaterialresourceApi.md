# swagger_client.MaterialresourceApi

All URIs are relative to *https://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_material_using_post**](MaterialresourceApi.md#create_material_using_post) | **POST** /api/materials | createMaterial
[**delete_material_using_delete**](MaterialresourceApi.md#delete_material_using_delete) | **DELETE** /api/materials/{id} | deleteMaterial
[**get_all_materials_using_get**](MaterialresourceApi.md#get_all_materials_using_get) | **GET** /api/materials | getAllMaterials
[**get_material_using_get**](MaterialresourceApi.md#get_material_using_get) | **GET** /api/materials/{id} | getMaterial
[**search_materials_using_get**](MaterialresourceApi.md#search_materials_using_get) | **GET** /api/_search/materials | searchMaterials
[**update_material_using_put**](MaterialresourceApi.md#update_material_using_put) | **PUT** /api/materials | updateMaterial


# **create_material_using_post**
> MaterialDTO create_material_using_post(material_dto)

createMaterial

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialresourceApi()
material_dto = swagger_client.MaterialDTO() # MaterialDTO | materialDTO

try: 
    # createMaterial
    api_response = api_instance.create_material_using_post(material_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaterialresourceApi->create_material_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **material_dto** | [**MaterialDTO**](MaterialDTO.md)| materialDTO | 

### Return type

[**MaterialDTO**](MaterialDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_material_using_delete**
> delete_material_using_delete(id)

deleteMaterial

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialresourceApi()
id = 789 # int | id

try: 
    # deleteMaterial
    api_instance.delete_material_using_delete(id)
except ApiException as e:
    print("Exception when calling MaterialresourceApi->delete_material_using_delete: %s\n" % e)
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

# **get_all_materials_using_get**
> list[MaterialDTO] get_all_materials_using_get()

getAllMaterials

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialresourceApi()

try: 
    # getAllMaterials
    api_response = api_instance.get_all_materials_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaterialresourceApi->get_all_materials_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MaterialDTO]**](MaterialDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_material_using_get**
> MaterialDTO get_material_using_get(id)

getMaterial

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialresourceApi()
id = 789 # int | id

try: 
    # getMaterial
    api_response = api_instance.get_material_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaterialresourceApi->get_material_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**MaterialDTO**](MaterialDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_materials_using_get**
> list[MaterialDTO] search_materials_using_get(query)

searchMaterials

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialresourceApi()
query = 'query_example' # str | query

try: 
    # searchMaterials
    api_response = api_instance.search_materials_using_get(query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaterialresourceApi->search_materials_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| query | 

### Return type

[**list[MaterialDTO]**](MaterialDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_material_using_put**
> MaterialDTO update_material_using_put(material_dto)

updateMaterial

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialresourceApi()
material_dto = swagger_client.MaterialDTO() # MaterialDTO | materialDTO

try: 
    # updateMaterial
    api_response = api_instance.update_material_using_put(material_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaterialresourceApi->update_material_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **material_dto** | [**MaterialDTO**](MaterialDTO.md)| materialDTO | 

### Return type

[**MaterialDTO**](MaterialDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

