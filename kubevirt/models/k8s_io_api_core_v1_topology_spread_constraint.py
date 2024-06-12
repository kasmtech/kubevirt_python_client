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


class K8sIoApiCoreV1TopologySpreadConstraint(object):
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
        'label_selector': 'K8sIoApimachineryPkgApisMetaV1LabelSelector',
        'match_label_keys': 'list[str]',
        'max_skew': 'int',
        'min_domains': 'int',
        'node_affinity_policy': 'str',
        'node_taints_policy': 'str',
        'topology_key': 'str',
        'when_unsatisfiable': 'str'
    }

    attribute_map = {
        'label_selector': 'labelSelector',
        'match_label_keys': 'matchLabelKeys',
        'max_skew': 'maxSkew',
        'min_domains': 'minDomains',
        'node_affinity_policy': 'nodeAffinityPolicy',
        'node_taints_policy': 'nodeTaintsPolicy',
        'topology_key': 'topologyKey',
        'when_unsatisfiable': 'whenUnsatisfiable'
    }

    def __init__(self, label_selector=None, match_label_keys=None, max_skew=0, min_domains=None, node_affinity_policy=None, node_taints_policy=None, topology_key='', when_unsatisfiable=''):
        """
        K8sIoApiCoreV1TopologySpreadConstraint - a model defined in Swagger
        """

        self._label_selector = None
        self._match_label_keys = None
        self._max_skew = None
        self._min_domains = None
        self._node_affinity_policy = None
        self._node_taints_policy = None
        self._topology_key = None
        self._when_unsatisfiable = None

        if label_selector is not None:
          self.label_selector = label_selector
        if match_label_keys is not None:
          self.match_label_keys = match_label_keys
        self.max_skew = max_skew
        if min_domains is not None:
          self.min_domains = min_domains
        if node_affinity_policy is not None:
          self.node_affinity_policy = node_affinity_policy
        if node_taints_policy is not None:
          self.node_taints_policy = node_taints_policy
        self.topology_key = topology_key
        self.when_unsatisfiable = when_unsatisfiable

    @property
    def label_selector(self):
        """
        Gets the label_selector of this K8sIoApiCoreV1TopologySpreadConstraint.
        LabelSelector is used to find matching pods. Pods that match this label selector are counted to determine the number of pods in their corresponding topology domain.

        :return: The label_selector of this K8sIoApiCoreV1TopologySpreadConstraint.
        :rtype: K8sIoApimachineryPkgApisMetaV1LabelSelector
        """
        return self._label_selector

    @label_selector.setter
    def label_selector(self, label_selector):
        """
        Sets the label_selector of this K8sIoApiCoreV1TopologySpreadConstraint.
        LabelSelector is used to find matching pods. Pods that match this label selector are counted to determine the number of pods in their corresponding topology domain.

        :param label_selector: The label_selector of this K8sIoApiCoreV1TopologySpreadConstraint.
        :type: K8sIoApimachineryPkgApisMetaV1LabelSelector
        """

        self._label_selector = label_selector

    @property
    def match_label_keys(self):
        """
        Gets the match_label_keys of this K8sIoApiCoreV1TopologySpreadConstraint.
        MatchLabelKeys is a set of pod label keys to select the pods over which spreading will be calculated. The keys are used to lookup values from the incoming pod labels, those key-value labels are ANDed with labelSelector to select the group of existing pods over which spreading will be calculated for the incoming pod. The same key is forbidden to exist in both MatchLabelKeys and LabelSelector. MatchLabelKeys cannot be set when LabelSelector isn't set. Keys that don't exist in the incoming pod labels will be ignored. A null or empty list means only match against labelSelector.  This is a beta field and requires the MatchLabelKeysInPodTopologySpread feature gate to be enabled (enabled by default).

        :return: The match_label_keys of this K8sIoApiCoreV1TopologySpreadConstraint.
        :rtype: list[str]
        """
        return self._match_label_keys

    @match_label_keys.setter
    def match_label_keys(self, match_label_keys):
        """
        Sets the match_label_keys of this K8sIoApiCoreV1TopologySpreadConstraint.
        MatchLabelKeys is a set of pod label keys to select the pods over which spreading will be calculated. The keys are used to lookup values from the incoming pod labels, those key-value labels are ANDed with labelSelector to select the group of existing pods over which spreading will be calculated for the incoming pod. The same key is forbidden to exist in both MatchLabelKeys and LabelSelector. MatchLabelKeys cannot be set when LabelSelector isn't set. Keys that don't exist in the incoming pod labels will be ignored. A null or empty list means only match against labelSelector.  This is a beta field and requires the MatchLabelKeysInPodTopologySpread feature gate to be enabled (enabled by default).

        :param match_label_keys: The match_label_keys of this K8sIoApiCoreV1TopologySpreadConstraint.
        :type: list[str]
        """

        self._match_label_keys = match_label_keys

    @property
    def max_skew(self):
        """
        Gets the max_skew of this K8sIoApiCoreV1TopologySpreadConstraint.
        MaxSkew describes the degree to which pods may be unevenly distributed. When `whenUnsatisfiable=DoNotSchedule`, it is the maximum permitted difference between the number of matching pods in the target topology and the global minimum. The global minimum is the minimum number of matching pods in an eligible domain or zero if the number of eligible domains is less than MinDomains. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 2/2/1: In this case, the global minimum is 1. | zone1 | zone2 | zone3 | |  P P  |  P P  |   P   | - if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 2/2/2; scheduling it onto zone1(zone2) would make the ActualSkew(3-1) on zone1(zone2) violate MaxSkew(1). - if MaxSkew is 2, incoming pod can be scheduled onto any zone. When `whenUnsatisfiable=ScheduleAnyway`, it is used to give higher precedence to topologies that satisfy it. It's a required field. Default value is 1 and 0 is not allowed.

        :return: The max_skew of this K8sIoApiCoreV1TopologySpreadConstraint.
        :rtype: int
        """
        return self._max_skew

    @max_skew.setter
    def max_skew(self, max_skew):
        """
        Sets the max_skew of this K8sIoApiCoreV1TopologySpreadConstraint.
        MaxSkew describes the degree to which pods may be unevenly distributed. When `whenUnsatisfiable=DoNotSchedule`, it is the maximum permitted difference between the number of matching pods in the target topology and the global minimum. The global minimum is the minimum number of matching pods in an eligible domain or zero if the number of eligible domains is less than MinDomains. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 2/2/1: In this case, the global minimum is 1. | zone1 | zone2 | zone3 | |  P P  |  P P  |   P   | - if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 2/2/2; scheduling it onto zone1(zone2) would make the ActualSkew(3-1) on zone1(zone2) violate MaxSkew(1). - if MaxSkew is 2, incoming pod can be scheduled onto any zone. When `whenUnsatisfiable=ScheduleAnyway`, it is used to give higher precedence to topologies that satisfy it. It's a required field. Default value is 1 and 0 is not allowed.

        :param max_skew: The max_skew of this K8sIoApiCoreV1TopologySpreadConstraint.
        :type: int
        """
        if max_skew is None:
            raise ValueError("Invalid value for `max_skew`, must not be `None`")

        self._max_skew = max_skew

    @property
    def min_domains(self):
        """
        Gets the min_domains of this K8sIoApiCoreV1TopologySpreadConstraint.
        MinDomains indicates a minimum number of eligible domains. When the number of eligible domains with matching topology keys is less than minDomains, Pod Topology Spread treats \"global minimum\" as 0, and then the calculation of Skew is performed. And when the number of eligible domains with matching topology keys equals or greater than minDomains, this value has no effect on scheduling. As a result, when the number of eligible domains is less than minDomains, scheduler won't schedule more than maxSkew Pods to those domains. If value is nil, the constraint behaves as if MinDomains is equal to 1. Valid values are integers greater than 0. When value is not nil, WhenUnsatisfiable must be DoNotSchedule.  For example, in a 3-zone cluster, MaxSkew is set to 2, MinDomains is set to 5 and pods with the same labelSelector spread as 2/2/2: | zone1 | zone2 | zone3 | |  P P  |  P P  |  P P  | The number of domains is less than 5(MinDomains), so \"global minimum\" is treated as 0. In this situation, new pod with the same labelSelector cannot be scheduled, because computed skew will be 3(3 - 0) if new Pod is scheduled to any of the three zones, it will violate MaxSkew.

        :return: The min_domains of this K8sIoApiCoreV1TopologySpreadConstraint.
        :rtype: int
        """
        return self._min_domains

    @min_domains.setter
    def min_domains(self, min_domains):
        """
        Sets the min_domains of this K8sIoApiCoreV1TopologySpreadConstraint.
        MinDomains indicates a minimum number of eligible domains. When the number of eligible domains with matching topology keys is less than minDomains, Pod Topology Spread treats \"global minimum\" as 0, and then the calculation of Skew is performed. And when the number of eligible domains with matching topology keys equals or greater than minDomains, this value has no effect on scheduling. As a result, when the number of eligible domains is less than minDomains, scheduler won't schedule more than maxSkew Pods to those domains. If value is nil, the constraint behaves as if MinDomains is equal to 1. Valid values are integers greater than 0. When value is not nil, WhenUnsatisfiable must be DoNotSchedule.  For example, in a 3-zone cluster, MaxSkew is set to 2, MinDomains is set to 5 and pods with the same labelSelector spread as 2/2/2: | zone1 | zone2 | zone3 | |  P P  |  P P  |  P P  | The number of domains is less than 5(MinDomains), so \"global minimum\" is treated as 0. In this situation, new pod with the same labelSelector cannot be scheduled, because computed skew will be 3(3 - 0) if new Pod is scheduled to any of the three zones, it will violate MaxSkew.

        :param min_domains: The min_domains of this K8sIoApiCoreV1TopologySpreadConstraint.
        :type: int
        """

        self._min_domains = min_domains

    @property
    def node_affinity_policy(self):
        """
        Gets the node_affinity_policy of this K8sIoApiCoreV1TopologySpreadConstraint.
        NodeAffinityPolicy indicates how we will treat Pod's nodeAffinity/nodeSelector when calculating pod topology spread skew. Options are: - Honor: only nodes matching nodeAffinity/nodeSelector are included in the calculations. - Ignore: nodeAffinity/nodeSelector are ignored. All nodes are included in the calculations.  If this value is nil, the behavior is equivalent to the Honor policy. This is a beta-level feature default enabled by the NodeInclusionPolicyInPodTopologySpread feature flag.  Possible enum values:  - `\"Honor\"` means use this scheduling directive when calculating pod topology spread skew.  - `\"Ignore\"` means ignore this scheduling directive when calculating pod topology spread skew.

        :return: The node_affinity_policy of this K8sIoApiCoreV1TopologySpreadConstraint.
        :rtype: str
        """
        return self._node_affinity_policy

    @node_affinity_policy.setter
    def node_affinity_policy(self, node_affinity_policy):
        """
        Sets the node_affinity_policy of this K8sIoApiCoreV1TopologySpreadConstraint.
        NodeAffinityPolicy indicates how we will treat Pod's nodeAffinity/nodeSelector when calculating pod topology spread skew. Options are: - Honor: only nodes matching nodeAffinity/nodeSelector are included in the calculations. - Ignore: nodeAffinity/nodeSelector are ignored. All nodes are included in the calculations.  If this value is nil, the behavior is equivalent to the Honor policy. This is a beta-level feature default enabled by the NodeInclusionPolicyInPodTopologySpread feature flag.  Possible enum values:  - `\"Honor\"` means use this scheduling directive when calculating pod topology spread skew.  - `\"Ignore\"` means ignore this scheduling directive when calculating pod topology spread skew.

        :param node_affinity_policy: The node_affinity_policy of this K8sIoApiCoreV1TopologySpreadConstraint.
        :type: str
        """
        allowed_values = ["Honor", "Ignore"]
        if node_affinity_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `node_affinity_policy` ({0}), must be one of {1}"
                .format(node_affinity_policy, allowed_values)
            )

        self._node_affinity_policy = node_affinity_policy

    @property
    def node_taints_policy(self):
        """
        Gets the node_taints_policy of this K8sIoApiCoreV1TopologySpreadConstraint.
        NodeTaintsPolicy indicates how we will treat node taints when calculating pod topology spread skew. Options are: - Honor: nodes without taints, along with tainted nodes for which the incoming pod has a toleration, are included. - Ignore: node taints are ignored. All nodes are included.  If this value is nil, the behavior is equivalent to the Ignore policy. This is a beta-level feature default enabled by the NodeInclusionPolicyInPodTopologySpread feature flag.  Possible enum values:  - `\"Honor\"` means use this scheduling directive when calculating pod topology spread skew.  - `\"Ignore\"` means ignore this scheduling directive when calculating pod topology spread skew.

        :return: The node_taints_policy of this K8sIoApiCoreV1TopologySpreadConstraint.
        :rtype: str
        """
        return self._node_taints_policy

    @node_taints_policy.setter
    def node_taints_policy(self, node_taints_policy):
        """
        Sets the node_taints_policy of this K8sIoApiCoreV1TopologySpreadConstraint.
        NodeTaintsPolicy indicates how we will treat node taints when calculating pod topology spread skew. Options are: - Honor: nodes without taints, along with tainted nodes for which the incoming pod has a toleration, are included. - Ignore: node taints are ignored. All nodes are included.  If this value is nil, the behavior is equivalent to the Ignore policy. This is a beta-level feature default enabled by the NodeInclusionPolicyInPodTopologySpread feature flag.  Possible enum values:  - `\"Honor\"` means use this scheduling directive when calculating pod topology spread skew.  - `\"Ignore\"` means ignore this scheduling directive when calculating pod topology spread skew.

        :param node_taints_policy: The node_taints_policy of this K8sIoApiCoreV1TopologySpreadConstraint.
        :type: str
        """
        allowed_values = ["Honor", "Ignore"]
        if node_taints_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `node_taints_policy` ({0}), must be one of {1}"
                .format(node_taints_policy, allowed_values)
            )

        self._node_taints_policy = node_taints_policy

    @property
    def topology_key(self):
        """
        Gets the topology_key of this K8sIoApiCoreV1TopologySpreadConstraint.
        TopologyKey is the key of node labels. Nodes that have a label with this key and identical values are considered to be in the same topology. We consider each <key, value> as a \"bucket\", and try to put balanced number of pods into each bucket. We define a domain as a particular instance of a topology. Also, we define an eligible domain as a domain whose nodes meet the requirements of nodeAffinityPolicy and nodeTaintsPolicy. e.g. If TopologyKey is \"kubernetes.io/hostname\", each Node is a domain of that topology. And, if TopologyKey is \"topology.kubernetes.io/zone\", each zone is a domain of that topology. It's a required field.

        :return: The topology_key of this K8sIoApiCoreV1TopologySpreadConstraint.
        :rtype: str
        """
        return self._topology_key

    @topology_key.setter
    def topology_key(self, topology_key):
        """
        Sets the topology_key of this K8sIoApiCoreV1TopologySpreadConstraint.
        TopologyKey is the key of node labels. Nodes that have a label with this key and identical values are considered to be in the same topology. We consider each <key, value> as a \"bucket\", and try to put balanced number of pods into each bucket. We define a domain as a particular instance of a topology. Also, we define an eligible domain as a domain whose nodes meet the requirements of nodeAffinityPolicy and nodeTaintsPolicy. e.g. If TopologyKey is \"kubernetes.io/hostname\", each Node is a domain of that topology. And, if TopologyKey is \"topology.kubernetes.io/zone\", each zone is a domain of that topology. It's a required field.

        :param topology_key: The topology_key of this K8sIoApiCoreV1TopologySpreadConstraint.
        :type: str
        """
        if topology_key is None:
            raise ValueError("Invalid value for `topology_key`, must not be `None`")

        self._topology_key = topology_key

    @property
    def when_unsatisfiable(self):
        """
        Gets the when_unsatisfiable of this K8sIoApiCoreV1TopologySpreadConstraint.
        WhenUnsatisfiable indicates how to deal with a pod if it doesn't satisfy the spread constraint. - DoNotSchedule (default) tells the scheduler not to schedule it. - ScheduleAnyway tells the scheduler to schedule the pod in any location,   but giving higher precedence to topologies that would help reduce the   skew. A constraint is considered \"Unsatisfiable\" for an incoming pod if and only if every possible node assignment for that pod would violate \"MaxSkew\" on some topology. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 3/1/1: | zone1 | zone2 | zone3 | | P P P |   P   |   P   | If WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled to zone2(zone3) to become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies MaxSkew(1). In other words, the cluster can still be imbalanced, but scheduler won't make it *more* imbalanced. It's a required field.  Possible enum values:  - `\"DoNotSchedule\"` instructs the scheduler not to schedule the pod when constraints are not satisfied.  - `\"ScheduleAnyway\"` instructs the scheduler to schedule the pod even if constraints are not satisfied.

        :return: The when_unsatisfiable of this K8sIoApiCoreV1TopologySpreadConstraint.
        :rtype: str
        """
        return self._when_unsatisfiable

    @when_unsatisfiable.setter
    def when_unsatisfiable(self, when_unsatisfiable):
        """
        Sets the when_unsatisfiable of this K8sIoApiCoreV1TopologySpreadConstraint.
        WhenUnsatisfiable indicates how to deal with a pod if it doesn't satisfy the spread constraint. - DoNotSchedule (default) tells the scheduler not to schedule it. - ScheduleAnyway tells the scheduler to schedule the pod in any location,   but giving higher precedence to topologies that would help reduce the   skew. A constraint is considered \"Unsatisfiable\" for an incoming pod if and only if every possible node assignment for that pod would violate \"MaxSkew\" on some topology. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 3/1/1: | zone1 | zone2 | zone3 | | P P P |   P   |   P   | If WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled to zone2(zone3) to become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies MaxSkew(1). In other words, the cluster can still be imbalanced, but scheduler won't make it *more* imbalanced. It's a required field.  Possible enum values:  - `\"DoNotSchedule\"` instructs the scheduler not to schedule the pod when constraints are not satisfied.  - `\"ScheduleAnyway\"` instructs the scheduler to schedule the pod even if constraints are not satisfied.

        :param when_unsatisfiable: The when_unsatisfiable of this K8sIoApiCoreV1TopologySpreadConstraint.
        :type: str
        """
        if when_unsatisfiable is None:
            raise ValueError("Invalid value for `when_unsatisfiable`, must not be `None`")
        allowed_values = ["DoNotSchedule", "ScheduleAnyway"]
        if when_unsatisfiable not in allowed_values:
            raise ValueError(
                "Invalid value for `when_unsatisfiable` ({0}), must be one of {1}"
                .format(when_unsatisfiable, allowed_values)
            )

        self._when_unsatisfiable = when_unsatisfiable

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
        if not isinstance(other, K8sIoApiCoreV1TopologySpreadConstraint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
