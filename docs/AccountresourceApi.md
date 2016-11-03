# swagger_client.AccountresourceApi

All URIs are relative to *https://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_account_using_get**](AccountresourceApi.md#activate_account_using_get) | **GET** /api/activate | activateAccount
[**change_password_using_post**](AccountresourceApi.md#change_password_using_post) | **POST** /api/account/change_password | changePassword
[**finish_password_reset_using_post**](AccountresourceApi.md#finish_password_reset_using_post) | **POST** /api/account/reset_password/finish | finishPasswordReset
[**get_account_using_get**](AccountresourceApi.md#get_account_using_get) | **GET** /api/account | getAccount
[**is_authenticated_using_get**](AccountresourceApi.md#is_authenticated_using_get) | **GET** /api/authenticate | isAuthenticated
[**register_account_using_post**](AccountresourceApi.md#register_account_using_post) | **POST** /api/register | registerAccount
[**request_password_reset_using_post**](AccountresourceApi.md#request_password_reset_using_post) | **POST** /api/account/reset_password/init | requestPasswordReset
[**save_account_using_post**](AccountresourceApi.md#save_account_using_post) | **POST** /api/account | saveAccount


# **activate_account_using_get**
> str activate_account_using_get(key)

activateAccount

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountresourceApi()
key = 'key_example' # str | key

try: 
    # activateAccount
    api_response = api_instance.activate_account_using_get(key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountresourceApi->activate_account_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| key | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_password_using_post**
> object change_password_using_post(password)

changePassword

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountresourceApi()
password = 'password_example' # str | password

try: 
    # changePassword
    api_response = api_instance.change_password_using_post(password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountresourceApi->change_password_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | **str**| password | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finish_password_reset_using_post**
> str finish_password_reset_using_post(key_and_password)

finishPasswordReset

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountresourceApi()
key_and_password = swagger_client.KeyAndPasswordDTO() # KeyAndPasswordDTO | keyAndPassword

try: 
    # finishPasswordReset
    api_response = api_instance.finish_password_reset_using_post(key_and_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountresourceApi->finish_password_reset_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_and_password** | [**KeyAndPasswordDTO**](KeyAndPasswordDTO.md)| keyAndPassword | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_using_get**
> UserDTO get_account_using_get()

getAccount

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountresourceApi()

try: 
    # getAccount
    api_response = api_instance.get_account_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountresourceApi->get_account_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserDTO**](UserDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_authenticated_using_get**
> str is_authenticated_using_get()

isAuthenticated

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountresourceApi()

try: 
    # isAuthenticated
    api_response = api_instance.is_authenticated_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountresourceApi->is_authenticated_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_account_using_post**
> object register_account_using_post(managed_user_dto)

registerAccount

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountresourceApi()
managed_user_dto = swagger_client.ManagedUserDTO() # ManagedUserDTO | managedUserDTO

try: 
    # registerAccount
    api_response = api_instance.register_account_using_post(managed_user_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountresourceApi->register_account_using_post: %s\n" % e)
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
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_password_reset_using_post**
> object request_password_reset_using_post(mail)

requestPasswordReset

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountresourceApi()
mail = 'mail_example' # str | mail

try: 
    # requestPasswordReset
    api_response = api_instance.request_password_reset_using_post(mail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountresourceApi->request_password_reset_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail** | **str**| mail | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_account_using_post**
> str save_account_using_post(user_dto)

saveAccount

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountresourceApi()
user_dto = swagger_client.UserDTO() # UserDTO | userDTO

try: 
    # saveAccount
    api_response = api_instance.save_account_using_post(user_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountresourceApi->save_account_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_dto** | [**UserDTO**](UserDTO.md)| userDTO | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

