# swagger_client.MaterialattachmentresourceApi

All URIs are relative to *https://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_material_attachment_using_post**](MaterialattachmentresourceApi.md#create_material_attachment_using_post) | **POST** /api/material-attachments | createMaterialAttachment
[**delete_material_attachment_using_delete**](MaterialattachmentresourceApi.md#delete_material_attachment_using_delete) | **DELETE** /api/material-attachments/{id} | deleteMaterialAttachment
[**get_all_material_attachments_using_get**](MaterialattachmentresourceApi.md#get_all_material_attachments_using_get) | **GET** /api/material-attachments | getAllMaterialAttachments
[**get_material_attachment_using_get**](MaterialattachmentresourceApi.md#get_material_attachment_using_get) | **GET** /api/material-attachments/{id} | getMaterialAttachment
[**search_material_attachments_using_get**](MaterialattachmentresourceApi.md#search_material_attachments_using_get) | **GET** /api/_search/material-attachments | searchMaterialAttachments
[**update_material_attachment_using_put**](MaterialattachmentresourceApi.md#update_material_attachment_using_put) | **PUT** /api/material-attachments | updateMaterialAttachment


# **create_material_attachment_using_post**
> MaterialAttachmentDTO create_material_attachment_using_post(material_attachment_dto)

createMaterialAttachment

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialattachmentresourceApi()
material_attachment_dto = swagger_client.MaterialAttachmentDTO() # MaterialAttachmentDTO | materialAttachmentDTO

try: 
    # createMaterialAttachment
    api_response = api_instance.create_material_attachment_using_post(material_attachment_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaterialattachmentresourceApi->create_material_attachment_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **material_attachment_dto** | [**MaterialAttachmentDTO**](MaterialAttachmentDTO.md)| materialAttachmentDTO | 

### Return type

[**MaterialAttachmentDTO**](MaterialAttachmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_material_attachment_using_delete**
> delete_material_attachment_using_delete(id)

deleteMaterialAttachment

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialattachmentresourceApi()
id = 789 # int | id

try: 
    # deleteMaterialAttachment
    api_instance.delete_material_attachment_using_delete(id)
except ApiException as e:
    print("Exception when calling MaterialattachmentresourceApi->delete_material_attachment_using_delete: %s\n" % e)
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

# **get_all_material_attachments_using_get**
> list[MaterialAttachmentDTO] get_all_material_attachments_using_get()

getAllMaterialAttachments

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialattachmentresourceApi()

try: 
    # getAllMaterialAttachments
    api_response = api_instance.get_all_material_attachments_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaterialattachmentresourceApi->get_all_material_attachments_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MaterialAttachmentDTO]**](MaterialAttachmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_material_attachment_using_get**
> MaterialAttachmentDTO get_material_attachment_using_get(id)

getMaterialAttachment

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialattachmentresourceApi()
id = 789 # int | id

try: 
    # getMaterialAttachment
    api_response = api_instance.get_material_attachment_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaterialattachmentresourceApi->get_material_attachment_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**MaterialAttachmentDTO**](MaterialAttachmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_material_attachments_using_get**
> list[MaterialAttachmentDTO] search_material_attachments_using_get(query)

searchMaterialAttachments

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialattachmentresourceApi()
query = 'query_example' # str | query

try: 
    # searchMaterialAttachments
    api_response = api_instance.search_material_attachments_using_get(query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaterialattachmentresourceApi->search_material_attachments_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| query | 

### Return type

[**list[MaterialAttachmentDTO]**](MaterialAttachmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_material_attachment_using_put**
> MaterialAttachmentDTO update_material_attachment_using_put(material_attachment_dto)

updateMaterialAttachment

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialattachmentresourceApi()
material_attachment_dto = swagger_client.MaterialAttachmentDTO() # MaterialAttachmentDTO | materialAttachmentDTO

try: 
    # updateMaterialAttachment
    api_response = api_instance.update_material_attachment_using_put(material_attachment_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaterialattachmentresourceApi->update_material_attachment_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **material_attachment_dto** | [**MaterialAttachmentDTO**](MaterialAttachmentDTO.md)| materialAttachmentDTO | 

### Return type

[**MaterialAttachmentDTO**](MaterialAttachmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

