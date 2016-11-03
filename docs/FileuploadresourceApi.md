# swagger_client.FileuploadresourceApi

All URIs are relative to *https://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_attached_file_using_post**](FileuploadresourceApi.md#upload_attached_file_using_post) | **POST** /api/attachment/upload | uploadAttachedFile
[**upload_materials_using_post**](FileuploadresourceApi.md#upload_materials_using_post) | **POST** /api/materials/upload | uploadMaterials
[**upload_profile_image_using_post**](FileuploadresourceApi.md#upload_profile_image_using_post) | **POST** /api/profileimage/upload | uploadProfileImage


# **upload_attached_file_using_post**
> ResponseEntity upload_attached_file_using_post(attachment_type=attachment_type, request=request)

uploadAttachedFile

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileuploadresourceApi()
attachment_type = 'attachment_type_example' # str | attachmentType (optional)
request = swagger_client.MultipartHttpServletRequest() # MultipartHttpServletRequest | request (optional)

try: 
    # uploadAttachedFile
    api_response = api_instance.upload_attached_file_using_post(attachment_type=attachment_type, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileuploadresourceApi->upload_attached_file_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_type** | **str**| attachmentType | [optional] 
 **request** | [**MultipartHttpServletRequest**](MultipartHttpServletRequest.md)| request | [optional] 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_materials_using_post**
> ResponseEntity upload_materials_using_post(user_id, company_id, request=request)

uploadMaterials

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileuploadresourceApi()
user_id = 789 # int | userId
company_id = 789 # int | companyId
request = swagger_client.MultipartHttpServletRequest() # MultipartHttpServletRequest | request (optional)

try: 
    # uploadMaterials
    api_response = api_instance.upload_materials_using_post(user_id, company_id, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileuploadresourceApi->upload_materials_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 
 **company_id** | **int**| companyId | 
 **request** | [**MultipartHttpServletRequest**](MultipartHttpServletRequest.md)| request | [optional] 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_profile_image_using_post**
> ResponseEntity upload_profile_image_using_post(user_id, request=request)

uploadProfileImage

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileuploadresourceApi()
user_id = 789 # int | userId
request = swagger_client.MultipartHttpServletRequest() # MultipartHttpServletRequest | request (optional)

try: 
    # uploadProfileImage
    api_response = api_instance.upload_profile_image_using_post(user_id, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileuploadresourceApi->upload_profile_image_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 
 **request** | [**MultipartHttpServletRequest**](MultipartHttpServletRequest.md)| request | [optional] 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

