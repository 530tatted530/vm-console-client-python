# coding: utf-8

"""
    Python InsightVM API Client

    OpenAPI spec version: 3
    Contact: support@rapid7.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AssetPolicy(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'benchmark_name': 'str',
        'benchmark_version': 'str',
        'category': 'str',
        'description': 'str',
        'failed_assets_count': 'int',
        'failed_rules_count': 'int',
        'id': 'str',
        'is_custom': 'bool',
        'links': 'list[Link]',
        'not_applicable_assets_count': 'int',
        'not_applicable_rules_count': 'int',
        'passed_assets_count': 'int',
        'passed_rules_count': 'int',
        'policy_name': 'str',
        'rule_compliance': 'float',
        'rule_compliance_delta': 'float',
        'scope': 'str',
        'status': 'str',
        'surrogate_id': 'int',
        'title': 'str',
        'unscored_rules': 'int'
    }

    attribute_map = {
        'benchmark_name': 'benchmarkName',
        'benchmark_version': 'benchmarkVersion',
        'category': 'category',
        'description': 'description',
        'failed_assets_count': 'failedAssetsCount',
        'failed_rules_count': 'failedRulesCount',
        'id': 'id',
        'is_custom': 'isCustom',
        'links': 'links',
        'not_applicable_assets_count': 'notApplicableAssetsCount',
        'not_applicable_rules_count': 'notApplicableRulesCount',
        'passed_assets_count': 'passedAssetsCount',
        'passed_rules_count': 'passedRulesCount',
        'policy_name': 'policyName',
        'rule_compliance': 'ruleCompliance',
        'rule_compliance_delta': 'ruleComplianceDelta',
        'scope': 'scope',
        'status': 'status',
        'surrogate_id': 'surrogateId',
        'title': 'title',
        'unscored_rules': 'unscoredRules'
    }

    def __init__(self, benchmark_name=None, benchmark_version=None, category=None, description=None, failed_assets_count=None, failed_rules_count=None, id=None, is_custom=None, links=None, not_applicable_assets_count=None, not_applicable_rules_count=None, passed_assets_count=None, passed_rules_count=None, policy_name=None, rule_compliance=None, rule_compliance_delta=None, scope=None, status=None, surrogate_id=None, title=None, unscored_rules=None):  # noqa: E501
        """AssetPolicy - a model defined in Swagger"""  # noqa: E501

        self._benchmark_name = None
        self._benchmark_version = None
        self._category = None
        self._description = None
        self._failed_assets_count = None
        self._failed_rules_count = None
        self._id = None
        self._is_custom = None
        self._links = None
        self._not_applicable_assets_count = None
        self._not_applicable_rules_count = None
        self._passed_assets_count = None
        self._passed_rules_count = None
        self._policy_name = None
        self._rule_compliance = None
        self._rule_compliance_delta = None
        self._scope = None
        self._status = None
        self._surrogate_id = None
        self._title = None
        self._unscored_rules = None
        self.discriminator = None

        if benchmark_name is not None:
            self.benchmark_name = benchmark_name
        if benchmark_version is not None:
            self.benchmark_version = benchmark_version
        if category is not None:
            self.category = category
        if description is not None:
            self.description = description
        if failed_assets_count is not None:
            self.failed_assets_count = failed_assets_count
        if failed_rules_count is not None:
            self.failed_rules_count = failed_rules_count
        if id is not None:
            self.id = id
        if is_custom is not None:
            self.is_custom = is_custom
        if links is not None:
            self.links = links
        if not_applicable_assets_count is not None:
            self.not_applicable_assets_count = not_applicable_assets_count
        if not_applicable_rules_count is not None:
            self.not_applicable_rules_count = not_applicable_rules_count
        if passed_assets_count is not None:
            self.passed_assets_count = passed_assets_count
        if passed_rules_count is not None:
            self.passed_rules_count = passed_rules_count
        if policy_name is not None:
            self.policy_name = policy_name
        if rule_compliance is not None:
            self.rule_compliance = rule_compliance
        if rule_compliance_delta is not None:
            self.rule_compliance_delta = rule_compliance_delta
        if scope is not None:
            self.scope = scope
        if status is not None:
            self.status = status
        if surrogate_id is not None:
            self.surrogate_id = surrogate_id
        if title is not None:
            self.title = title
        if unscored_rules is not None:
            self.unscored_rules = unscored_rules

    @property
    def benchmark_name(self):
        """Gets the benchmark_name of this AssetPolicy.  # noqa: E501

        The name of the policy's benchmark.  # noqa: E501

        :return: The benchmark_name of this AssetPolicy.  # noqa: E501
        :rtype: str
        """
        return self._benchmark_name

    @benchmark_name.setter
    def benchmark_name(self, benchmark_name):
        """Sets the benchmark_name of this AssetPolicy.

        The name of the policy's benchmark.  # noqa: E501

        :param benchmark_name: The benchmark_name of this AssetPolicy.  # noqa: E501
        :type: str
        """

        self._benchmark_name = benchmark_name

    @property
    def benchmark_version(self):
        """Gets the benchmark_version of this AssetPolicy.  # noqa: E501

        The version number of the benchmark that includes the policy.  # noqa: E501

        :return: The benchmark_version of this AssetPolicy.  # noqa: E501
        :rtype: str
        """
        return self._benchmark_version

    @benchmark_version.setter
    def benchmark_version(self, benchmark_version):
        """Sets the benchmark_version of this AssetPolicy.

        The version number of the benchmark that includes the policy.  # noqa: E501

        :param benchmark_version: The benchmark_version of this AssetPolicy.  # noqa: E501
        :type: str
        """

        self._benchmark_version = benchmark_version

    @property
    def category(self):
        """Gets the category of this AssetPolicy.  # noqa: E501

        A grouping of similar benchmarks based on their source, purpose, or other criteria. Examples include FDCC, USGCB, and CIS.  # noqa: E501

        :return: The category of this AssetPolicy.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this AssetPolicy.

        A grouping of similar benchmarks based on their source, purpose, or other criteria. Examples include FDCC, USGCB, and CIS.  # noqa: E501

        :param category: The category of this AssetPolicy.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def description(self):
        """Gets the description of this AssetPolicy.  # noqa: E501

        The description of the policy.  # noqa: E501

        :return: The description of this AssetPolicy.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AssetPolicy.

        The description of the policy.  # noqa: E501

        :param description: The description of this AssetPolicy.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def failed_assets_count(self):
        """Gets the failed_assets_count of this AssetPolicy.  # noqa: E501

        The number of assets that are not compliant with the policy. The assets considered in the calculation are based on the user's list of accessible assets.  # noqa: E501

        :return: The failed_assets_count of this AssetPolicy.  # noqa: E501
        :rtype: int
        """
        return self._failed_assets_count

    @failed_assets_count.setter
    def failed_assets_count(self, failed_assets_count):
        """Sets the failed_assets_count of this AssetPolicy.

        The number of assets that are not compliant with the policy. The assets considered in the calculation are based on the user's list of accessible assets.  # noqa: E501

        :param failed_assets_count: The failed_assets_count of this AssetPolicy.  # noqa: E501
        :type: int
        """

        self._failed_assets_count = failed_assets_count

    @property
    def failed_rules_count(self):
        """Gets the failed_rules_count of this AssetPolicy.  # noqa: E501

        The number of rules in the policy that are not compliant with any scanned assets. The assets considered in the calculation are based on the user's list of accessible assets.  # noqa: E501

        :return: The failed_rules_count of this AssetPolicy.  # noqa: E501
        :rtype: int
        """
        return self._failed_rules_count

    @failed_rules_count.setter
    def failed_rules_count(self, failed_rules_count):
        """Sets the failed_rules_count of this AssetPolicy.

        The number of rules in the policy that are not compliant with any scanned assets. The assets considered in the calculation are based on the user's list of accessible assets.  # noqa: E501

        :param failed_rules_count: The failed_rules_count of this AssetPolicy.  # noqa: E501
        :type: int
        """

        self._failed_rules_count = failed_rules_count

    @property
    def id(self):
        """Gets the id of this AssetPolicy.  # noqa: E501

        The textual representation of the policy identifier.  # noqa: E501

        :return: The id of this AssetPolicy.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssetPolicy.

        The textual representation of the policy identifier.  # noqa: E501

        :param id: The id of this AssetPolicy.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_custom(self):
        """Gets the is_custom of this AssetPolicy.  # noqa: E501

        A flag indicating whether the policy is custom.  # noqa: E501

        :return: The is_custom of this AssetPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._is_custom

    @is_custom.setter
    def is_custom(self, is_custom):
        """Sets the is_custom of this AssetPolicy.

        A flag indicating whether the policy is custom.  # noqa: E501

        :param is_custom: The is_custom of this AssetPolicy.  # noqa: E501
        :type: bool
        """

        self._is_custom = is_custom

    @property
    def links(self):
        """Gets the links of this AssetPolicy.  # noqa: E501

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :return: The links of this AssetPolicy.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AssetPolicy.

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :param links: The links of this AssetPolicy.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def not_applicable_assets_count(self):
        """Gets the not_applicable_assets_count of this AssetPolicy.  # noqa: E501

        The number of assets that were attempted to be scanned, but are not applicable to the policy. The assets considered in the calculation are based on the user's list of accessible assets.  # noqa: E501

        :return: The not_applicable_assets_count of this AssetPolicy.  # noqa: E501
        :rtype: int
        """
        return self._not_applicable_assets_count

    @not_applicable_assets_count.setter
    def not_applicable_assets_count(self, not_applicable_assets_count):
        """Sets the not_applicable_assets_count of this AssetPolicy.

        The number of assets that were attempted to be scanned, but are not applicable to the policy. The assets considered in the calculation are based on the user's list of accessible assets.  # noqa: E501

        :param not_applicable_assets_count: The not_applicable_assets_count of this AssetPolicy.  # noqa: E501
        :type: int
        """

        self._not_applicable_assets_count = not_applicable_assets_count

    @property
    def not_applicable_rules_count(self):
        """Gets the not_applicable_rules_count of this AssetPolicy.  # noqa: E501

        The number of rules in the policy that are not applicable with any scanned assets. The assets considered in the calculation are based on the user's list of accessible assets.  # noqa: E501

        :return: The not_applicable_rules_count of this AssetPolicy.  # noqa: E501
        :rtype: int
        """
        return self._not_applicable_rules_count

    @not_applicable_rules_count.setter
    def not_applicable_rules_count(self, not_applicable_rules_count):
        """Sets the not_applicable_rules_count of this AssetPolicy.

        The number of rules in the policy that are not applicable with any scanned assets. The assets considered in the calculation are based on the user's list of accessible assets.  # noqa: E501

        :param not_applicable_rules_count: The not_applicable_rules_count of this AssetPolicy.  # noqa: E501
        :type: int
        """

        self._not_applicable_rules_count = not_applicable_rules_count

    @property
    def passed_assets_count(self):
        """Gets the passed_assets_count of this AssetPolicy.  # noqa: E501

        The number of assets that are compliant with the policy. The assets considered in the calculation are based on the user's list of accessible assets.  # noqa: E501

        :return: The passed_assets_count of this AssetPolicy.  # noqa: E501
        :rtype: int
        """
        return self._passed_assets_count

    @passed_assets_count.setter
    def passed_assets_count(self, passed_assets_count):
        """Sets the passed_assets_count of this AssetPolicy.

        The number of assets that are compliant with the policy. The assets considered in the calculation are based on the user's list of accessible assets.  # noqa: E501

        :param passed_assets_count: The passed_assets_count of this AssetPolicy.  # noqa: E501
        :type: int
        """

        self._passed_assets_count = passed_assets_count

    @property
    def passed_rules_count(self):
        """Gets the passed_rules_count of this AssetPolicy.  # noqa: E501

        The number of rules in the policy that are compliant with all scanned assets. The assets considered in the calculation are based on the user's list of accessible assets.  # noqa: E501

        :return: The passed_rules_count of this AssetPolicy.  # noqa: E501
        :rtype: int
        """
        return self._passed_rules_count

    @passed_rules_count.setter
    def passed_rules_count(self, passed_rules_count):
        """Sets the passed_rules_count of this AssetPolicy.

        The number of rules in the policy that are compliant with all scanned assets. The assets considered in the calculation are based on the user's list of accessible assets.  # noqa: E501

        :param passed_rules_count: The passed_rules_count of this AssetPolicy.  # noqa: E501
        :type: int
        """

        self._passed_rules_count = passed_rules_count

    @property
    def policy_name(self):
        """Gets the policy_name of this AssetPolicy.  # noqa: E501

        The name of the policy.  # noqa: E501

        :return: The policy_name of this AssetPolicy.  # noqa: E501
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this AssetPolicy.

        The name of the policy.  # noqa: E501

        :param policy_name: The policy_name of this AssetPolicy.  # noqa: E501
        :type: str
        """

        self._policy_name = policy_name

    @property
    def rule_compliance(self):
        """Gets the rule_compliance of this AssetPolicy.  # noqa: E501

        The ratio of PASS results for the rules to the total number of rules in each policy.  # noqa: E501

        :return: The rule_compliance of this AssetPolicy.  # noqa: E501
        :rtype: float
        """
        return self._rule_compliance

    @rule_compliance.setter
    def rule_compliance(self, rule_compliance):
        """Sets the rule_compliance of this AssetPolicy.

        The ratio of PASS results for the rules to the total number of rules in each policy.  # noqa: E501

        :param rule_compliance: The rule_compliance of this AssetPolicy.  # noqa: E501
        :type: float
        """

        self._rule_compliance = rule_compliance

    @property
    def rule_compliance_delta(self):
        """Gets the rule_compliance_delta of this AssetPolicy.  # noqa: E501

        The change in rule compliance between the last two scans of all assets. The list of scanned policies is based on the user's list of accessible assets.  # noqa: E501

        :return: The rule_compliance_delta of this AssetPolicy.  # noqa: E501
        :rtype: float
        """
        return self._rule_compliance_delta

    @rule_compliance_delta.setter
    def rule_compliance_delta(self, rule_compliance_delta):
        """Sets the rule_compliance_delta of this AssetPolicy.

        The change in rule compliance between the last two scans of all assets. The list of scanned policies is based on the user's list of accessible assets.  # noqa: E501

        :param rule_compliance_delta: The rule_compliance_delta of this AssetPolicy.  # noqa: E501
        :type: float
        """

        self._rule_compliance_delta = rule_compliance_delta

    @property
    def scope(self):
        """Gets the scope of this AssetPolicy.  # noqa: E501

        The textual representation of the policy scope. Policies that are automatically available have `\"Built-in\"` scope, whereas policies created by users have scope as `\"Custom\"`.  # noqa: E501

        :return: The scope of this AssetPolicy.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this AssetPolicy.

        The textual representation of the policy scope. Policies that are automatically available have `\"Built-in\"` scope, whereas policies created by users have scope as `\"Custom\"`.  # noqa: E501

        :param scope: The scope of this AssetPolicy.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def status(self):
        """Gets the status of this AssetPolicy.  # noqa: E501

        The overall compliance status of the policy.  # noqa: E501

        :return: The status of this AssetPolicy.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AssetPolicy.

        The overall compliance status of the policy.  # noqa: E501

        :param status: The status of this AssetPolicy.  # noqa: E501
        :type: str
        """
        allowed_values = ["PASS", "FAIL", "NOT_APPLICABLE"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def surrogate_id(self):
        """Gets the surrogate_id of this AssetPolicy.  # noqa: E501

        The identifier of the policy  # noqa: E501

        :return: The surrogate_id of this AssetPolicy.  # noqa: E501
        :rtype: int
        """
        return self._surrogate_id

    @surrogate_id.setter
    def surrogate_id(self, surrogate_id):
        """Sets the surrogate_id of this AssetPolicy.

        The identifier of the policy  # noqa: E501

        :param surrogate_id: The surrogate_id of this AssetPolicy.  # noqa: E501
        :type: int
        """

        self._surrogate_id = surrogate_id

    @property
    def title(self):
        """Gets the title of this AssetPolicy.  # noqa: E501

        The title of the policy as visible to the user.  # noqa: E501

        :return: The title of this AssetPolicy.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this AssetPolicy.

        The title of the policy as visible to the user.  # noqa: E501

        :param title: The title of this AssetPolicy.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def unscored_rules(self):
        """Gets the unscored_rules of this AssetPolicy.  # noqa: E501

        The number of rules defined in the policy with a role of \"unscored\". These rules will not affect rule compliance scoring for the policy.  # noqa: E501

        :return: The unscored_rules of this AssetPolicy.  # noqa: E501
        :rtype: int
        """
        return self._unscored_rules

    @unscored_rules.setter
    def unscored_rules(self, unscored_rules):
        """Sets the unscored_rules of this AssetPolicy.

        The number of rules defined in the policy with a role of \"unscored\". These rules will not affect rule compliance scoring for the policy.  # noqa: E501

        :param unscored_rules: The unscored_rules of this AssetPolicy.  # noqa: E501
        :type: int
        """

        self._unscored_rules = unscored_rules

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(AssetPolicy, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AssetPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
