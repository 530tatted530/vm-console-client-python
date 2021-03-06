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


class PCI(object):
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
        'adjusted_cvss_score': 'int',
        'adjusted_severity_score': 'int',
        'fail': 'bool',
        'special_notes': 'str',
        'status': 'str'
    }

    attribute_map = {
        'adjusted_cvss_score': 'adjustedCVSSScore',
        'adjusted_severity_score': 'adjustedSeverityScore',
        'fail': 'fail',
        'special_notes': 'specialNotes',
        'status': 'status'
    }

    def __init__(self, adjusted_cvss_score=None, adjusted_severity_score=None, fail=None, special_notes=None, status=None):  # noqa: E501
        """PCI - a model defined in Swagger"""  # noqa: E501

        self._adjusted_cvss_score = None
        self._adjusted_severity_score = None
        self._fail = None
        self._special_notes = None
        self._status = None
        self.discriminator = None

        if adjusted_cvss_score is not None:
            self.adjusted_cvss_score = adjusted_cvss_score
        if adjusted_severity_score is not None:
            self.adjusted_severity_score = adjusted_severity_score
        if fail is not None:
            self.fail = fail
        if special_notes is not None:
            self.special_notes = special_notes
        if status is not None:
            self.status = status

    @property
    def adjusted_cvss_score(self):
        """Gets the adjusted_cvss_score of this PCI.  # noqa: E501

        The CVSS score of the vulnerability, adjusted for PCI rules and exceptions, on a scale of 0-10.  # noqa: E501

        :return: The adjusted_cvss_score of this PCI.  # noqa: E501
        :rtype: int
        """
        return self._adjusted_cvss_score

    @adjusted_cvss_score.setter
    def adjusted_cvss_score(self, adjusted_cvss_score):
        """Sets the adjusted_cvss_score of this PCI.

        The CVSS score of the vulnerability, adjusted for PCI rules and exceptions, on a scale of 0-10.  # noqa: E501

        :param adjusted_cvss_score: The adjusted_cvss_score of this PCI.  # noqa: E501
        :type: int
        """

        self._adjusted_cvss_score = adjusted_cvss_score

    @property
    def adjusted_severity_score(self):
        """Gets the adjusted_severity_score of this PCI.  # noqa: E501

        The severity score of the vulnerability, adjusted for PCI rules and exceptions, on a scale of 0-10.  # noqa: E501

        :return: The adjusted_severity_score of this PCI.  # noqa: E501
        :rtype: int
        """
        return self._adjusted_severity_score

    @adjusted_severity_score.setter
    def adjusted_severity_score(self, adjusted_severity_score):
        """Sets the adjusted_severity_score of this PCI.

        The severity score of the vulnerability, adjusted for PCI rules and exceptions, on a scale of 0-10.  # noqa: E501

        :param adjusted_severity_score: The adjusted_severity_score of this PCI.  # noqa: E501
        :type: int
        """

        self._adjusted_severity_score = adjusted_severity_score

    @property
    def fail(self):
        """Gets the fail of this PCI.  # noqa: E501

        Whether if present on a host this vulnerability would cause a PCI failure. `true` if \"status\" is `\"Fail\"`, `false` otherwise.  # noqa: E501

        :return: The fail of this PCI.  # noqa: E501
        :rtype: bool
        """
        return self._fail

    @fail.setter
    def fail(self, fail):
        """Sets the fail of this PCI.

        Whether if present on a host this vulnerability would cause a PCI failure. `true` if \"status\" is `\"Fail\"`, `false` otherwise.  # noqa: E501

        :param fail: The fail of this PCI.  # noqa: E501
        :type: bool
        """

        self._fail = fail

    @property
    def special_notes(self):
        """Gets the special_notes of this PCI.  # noqa: E501

        Any special notes or remarks about the vulnerability that pertain to PCI compliance.  # noqa: E501

        :return: The special_notes of this PCI.  # noqa: E501
        :rtype: str
        """
        return self._special_notes

    @special_notes.setter
    def special_notes(self, special_notes):
        """Sets the special_notes of this PCI.

        Any special notes or remarks about the vulnerability that pertain to PCI compliance.  # noqa: E501

        :param special_notes: The special_notes of this PCI.  # noqa: E501
        :type: str
        """

        self._special_notes = special_notes

    @property
    def status(self):
        """Gets the status of this PCI.  # noqa: E501

        The PCI compliance status of the vulnerability. One of: `\"Pass\"`, `\"Fail\"`.  # noqa: E501

        :return: The status of this PCI.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PCI.

        The PCI compliance status of the vulnerability. One of: `\"Pass\"`, `\"Fail\"`.  # noqa: E501

        :param status: The status of this PCI.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(PCI, dict):
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
        if not isinstance(other, PCI):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
