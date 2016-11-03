# swagger_client.MaterialsubcategoryresourceApi

All URIs are relative to *https://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_material_subcategory_using_post**](MaterialsubcategoryresourceApi.md#create_material_subcategory_using_post) | **POST** /api/material-subcategories | createMaterialSubcategory
[**delete_material_subcategory_using_delete**](MaterialsubcategoryresourceApi.md#delete_material_subcategory_using_delete) | **DELETE** /api/material-subcategories/{id} | deleteMaterialSubcategory
[**get_all_material_subcategories_using_get**](MaterialsubcategoryresourceApi.md#get_all_material_subcategories_using_get) | **GET** /api/material-subcategories | getAllMaterialSubcategories
[**get_material_subcategory_using_get**](MaterialsubcategoryresourceApi.md#get_material_subcategory_using_get) | **GET** /api/material-subcategories/{id} | getMaterialSubcategory
[**update_material_subcategory_using_put**](MaterialsubcategoryresourceApi.md#update_material_subcategory_using_put) | **PUT** /api/material-subcategories | updateMaterialSubcategory


# **create_material_subcategory_using_post**
> MaterialSubcategoryDTO create_material_subcategory_using_post(material_subcategory_dto)

createMaterialSubcategory

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialsubcategoryresourceApi()
material_subcategory_dto = swagger_client.MaterialSubcategoryDTO() # MaterialSubcategoryDTO | materialSubcategoryDTO

try: 
    # createMaterialSubcategory
    api_response = api_instance.create_material_subcategory_using_post(material_subcategory_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaterialsubcategoryresourceApi->create_material_subcategory_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **material_subcategory_dto** | [**MaterialSubcategoryDTO**](MaterialSubcategoryDTO.md)| materialSubcategoryDTO | 

### Return type

[**MaterialSubcategoryDTO**](MaterialSubcategoryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_material_subcategory_using_delete**
> delete_material_subcategory_using_delete(id)

deleteMaterialSubcategory

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialsubcategoryresourceApi()
id = 789 # int | id

try: 
    # deleteMaterialSubcategory
    api_instance.delete_material_subcategory_using_delete(id)
except ApiException as e:
    print("Exception when calling MaterialsubcategoryresourceApi->delete_material_subcategory_using_delete: %s\n" % e)
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

# **get_all_material_subcategories_using_get**
> list[MaterialSubcategoryDTO] get_all_material_subcategories_using_get()

getAllMaterialSubcategories

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialsubcategoryresourceApi()

try: 
    # getAllMaterialSubcategories
    api_response = api_instance.get_all_material_subcategories_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaterialsubcategoryresourceApi->get_all_material_subcategories_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MaterialSubcategoryDTO]**](MaterialSubcategoryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_material_subcategory_using_get**
> MaterialSubcategoryDTO get_material_subcategory_using_get(id)

getMaterialSubcategory

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialsubcategoryresourceApi()
id = 789 # int | id

try: 
    # getMaterialSubcategory
    api_response = api_instance.get_material_subcategory_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaterialsubcategoryresourceApi->get_material_subcategory_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**MaterialSubcategoryDTO**](MaterialSubcategoryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_material_subcategory_using_put**
> MaterialSubcategoryDTO update_material_subcategory_using_put(material_subcategory_dto)

updateMaterialSubcategory

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialsubcategoryresourceApi()
material_subcategory_dto = swagger_client.MaterialSubcategoryDTO() # MaterialSubcategoryDTO | materialSubcategoryDTO

try: 
    # updateMaterialSubcategory
    api_response = api_instance.update_material_subcategory_using_put(material_subcategory_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaterialsubcategoryresourceApi->update_material_subcategory_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **material_subcategory_dto** | [**MaterialSubcategoryDTO**](MaterialSubcategoryDTO.md)| materialSubcategoryDTO | 

### Return type

[**MaterialSubcategoryDTO**](MaterialSubcategoryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

