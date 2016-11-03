# coding: utf-8

"""
    spitfire API

    spitfire API documentation

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class ContactInfoDTO(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, email1=None, email2=None, facebook=None, id=None, phone1=None, phone2=None, phone3=None, skype=None):
        """
        ContactInfoDTO - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'email1': 'str',
            'email2': 'str',
            'facebook': 'str',
            'id': 'int',
            'phone1': 'str',
            'phone2': 'str',
            'phone3': 'str',
            'skype': 'str'
        }

        self.attribute_map = {
            'email1': 'email1',
            'email2': 'email2',
            'facebook': 'facebook',
            'id': 'id',
            'phone1': 'phone1',
            'phone2': 'phone2',
            'phone3': 'phone3',
            'skype': 'skype'
        }

        self._email1 = email1
        self._email2 = email2
        self._facebook = facebook
        self._id = id
        self._phone1 = phone1
        self._phone2 = phone2
        self._phone3 = phone3
        self._skype = skype


    @property
    def email1(self):
        """
        Gets the email1 of this ContactInfoDTO.


        :return: The email1 of this ContactInfoDTO.
        :rtype: str
        """
        return self._email1

    @email1.setter
    def email1(self, email1):
        """
        Sets the email1 of this ContactInfoDTO.


        :param email1: The email1 of this ContactInfoDTO.
        :type: str
        """

        self._email1 = email1

    @property
    def email2(self):
        """
        Gets the email2 of this ContactInfoDTO.


        :return: The email2 of this ContactInfoDTO.
        :rtype: str
        """
        return self._email2

    @email2.setter
    def email2(self, email2):
        """
        Sets the email2 of this ContactInfoDTO.


        :param email2: The email2 of this ContactInfoDTO.
        :type: str
        """

        self._email2 = email2

    @property
    def facebook(self):
        """
        Gets the facebook of this ContactInfoDTO.


        :return: The facebook of this ContactInfoDTO.
        :rtype: str
        """
        return self._facebook

    @facebook.setter
    def facebook(self, facebook):
        """
        Sets the facebook of this ContactInfoDTO.


        :param facebook: The facebook of this ContactInfoDTO.
        :type: str
        """

        self._facebook = facebook

    @property
    def id(self):
        """
        Gets the id of this ContactInfoDTO.


        :return: The id of this ContactInfoDTO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ContactInfoDTO.


        :param id: The id of this ContactInfoDTO.
        :type: int
        """

        self._id = id

    @property
    def phone1(self):
        """
        Gets the phone1 of this ContactInfoDTO.


        :return: The phone1 of this ContactInfoDTO.
        :rtype: str
        """
        return self._phone1

    @phone1.setter
    def phone1(self, phone1):
        """
        Sets the phone1 of this ContactInfoDTO.


        :param phone1: The phone1 of this ContactInfoDTO.
        :type: str
        """

        self._phone1 = phone1

    @property
    def phone2(self):
        """
        Gets the phone2 of this ContactInfoDTO.


        :return: The phone2 of this ContactInfoDTO.
        :rtype: str
        """
        return self._phone2

    @phone2.setter
    def phone2(self, phone2):
        """
        Sets the phone2 of this ContactInfoDTO.


        :param phone2: The phone2 of this ContactInfoDTO.
        :type: str
        """

        self._phone2 = phone2

    @property
    def phone3(self):
        """
        Gets the phone3 of this ContactInfoDTO.


        :return: The phone3 of this ContactInfoDTO.
        :rtype: str
        """
        return self._phone3

    @phone3.setter
    def phone3(self, phone3):
        """
        Sets the phone3 of this ContactInfoDTO.


        :param phone3: The phone3 of this ContactInfoDTO.
        :type: str
        """

        self._phone3 = phone3

    @property
    def skype(self):
        """
        Gets the skype of this ContactInfoDTO.


        :return: The skype of this ContactInfoDTO.
        :rtype: str
        """
        return self._skype

    @skype.setter
    def skype(self, skype):
        """
        Sets the skype of this ContactInfoDTO.


        :param skype: The skype of this ContactInfoDTO.
        :type: str
        """

        self._skype = skype

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other