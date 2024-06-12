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


class K8sIoApiCoreV1ResourceRequirements(object):
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
        'claims': 'list[K8sIoApiCoreV1ResourceClaim]',
        'limits': 'dict(str, K8sIoApimachineryPkgApiResourceQuantity)',
        'requests': 'dict(str, K8sIoApimachineryPkgApiResourceQuantity)'
    }

    attribute_map = {
        'claims': 'claims',
        'limits': 'limits',
        'requests': 'requests'
    }

    def __init__(self, claims=None, limits=None, requests=None):
        """
        K8sIoApiCoreV1ResourceRequirements - a model defined in Swagger
        """

        self._claims = None
        self._limits = None
        self._requests = None

        if claims is not None:
          self.claims = claims
        if limits is not None:
          self.limits = limits
        if requests is not None:
          self.requests = requests

    @property
    def claims(self):
        """
        Gets the claims of this K8sIoApiCoreV1ResourceRequirements.
        Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.  This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.  This field is immutable. It can only be set for containers.

        :return: The claims of this K8sIoApiCoreV1ResourceRequirements.
        :rtype: list[K8sIoApiCoreV1ResourceClaim]
        """
        return self._claims

    @claims.setter
    def claims(self, claims):
        """
        Sets the claims of this K8sIoApiCoreV1ResourceRequirements.
        Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.  This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.  This field is immutable. It can only be set for containers.

        :param claims: The claims of this K8sIoApiCoreV1ResourceRequirements.
        :type: list[K8sIoApiCoreV1ResourceClaim]
        """

        self._claims = claims

    @property
    def limits(self):
        """
        Gets the limits of this K8sIoApiCoreV1ResourceRequirements.
        Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

        :return: The limits of this K8sIoApiCoreV1ResourceRequirements.
        :rtype: dict(str, K8sIoApimachineryPkgApiResourceQuantity)
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """
        Sets the limits of this K8sIoApiCoreV1ResourceRequirements.
        Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

        :param limits: The limits of this K8sIoApiCoreV1ResourceRequirements.
        :type: dict(str, K8sIoApimachineryPkgApiResourceQuantity)
        """

        self._limits = limits

    @property
    def requests(self):
        """
        Gets the requests of this K8sIoApiCoreV1ResourceRequirements.
        Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

        :return: The requests of this K8sIoApiCoreV1ResourceRequirements.
        :rtype: dict(str, K8sIoApimachineryPkgApiResourceQuantity)
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        """
        Sets the requests of this K8sIoApiCoreV1ResourceRequirements.
        Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

        :param requests: The requests of this K8sIoApiCoreV1ResourceRequirements.
        :type: dict(str, K8sIoApimachineryPkgApiResourceQuantity)
        """

        self._requests = requests

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
        if not isinstance(other, K8sIoApiCoreV1ResourceRequirements):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
