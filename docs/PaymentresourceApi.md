# swagger_client.PaymentresourceApi

All URIs are relative to *https://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_using_post**](PaymentresourceApi.md#create_payment_using_post) | **POST** /api/payments | createPayment
[**delete_payment_using_delete**](PaymentresourceApi.md#delete_payment_using_delete) | **DELETE** /api/payments/{id} | deletePayment
[**get_all_payments_using_get**](PaymentresourceApi.md#get_all_payments_using_get) | **GET** /api/payments | getAllPayments
[**get_payment_using_get**](PaymentresourceApi.md#get_payment_using_get) | **GET** /api/payments/{id} | getPayment
[**handle_notification_using_post**](PaymentresourceApi.md#handle_notification_using_post) | **POST** /api/notify | handleNotification
[**update_payment_using_put**](PaymentresourceApi.md#update_payment_using_put) | **PUT** /api/payments | updatePayment


# **create_payment_using_post**
> Payment create_payment_using_post(payment)

createPayment

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentresourceApi()
payment = swagger_client.Payment() # Payment | payment

try: 
    # createPayment
    api_response = api_instance.create_payment_using_post(payment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentresourceApi->create_payment_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment** | [**Payment**](Payment.md)| payment | 

### Return type

[**Payment**](Payment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment_using_delete**
> delete_payment_using_delete(id)

deletePayment

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentresourceApi()
id = 789 # int | id

try: 
    # deletePayment
    api_instance.delete_payment_using_delete(id)
except ApiException as e:
    print("Exception when calling PaymentresourceApi->delete_payment_using_delete: %s\n" % e)
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

# **get_all_payments_using_get**
> list[Payment] get_all_payments_using_get(email=email)

getAllPayments

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentresourceApi()
email = 'admin@localhost' # str | email (optional) (default to admin@localhost)

try: 
    # getAllPayments
    api_response = api_instance.get_all_payments_using_get(email=email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentresourceApi->get_all_payments_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| email | [optional] [default to admin@localhost]

### Return type

[**list[Payment]**](Payment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_using_get**
> Payment get_payment_using_get(id)

getPayment

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentresourceApi()
id = 789 # int | id

try: 
    # getPayment
    api_response = api_instance.get_payment_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentresourceApi->get_payment_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**Payment**](Payment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_notification_using_post**
> str handle_notification_using_post()

handleNotification

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentresourceApi()

try: 
    # handleNotification
    api_response = api_instance.handle_notification_using_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentresourceApi->handle_notification_using_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_using_put**
> Payment update_payment_using_put(payment)

updatePayment

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentresourceApi()
payment = swagger_client.Payment() # Payment | payment

try: 
    # updatePayment
    api_response = api_instance.update_payment_using_put(payment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentresourceApi->update_payment_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment** | [**Payment**](Payment.md)| payment | 

### Return type

[**Payment**](Payment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

