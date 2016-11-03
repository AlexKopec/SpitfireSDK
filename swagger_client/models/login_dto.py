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


class LoginDTO(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, password=None, remember_me=None, username=None):
        """
        LoginDTO - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'password': 'str',
            'remember_me': 'bool',
            'username': 'str'
        }

        self.attribute_map = {
            'password': 'password',
            'remember_me': 'rememberMe',
            'username': 'username'
        }

        self._password = password
        self._remember_me = remember_me
        self._username = username


    @property
    def password(self):
        """
        Gets the password of this LoginDTO.


        :return: The password of this LoginDTO.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this LoginDTO.


        :param password: The password of this LoginDTO.
        :type: str
        """

        self._password = password

    @property
    def remember_me(self):
        """
        Gets the remember_me of this LoginDTO.


        :return: The remember_me of this LoginDTO.
        :rtype: bool
        """
        return self._remember_me

    @remember_me.setter
    def remember_me(self, remember_me):
        """
        Sets the remember_me of this LoginDTO.


        :param remember_me: The remember_me of this LoginDTO.
        :type: bool
        """

        self._remember_me = remember_me

    @property
    def username(self):
        """
        Gets the username of this LoginDTO.


        :return: The username of this LoginDTO.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this LoginDTO.


        :param username: The username of this LoginDTO.
        :type: str
        """

        self._username = username

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