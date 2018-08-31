# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1alpha1DataVolumeSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'http': 'V1alpha1DataVolumeSourceHTTP',
        's3': 'V1alpha1DataVolumeSourceS3'
    }

    attribute_map = {
        'http': 'http',
        's3': 's3'
    }

    def __init__(self, http=None, s3=None):
        """
        V1alpha1DataVolumeSource - a model defined in Swagger
        """

        self._http = None
        self._s3 = None

        if http is not None:
          self.http = http
        if s3 is not None:
          self.s3 = s3

    @property
    def http(self):
        """
        Gets the http of this V1alpha1DataVolumeSource.

        :return: The http of this V1alpha1DataVolumeSource.
        :rtype: V1alpha1DataVolumeSourceHTTP
        """
        return self._http

    @http.setter
    def http(self, http):
        """
        Sets the http of this V1alpha1DataVolumeSource.

        :param http: The http of this V1alpha1DataVolumeSource.
        :type: V1alpha1DataVolumeSourceHTTP
        """

        self._http = http

    @property
    def s3(self):
        """
        Gets the s3 of this V1alpha1DataVolumeSource.

        :return: The s3 of this V1alpha1DataVolumeSource.
        :rtype: V1alpha1DataVolumeSourceS3
        """
        return self._s3

    @s3.setter
    def s3(self, s3):
        """
        Sets the s3 of this V1alpha1DataVolumeSource.

        :param s3: The s3 of this V1alpha1DataVolumeSource.
        :type: V1alpha1DataVolumeSourceS3
        """

        self._s3 = s3

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
        if not isinstance(other, V1alpha1DataVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
