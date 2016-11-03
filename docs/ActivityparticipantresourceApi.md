# swagger_client.ActivityparticipantresourceApi

All URIs are relative to *https://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_activity_participant_using_post**](ActivityparticipantresourceApi.md#create_activity_participant_using_post) | **POST** /api/activity-participants | createActivityParticipant
[**delete_activity_participant_using_delete**](ActivityparticipantresourceApi.md#delete_activity_participant_using_delete) | **DELETE** /api/activity-participants/{id} | deleteActivityParticipant
[**get_activity_participant_using_get**](ActivityparticipantresourceApi.md#get_activity_participant_using_get) | **GET** /api/activity-participants/{id} | getActivityParticipant
[**get_all_activity_participants_using_get**](ActivityparticipantresourceApi.md#get_all_activity_participants_using_get) | **GET** /api/activity-participants | getAllActivityParticipants
[**search_activity_participants_using_get**](ActivityparticipantresourceApi.md#search_activity_participants_using_get) | **GET** /api/_search/activity-participants | searchActivityParticipants
[**update_activity_participant_using_put**](ActivityparticipantresourceApi.md#update_activity_participant_using_put) | **PUT** /api/activity-participants | updateActivityParticipant


# **create_activity_participant_using_post**
> ActivityParticipantDTO create_activity_participant_using_post(activity_participant_dto)

createActivityParticipant

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivityparticipantresourceApi()
activity_participant_dto = swagger_client.ActivityParticipantDTO() # ActivityParticipantDTO | activityParticipantDTO

try: 
    # createActivityParticipant
    api_response = api_instance.create_activity_participant_using_post(activity_participant_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityparticipantresourceApi->create_activity_participant_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_participant_dto** | [**ActivityParticipantDTO**](ActivityParticipantDTO.md)| activityParticipantDTO | 

### Return type

[**ActivityParticipantDTO**](ActivityParticipantDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_activity_participant_using_delete**
> delete_activity_participant_using_delete(id)

deleteActivityParticipant

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivityparticipantresourceApi()
id = 789 # int | id

try: 
    # deleteActivityParticipant
    api_instance.delete_activity_participant_using_delete(id)
except ApiException as e:
    print("Exception when calling ActivityparticipantresourceApi->delete_activity_participant_using_delete: %s\n" % e)
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

# **get_activity_participant_using_get**
> ActivityParticipantDTO get_activity_participant_using_get(id)

getActivityParticipant

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivityparticipantresourceApi()
id = 789 # int | id

try: 
    # getActivityParticipant
    api_response = api_instance.get_activity_participant_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityparticipantresourceApi->get_activity_participant_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**ActivityParticipantDTO**](ActivityParticipantDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_activity_participants_using_get**
> list[ActivityParticipantDTO] get_all_activity_participants_using_get()

getAllActivityParticipants

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivityparticipantresourceApi()

try: 
    # getAllActivityParticipants
    api_response = api_instance.get_all_activity_participants_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityparticipantresourceApi->get_all_activity_participants_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ActivityParticipantDTO]**](ActivityParticipantDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_activity_participants_using_get**
> list[ActivityParticipantDTO] search_activity_participants_using_get(query)

searchActivityParticipants

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivityparticipantresourceApi()
query = 'query_example' # str | query

try: 
    # searchActivityParticipants
    api_response = api_instance.search_activity_participants_using_get(query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityparticipantresourceApi->search_activity_participants_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| query | 

### Return type

[**list[ActivityParticipantDTO]**](ActivityParticipantDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_activity_participant_using_put**
> ActivityParticipantDTO update_activity_participant_using_put(activity_participant_dto)

updateActivityParticipant

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivityparticipantresourceApi()
activity_participant_dto = swagger_client.ActivityParticipantDTO() # ActivityParticipantDTO | activityParticipantDTO

try: 
    # updateActivityParticipant
    api_response = api_instance.update_activity_participant_using_put(activity_participant_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityparticipantresourceApi->update_activity_participant_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_participant_dto** | [**ActivityParticipantDTO**](ActivityParticipantDTO.md)| activityParticipantDTO | 

### Return type

[**ActivityParticipantDTO**](ActivityParticipantDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

