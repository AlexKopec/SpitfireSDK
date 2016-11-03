# swagger_client.ActivitymessageresourceApi

All URIs are relative to *https://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_activity_message_using_post**](ActivitymessageresourceApi.md#create_activity_message_using_post) | **POST** /api/activity-messages | createActivityMessage
[**delete_activity_message_using_delete**](ActivitymessageresourceApi.md#delete_activity_message_using_delete) | **DELETE** /api/activity-messages/{id} | deleteActivityMessage
[**get_activity_message_using_get**](ActivitymessageresourceApi.md#get_activity_message_using_get) | **GET** /api/activity-messages/{id} | getActivityMessage
[**get_all_activity_messages_using_get**](ActivitymessageresourceApi.md#get_all_activity_messages_using_get) | **GET** /api/activity-messages | getAllActivityMessages
[**search_activity_messages_using_get**](ActivitymessageresourceApi.md#search_activity_messages_using_get) | **GET** /api/_search/activity-messages | searchActivityMessages
[**update_activity_message_using_put**](ActivitymessageresourceApi.md#update_activity_message_using_put) | **PUT** /api/activity-messages | updateActivityMessage


# **create_activity_message_using_post**
> ActivityMessageDTO create_activity_message_using_post(activity_message_dto)

createActivityMessage

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivitymessageresourceApi()
activity_message_dto = swagger_client.ActivityMessageDTO() # ActivityMessageDTO | activityMessageDTO

try: 
    # createActivityMessage
    api_response = api_instance.create_activity_message_using_post(activity_message_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitymessageresourceApi->create_activity_message_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_message_dto** | [**ActivityMessageDTO**](ActivityMessageDTO.md)| activityMessageDTO | 

### Return type

[**ActivityMessageDTO**](ActivityMessageDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_activity_message_using_delete**
> delete_activity_message_using_delete(id)

deleteActivityMessage

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivitymessageresourceApi()
id = 789 # int | id

try: 
    # deleteActivityMessage
    api_instance.delete_activity_message_using_delete(id)
except ApiException as e:
    print("Exception when calling ActivitymessageresourceApi->delete_activity_message_using_delete: %s\n" % e)
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

# **get_activity_message_using_get**
> ActivityMessageDTO get_activity_message_using_get(id)

getActivityMessage

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivitymessageresourceApi()
id = 789 # int | id

try: 
    # getActivityMessage
    api_response = api_instance.get_activity_message_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitymessageresourceApi->get_activity_message_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**ActivityMessageDTO**](ActivityMessageDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_activity_messages_using_get**
> list[ActivityMessageDTO] get_all_activity_messages_using_get()

getAllActivityMessages

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivitymessageresourceApi()

try: 
    # getAllActivityMessages
    api_response = api_instance.get_all_activity_messages_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitymessageresourceApi->get_all_activity_messages_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ActivityMessageDTO]**](ActivityMessageDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_activity_messages_using_get**
> list[ActivityMessageDTO] search_activity_messages_using_get(query)

searchActivityMessages

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivitymessageresourceApi()
query = 'query_example' # str | query

try: 
    # searchActivityMessages
    api_response = api_instance.search_activity_messages_using_get(query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitymessageresourceApi->search_activity_messages_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| query | 

### Return type

[**list[ActivityMessageDTO]**](ActivityMessageDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_activity_message_using_put**
> ActivityMessageDTO update_activity_message_using_put(activity_message_dto)

updateActivityMessage

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivitymessageresourceApi()
activity_message_dto = swagger_client.ActivityMessageDTO() # ActivityMessageDTO | activityMessageDTO

try: 
    # updateActivityMessage
    api_response = api_instance.update_activity_message_using_put(activity_message_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitymessageresourceApi->update_activity_message_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_message_dto** | [**ActivityMessageDTO**](ActivityMessageDTO.md)| activityMessageDTO | 

### Return type

[**ActivityMessageDTO**](ActivityMessageDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

