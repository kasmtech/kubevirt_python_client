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


class K8sIoApiCoreV1DownwardAPIVolumeFile(object):
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
        'field_ref': 'K8sIoApiCoreV1ObjectFieldSelector',
        'mode': 'int',
        'path': 'str',
        'resource_field_ref': 'K8sIoApiCoreV1ResourceFieldSelector'
    }

    attribute_map = {
        'field_ref': 'fieldRef',
        'mode': 'mode',
        'path': 'path',
        'resource_field_ref': 'resourceFieldRef'
    }

    def __init__(self, field_ref=None, mode=None, path='', resource_field_ref=None):
        """
        K8sIoApiCoreV1DownwardAPIVolumeFile - a model defined in Swagger
        """

        self._field_ref = None
        self._mode = None
        self._path = None
        self._resource_field_ref = None

        if field_ref is not None:
          self.field_ref = field_ref
        if mode is not None:
          self.mode = mode
        self.path = path
        if resource_field_ref is not None:
          self.resource_field_ref = resource_field_ref

    @property
    def field_ref(self):
        """
        Gets the field_ref of this K8sIoApiCoreV1DownwardAPIVolumeFile.
        Required: Selects a field of the pod: only annotations, labels, name, namespace and uid are supported.

        :return: The field_ref of this K8sIoApiCoreV1DownwardAPIVolumeFile.
        :rtype: K8sIoApiCoreV1ObjectFieldSelector
        """
        return self._field_ref

    @field_ref.setter
    def field_ref(self, field_ref):
        """
        Sets the field_ref of this K8sIoApiCoreV1DownwardAPIVolumeFile.
        Required: Selects a field of the pod: only annotations, labels, name, namespace and uid are supported.

        :param field_ref: The field_ref of this K8sIoApiCoreV1DownwardAPIVolumeFile.
        :type: K8sIoApiCoreV1ObjectFieldSelector
        """

        self._field_ref = field_ref

    @property
    def mode(self):
        """
        Gets the mode of this K8sIoApiCoreV1DownwardAPIVolumeFile.
        Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.

        :return: The mode of this K8sIoApiCoreV1DownwardAPIVolumeFile.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this K8sIoApiCoreV1DownwardAPIVolumeFile.
        Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.

        :param mode: The mode of this K8sIoApiCoreV1DownwardAPIVolumeFile.
        :type: int
        """

        self._mode = mode

    @property
    def path(self):
        """
        Gets the path of this K8sIoApiCoreV1DownwardAPIVolumeFile.
        Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'

        :return: The path of this K8sIoApiCoreV1DownwardAPIVolumeFile.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this K8sIoApiCoreV1DownwardAPIVolumeFile.
        Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'

        :param path: The path of this K8sIoApiCoreV1DownwardAPIVolumeFile.
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")

        self._path = path

    @property
    def resource_field_ref(self):
        """
        Gets the resource_field_ref of this K8sIoApiCoreV1DownwardAPIVolumeFile.
        Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.

        :return: The resource_field_ref of this K8sIoApiCoreV1DownwardAPIVolumeFile.
        :rtype: K8sIoApiCoreV1ResourceFieldSelector
        """
        return self._resource_field_ref

    @resource_field_ref.setter
    def resource_field_ref(self, resource_field_ref):
        """
        Sets the resource_field_ref of this K8sIoApiCoreV1DownwardAPIVolumeFile.
        Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.

        :param resource_field_ref: The resource_field_ref of this K8sIoApiCoreV1DownwardAPIVolumeFile.
        :type: K8sIoApiCoreV1ResourceFieldSelector
        """

        self._resource_field_ref = resource_field_ref

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
        if not isinstance(other, K8sIoApiCoreV1DownwardAPIVolumeFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
