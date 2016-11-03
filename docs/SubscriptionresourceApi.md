# swagger_client.SubscriptionresourceApi

All URIs are relative to *https://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription_using_post**](SubscriptionresourceApi.md#create_subscription_using_post) | **POST** /api/subscriptions | createSubscription
[**delete_subscription_using_delete**](SubscriptionresourceApi.md#delete_subscription_using_delete) | **DELETE** /api/subscriptions/{id} | deleteSubscription
[**get_all_subscriptions_using_get**](SubscriptionresourceApi.md#get_all_subscriptions_using_get) | **GET** /api/subscriptions | getAllSubscriptions
[**get_subscription_using_get**](SubscriptionresourceApi.md#get_subscription_using_get) | **GET** /api/subscriptions/{id} | getSubscription
[**update_subscription_using_put**](SubscriptionresourceApi.md#update_subscription_using_put) | **PUT** /api/subscriptions | updateSubscription


# **create_subscription_using_post**
> Subscription create_subscription_using_post(subscription)

createSubscription

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionresourceApi()
subscription = swagger_client.Subscription() # Subscription | subscription

try: 
    # createSubscription
    api_response = api_instance.create_subscription_using_post(subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionresourceApi->create_subscription_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription** | [**Subscription**](Subscription.md)| subscription | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription_using_delete**
> delete_subscription_using_delete(id)

deleteSubscription

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionresourceApi()
id = 789 # int | id

try: 
    # deleteSubscription
    api_instance.delete_subscription_using_delete(id)
except ApiException as e:
    print("Exception when calling SubscriptionresourceApi->delete_subscription_using_delete: %s\n" % e)
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

# **get_all_subscriptions_using_get**
> list[Subscription] get_all_subscriptions_using_get(email=email)

getAllSubscriptions

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionresourceApi()
email = 'admin@localhost' # str | email (optional) (default to admin@localhost)

try: 
    # getAllSubscriptions
    api_response = api_instance.get_all_subscriptions_using_get(email=email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionresourceApi->get_all_subscriptions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| email | [optional] [default to admin@localhost]

### Return type

[**list[Subscription]**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_using_get**
> Subscription get_subscription_using_get(id)

getSubscription

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionresourceApi()
id = 789 # int | id

try: 
    # getSubscription
    api_response = api_instance.get_subscription_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionresourceApi->get_subscription_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscription_using_put**
> Subscription update_subscription_using_put(subscription)

updateSubscription

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionresourceApi()
subscription = swagger_client.Subscription() # Subscription | subscription

try: 
    # updateSubscription
    api_response = api_instance.update_subscription_using_put(subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionresourceApi->update_subscription_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription** | [**Subscription**](Subscription.md)| subscription | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

