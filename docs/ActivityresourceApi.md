# swagger_client.ActivityresourceApi

All URIs are relative to *https://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_activity_using_post**](ActivityresourceApi.md#create_activity_using_post) | **POST** /api/activities | createActivity
[**delete_activity_using_delete**](ActivityresourceApi.md#delete_activity_using_delete) | **DELETE** /api/activities/{id} | deleteActivity
[**get_activity_using_get**](ActivityresourceApi.md#get_activity_using_get) | **GET** /api/activities/{id} | getActivity
[**get_all_activities_using_get**](ActivityresourceApi.md#get_all_activities_using_get) | **GET** /api/activities | getAllActivities
[**search_activities_using_get**](ActivityresourceApi.md#search_activities_using_get) | **GET** /api/_search/activities | searchActivities
[**update_activity_using_put**](ActivityresourceApi.md#update_activity_using_put) | **PUT** /api/activities | updateActivity


# **create_activity_using_post**
> ActivityDTO create_activity_using_post(activity_dto)

createActivity

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivityresourceApi()
activity_dto = swagger_client.ActivityDTO() # ActivityDTO | activityDTO

try: 
    # createActivity
    api_response = api_instance.create_activity_using_post(activity_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityresourceApi->create_activity_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_dto** | [**ActivityDTO**](ActivityDTO.md)| activityDTO | 

### Return type

[**ActivityDTO**](ActivityDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_activity_using_delete**
> delete_activity_using_delete(id)

deleteActivity

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivityresourceApi()
id = 789 # int | id

try: 
    # deleteActivity
    api_instance.delete_activity_using_delete(id)
except ApiException as e:
    print("Exception when calling ActivityresourceApi->delete_activity_using_delete: %s\n" % e)
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

# **get_activity_using_get**
> ActivityDTO get_activity_using_get(id)

getActivity

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivityresourceApi()
id = 789 # int | id

try: 
    # getActivity
    api_response = api_instance.get_activity_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityresourceApi->get_activity_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**ActivityDTO**](ActivityDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_activities_using_get**
> list[ActivityDTO] get_all_activities_using_get(user_id=user_id)

getAllActivities

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivityresourceApi()
user_id = 789 # int | userId (optional)

try: 
    # getAllActivities
    api_response = api_instance.get_all_activities_using_get(user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityresourceApi->get_all_activities_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | [optional] 

### Return type

[**list[ActivityDTO]**](ActivityDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_activities_using_get**
> list[ActivityDTO] search_activities_using_get(query)

searchActivities

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivityresourceApi()
query = 'query_example' # str | query

try: 
    # searchActivities
    api_response = api_instance.search_activities_using_get(query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityresourceApi->search_activities_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| query | 

### Return type

[**list[ActivityDTO]**](ActivityDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_activity_using_put**
> ActivityDTO update_activity_using_put(activity_dto)

updateActivity

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivityresourceApi()
activity_dto = swagger_client.ActivityDTO() # ActivityDTO | activityDTO

try: 
    # updateActivity
    api_response = api_instance.update_activity_using_put(activity_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityresourceApi->update_activity_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_dto** | [**ActivityDTO**](ActivityDTO.md)| activityDTO | 

### Return type

[**ActivityDTO**](ActivityDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

