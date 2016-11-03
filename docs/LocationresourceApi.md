# swagger_client.LocationresourceApi

All URIs are relative to *https://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_location_using_post**](LocationresourceApi.md#create_location_using_post) | **POST** /api/locations | createLocation
[**delete_location_using_delete**](LocationresourceApi.md#delete_location_using_delete) | **DELETE** /api/locations/{id} | deleteLocation
[**get_all_locations_using_get**](LocationresourceApi.md#get_all_locations_using_get) | **GET** /api/locations | getAllLocations
[**get_location_using_get**](LocationresourceApi.md#get_location_using_get) | **GET** /api/locations/{id} | getLocation
[**update_location_using_put**](LocationresourceApi.md#update_location_using_put) | **PUT** /api/locations | updateLocation


# **create_location_using_post**
> LocationDTO create_location_using_post(location_dto)

createLocation

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocationresourceApi()
location_dto = swagger_client.LocationDTO() # LocationDTO | locationDTO

try: 
    # createLocation
    api_response = api_instance.create_location_using_post(location_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationresourceApi->create_location_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_dto** | [**LocationDTO**](LocationDTO.md)| locationDTO | 

### Return type

[**LocationDTO**](LocationDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_location_using_delete**
> delete_location_using_delete(id)

deleteLocation

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocationresourceApi()
id = 789 # int | id

try: 
    # deleteLocation
    api_instance.delete_location_using_delete(id)
except ApiException as e:
    print("Exception when calling LocationresourceApi->delete_location_using_delete: %s\n" % e)
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

# **get_all_locations_using_get**
> list[LocationDTO] get_all_locations_using_get()

getAllLocations

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocationresourceApi()

try: 
    # getAllLocations
    api_response = api_instance.get_all_locations_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationresourceApi->get_all_locations_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LocationDTO]**](LocationDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location_using_get**
> LocationDTO get_location_using_get(id)

getLocation

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocationresourceApi()
id = 789 # int | id

try: 
    # getLocation
    api_response = api_instance.get_location_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationresourceApi->get_location_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**LocationDTO**](LocationDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_location_using_put**
> LocationDTO update_location_using_put(location_dto)

updateLocation

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocationresourceApi()
location_dto = swagger_client.LocationDTO() # LocationDTO | locationDTO

try: 
    # updateLocation
    api_response = api_instance.update_location_using_put(location_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationresourceApi->update_location_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_dto** | [**LocationDTO**](LocationDTO.md)| locationDTO | 

### Return type

[**LocationDTO**](LocationDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

