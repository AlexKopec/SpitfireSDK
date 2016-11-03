# swagger_client.MaterialcategoryresourceApi

All URIs are relative to *https://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_material_category_using_post**](MaterialcategoryresourceApi.md#create_material_category_using_post) | **POST** /api/material-categories | createMaterialCategory
[**delete_material_category_using_delete**](MaterialcategoryresourceApi.md#delete_material_category_using_delete) | **DELETE** /api/material-categories/{id} | deleteMaterialCategory
[**get_all_material_categories_using_get**](MaterialcategoryresourceApi.md#get_all_material_categories_using_get) | **GET** /api/material-categories | getAllMaterialCategories
[**get_material_category_using_get**](MaterialcategoryresourceApi.md#get_material_category_using_get) | **GET** /api/material-categories/{id} | getMaterialCategory
[**update_material_category_using_put**](MaterialcategoryresourceApi.md#update_material_category_using_put) | **PUT** /api/material-categories | updateMaterialCategory


# **create_material_category_using_post**
> MaterialCategoryDTO create_material_category_using_post(material_category_dto)

createMaterialCategory

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialcategoryresourceApi()
material_category_dto = swagger_client.MaterialCategoryDTO() # MaterialCategoryDTO | materialCategoryDTO

try: 
    # createMaterialCategory
    api_response = api_instance.create_material_category_using_post(material_category_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaterialcategoryresourceApi->create_material_category_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **material_category_dto** | [**MaterialCategoryDTO**](MaterialCategoryDTO.md)| materialCategoryDTO | 

### Return type

[**MaterialCategoryDTO**](MaterialCategoryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_material_category_using_delete**
> delete_material_category_using_delete(id)

deleteMaterialCategory

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialcategoryresourceApi()
id = 789 # int | id

try: 
    # deleteMaterialCategory
    api_instance.delete_material_category_using_delete(id)
except ApiException as e:
    print("Exception when calling MaterialcategoryresourceApi->delete_material_category_using_delete: %s\n" % e)
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

# **get_all_material_categories_using_get**
> list[MaterialCategoryDTO] get_all_material_categories_using_get()

getAllMaterialCategories

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialcategoryresourceApi()

try: 
    # getAllMaterialCategories
    api_response = api_instance.get_all_material_categories_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaterialcategoryresourceApi->get_all_material_categories_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MaterialCategoryDTO]**](MaterialCategoryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_material_category_using_get**
> MaterialCategoryDTO get_material_category_using_get(id)

getMaterialCategory

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialcategoryresourceApi()
id = 789 # int | id

try: 
    # getMaterialCategory
    api_response = api_instance.get_material_category_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaterialcategoryresourceApi->get_material_category_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**MaterialCategoryDTO**](MaterialCategoryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_material_category_using_put**
> MaterialCategoryDTO update_material_category_using_put(material_category_dto)

updateMaterialCategory

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialcategoryresourceApi()
material_category_dto = swagger_client.MaterialCategoryDTO() # MaterialCategoryDTO | materialCategoryDTO

try: 
    # updateMaterialCategory
    api_response = api_instance.update_material_category_using_put(material_category_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaterialcategoryresourceApi->update_material_category_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **material_category_dto** | [**MaterialCategoryDTO**](MaterialCategoryDTO.md)| materialCategoryDTO | 

### Return type

[**MaterialCategoryDTO**](MaterialCategoryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

