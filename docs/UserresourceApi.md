# swagger_client.UserresourceApi

All URIs are relative to *https://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_using_post**](UserresourceApi.md#create_user_using_post) | **POST** /api/users | createUser
[**delete_user_using_delete**](UserresourceApi.md#delete_user_using_delete) | **DELETE** /api/users/{login} | deleteUser
[**get_all_users_using_get**](UserresourceApi.md#get_all_users_using_get) | **GET** /api/users | getAllUsers
[**get_user_using_get**](UserresourceApi.md#get_user_using_get) | **GET** /api/users/{login} | getUser
[**search_using_get**](UserresourceApi.md#search_using_get) | **GET** /api/_search/users/{query} | search
[**update_user_using_put**](UserresourceApi.md#update_user_using_put) | **PUT** /api/users | updateUser


# **create_user_using_post**
> object create_user_using_post(managed_user_dto)

createUser

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserresourceApi()
managed_user_dto = swagger_client.ManagedUserDTO() # ManagedUserDTO | managedUserDTO

try: 
    # createUser
    api_response = api_instance.create_user_using_post(managed_user_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserresourceApi->create_user_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed_user_dto** | [**ManagedUserDTO**](ManagedUserDTO.md)| managedUserDTO | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_using_delete**
> delete_user_using_delete(login)

deleteUser

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserresourceApi()
login = 'login_example' # str | login

try: 
    # deleteUser
    api_instance.delete_user_using_delete(login)
except ApiException as e:
    print("Exception when calling UserresourceApi->delete_user_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**| login | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_users_using_get**
> list[ManagedUserDTO] get_all_users_using_get()

getAllUsers

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserresourceApi()

try: 
    # getAllUsers
    api_response = api_instance.get_all_users_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserresourceApi->get_all_users_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ManagedUserDTO]**](ManagedUserDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_using_get**
> ManagedUserDTO get_user_using_get(login)

getUser

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserresourceApi()
login = 'login_example' # str | login

try: 
    # getUser
    api_response = api_instance.get_user_using_get(login)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserresourceApi->get_user_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**| login | 

### Return type

[**ManagedUserDTO**](ManagedUserDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_using_get**
> list[User] search_using_get(query)

search

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserresourceApi()
query = 'query_example' # str | query

try: 
    # search
    api_response = api_instance.search_using_get(query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserresourceApi->search_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| query | 

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_using_put**
> ManagedUserDTO update_user_using_put(managed_user_dto)

updateUser

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserresourceApi()
managed_user_dto = swagger_client.ManagedUserDTO() # ManagedUserDTO | managedUserDTO

try: 
    # updateUser
    api_response = api_instance.update_user_using_put(managed_user_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserresourceApi->update_user_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed_user_dto** | [**ManagedUserDTO**](ManagedUserDTO.md)| managedUserDTO | 

### Return type

[**ManagedUserDTO**](ManagedUserDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

