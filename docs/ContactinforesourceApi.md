# swagger_client.ContactinforesourceApi

All URIs are relative to *https://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contact_info_using_post**](ContactinforesourceApi.md#create_contact_info_using_post) | **POST** /api/contact-infos | createContactInfo
[**delete_contact_info_using_delete**](ContactinforesourceApi.md#delete_contact_info_using_delete) | **DELETE** /api/contact-infos/{id} | deleteContactInfo
[**get_all_contact_infos_using_get**](ContactinforesourceApi.md#get_all_contact_infos_using_get) | **GET** /api/contact-infos | getAllContactInfos
[**get_contact_info_using_get**](ContactinforesourceApi.md#get_contact_info_using_get) | **GET** /api/contact-infos/{id} | getContactInfo
[**update_contact_info_using_put**](ContactinforesourceApi.md#update_contact_info_using_put) | **PUT** /api/contact-infos | updateContactInfo


# **create_contact_info_using_post**
> ContactInfoDTO create_contact_info_using_post(contact_info_dto)

createContactInfo

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactinforesourceApi()
contact_info_dto = swagger_client.ContactInfoDTO() # ContactInfoDTO | contactInfoDTO

try: 
    # createContactInfo
    api_response = api_instance.create_contact_info_using_post(contact_info_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactinforesourceApi->create_contact_info_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_info_dto** | [**ContactInfoDTO**](ContactInfoDTO.md)| contactInfoDTO | 

### Return type

[**ContactInfoDTO**](ContactInfoDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_info_using_delete**
> delete_contact_info_using_delete(id)

deleteContactInfo

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactinforesourceApi()
id = 789 # int | id

try: 
    # deleteContactInfo
    api_instance.delete_contact_info_using_delete(id)
except ApiException as e:
    print("Exception when calling ContactinforesourceApi->delete_contact_info_using_delete: %s\n" % e)
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

# **get_all_contact_infos_using_get**
> list[ContactInfoDTO] get_all_contact_infos_using_get()

getAllContactInfos

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactinforesourceApi()

try: 
    # getAllContactInfos
    api_response = api_instance.get_all_contact_infos_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactinforesourceApi->get_all_contact_infos_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ContactInfoDTO]**](ContactInfoDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_info_using_get**
> ContactInfoDTO get_contact_info_using_get(id)

getContactInfo

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactinforesourceApi()
id = 789 # int | id

try: 
    # getContactInfo
    api_response = api_instance.get_contact_info_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactinforesourceApi->get_contact_info_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**ContactInfoDTO**](ContactInfoDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact_info_using_put**
> ContactInfoDTO update_contact_info_using_put(contact_info_dto)

updateContactInfo

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactinforesourceApi()
contact_info_dto = swagger_client.ContactInfoDTO() # ContactInfoDTO | contactInfoDTO

try: 
    # updateContactInfo
    api_response = api_instance.update_contact_info_using_put(contact_info_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactinforesourceApi->update_contact_info_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_info_dto** | [**ContactInfoDTO**](ContactInfoDTO.md)| contactInfoDTO | 

### Return type

[**ContactInfoDTO**](ContactInfoDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

