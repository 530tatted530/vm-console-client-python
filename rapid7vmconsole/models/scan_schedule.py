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

from rapid7vmconsole.models.link import Link  # noqa: F401,E501
from rapid7vmconsole.models.repeat import Repeat  # noqa: F401,E501
from rapid7vmconsole.models.scheduled_scan_targets import ScheduledScanTargets  # noqa: F401,E501


class ScanSchedule(object):
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
        'assets': 'ScheduledScanTargets',
        'duration': 'str',
        'enabled': 'bool',
        'id': 'int',
        'links': 'list[Link]',
        'next_runtimes': 'list[str]',
        'on_scan_repeat': 'str',
        'repeat': 'Repeat',
        'scan_engine_id': 'int',
        'scan_name': 'str',
        'scan_template_id': 'str',
        'start': 'str'
    }

    attribute_map = {
        'assets': 'assets',
        'duration': 'duration',
        'enabled': 'enabled',
        'id': 'id',
        'links': 'links',
        'next_runtimes': 'nextRuntimes',
        'on_scan_repeat': 'onScanRepeat',
        'repeat': 'repeat',
        'scan_engine_id': 'scanEngineId',
        'scan_name': 'scanName',
        'scan_template_id': 'scanTemplateId',
        'start': 'start'
    }

    def __init__(self, assets=None, duration=None, enabled=None, id=None, links=None, next_runtimes=None, on_scan_repeat=None, repeat=None, scan_engine_id=None, scan_name=None, scan_template_id=None, start=None):  # noqa: E501
        """ScanSchedule - a model defined in Swagger"""  # noqa: E501

        self._assets = None
        self._duration = None
        self._enabled = None
        self._id = None
        self._links = None
        self._next_runtimes = None
        self._on_scan_repeat = None
        self._repeat = None
        self._scan_engine_id = None
        self._scan_name = None
        self._scan_template_id = None
        self._start = None
        self.discriminator = None

        if assets is not None:
            self.assets = assets
        if duration is not None:
            self.duration = duration
        self.enabled = enabled
        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if next_runtimes is not None:
            self.next_runtimes = next_runtimes
        self.on_scan_repeat = on_scan_repeat
        if repeat is not None:
            self.repeat = repeat
        if scan_engine_id is not None:
            self.scan_engine_id = scan_engine_id
        if scan_name is not None:
            self.scan_name = scan_name
        if scan_template_id is not None:
            self.scan_template_id = scan_template_id
        self.start = start

    @property
    def assets(self):
        """Gets the assets of this ScanSchedule.  # noqa: E501

        Allows one or more assets defined within the site to be scanned for this scan schedule. This property is only supported for static sites. When this property is `null`, or not defined in schedule, then all assets defined in the static site will be scanned.  # noqa: E501

        :return: The assets of this ScanSchedule.  # noqa: E501
        :rtype: ScheduledScanTargets
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this ScanSchedule.

        Allows one or more assets defined within the site to be scanned for this scan schedule. This property is only supported for static sites. When this property is `null`, or not defined in schedule, then all assets defined in the static site will be scanned.  # noqa: E501

        :param assets: The assets of this ScanSchedule.  # noqa: E501
        :type: ScheduledScanTargets
        """

        self._assets = assets

    @property
    def duration(self):
        """Gets the duration of this ScanSchedule.  # noqa: E501

        Specifies the maximum duration the scheduled scan is allowed to run. Scheduled scans that do not complete within specified duration will be paused. The scan duration are represented by the format `\"P[n]DT[n]H[n]M\"`. In these representations, the [n] is replaced by a value for each of the date and time elements that follow the [n].The following table describes each supported value:  | Value | Description |  | ---------- | ---------------- |  | P | The duration designator. It must be placed at the start of the duration representation. |  | D | The day designator that follows the value for the number of days. |  | T | The time designator that precedes the time portion of the representation. |  | H | The hour designator that follows the value for the number of hours. |  | M | The minute designator that follows the value for the number of minutes. |  For example, `\"P5DT10H30M\"` represents a duration of \"5 days, 10 hours, and 30 minutes\". Each duration designator is optional; however, at least one must be specified and it must be preceded by the `\"P\"` designator.    # noqa: E501

        :return: The duration of this ScanSchedule.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ScanSchedule.

        Specifies the maximum duration the scheduled scan is allowed to run. Scheduled scans that do not complete within specified duration will be paused. The scan duration are represented by the format `\"P[n]DT[n]H[n]M\"`. In these representations, the [n] is replaced by a value for each of the date and time elements that follow the [n].The following table describes each supported value:  | Value | Description |  | ---------- | ---------------- |  | P | The duration designator. It must be placed at the start of the duration representation. |  | D | The day designator that follows the value for the number of days. |  | T | The time designator that precedes the time portion of the representation. |  | H | The hour designator that follows the value for the number of hours. |  | M | The minute designator that follows the value for the number of minutes. |  For example, `\"P5DT10H30M\"` represents a duration of \"5 days, 10 hours, and 30 minutes\". Each duration designator is optional; however, at least one must be specified and it must be preceded by the `\"P\"` designator.    # noqa: E501

        :param duration: The duration of this ScanSchedule.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def enabled(self):
        """Gets the enabled of this ScanSchedule.  # noqa: E501

        Flag indicating whether the scan schedule is enabled.  # noqa: E501

        :return: The enabled of this ScanSchedule.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ScanSchedule.

        Flag indicating whether the scan schedule is enabled.  # noqa: E501

        :param enabled: The enabled of this ScanSchedule.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this ScanSchedule.  # noqa: E501

        The identifier of the scan schedule.  # noqa: E501

        :return: The id of this ScanSchedule.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScanSchedule.

        The identifier of the scan schedule.  # noqa: E501

        :param id: The id of this ScanSchedule.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def links(self):
        """Gets the links of this ScanSchedule.  # noqa: E501


        :return: The links of this ScanSchedule.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ScanSchedule.


        :param links: The links of this ScanSchedule.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def next_runtimes(self):
        """Gets the next_runtimes of this ScanSchedule.  # noqa: E501

        List the next 10 dates in the future the schedule will launch.   # noqa: E501

        :return: The next_runtimes of this ScanSchedule.  # noqa: E501
        :rtype: list[str]
        """
        return self._next_runtimes

    @next_runtimes.setter
    def next_runtimes(self, next_runtimes):
        """Sets the next_runtimes of this ScanSchedule.

        List the next 10 dates in the future the schedule will launch.   # noqa: E501

        :param next_runtimes: The next_runtimes of this ScanSchedule.  # noqa: E501
        :type: list[str]
        """

        self._next_runtimes = next_runtimes

    @property
    def on_scan_repeat(self):
        """Gets the on_scan_repeat of this ScanSchedule.  # noqa: E501

        Specifies the desired behavior of a repeating scheduled scan when the previous scan was paused due to reaching is maximum duration. The following table describes each supported value:  | Value | Description |  | ---------- | ---------------- |  | restart-scan | Stops the previously-paused scan and launches a new scan if the previous scan did not complete within the specified duration. If the previous scheduled scan was not paused, then a new scan is launched. |  | resume-scan | Resumes the previously-paused scan if the previous scan did not complete within the specified duration. If the previous scheduled scan was not paused, then a new scan is launched. |    # noqa: E501

        :return: The on_scan_repeat of this ScanSchedule.  # noqa: E501
        :rtype: str
        """
        return self._on_scan_repeat

    @on_scan_repeat.setter
    def on_scan_repeat(self, on_scan_repeat):
        """Sets the on_scan_repeat of this ScanSchedule.

        Specifies the desired behavior of a repeating scheduled scan when the previous scan was paused due to reaching is maximum duration. The following table describes each supported value:  | Value | Description |  | ---------- | ---------------- |  | restart-scan | Stops the previously-paused scan and launches a new scan if the previous scan did not complete within the specified duration. If the previous scheduled scan was not paused, then a new scan is launched. |  | resume-scan | Resumes the previously-paused scan if the previous scan did not complete within the specified duration. If the previous scheduled scan was not paused, then a new scan is launched. |    # noqa: E501

        :param on_scan_repeat: The on_scan_repeat of this ScanSchedule.  # noqa: E501
        :type: str
        """
        if on_scan_repeat is None:
            raise ValueError("Invalid value for `on_scan_repeat`, must not be `None`")  # noqa: E501

        self._on_scan_repeat = on_scan_repeat

    @property
    def repeat(self):
        """Gets the repeat of this ScanSchedule.  # noqa: E501

        Settings for repeating a scheduled scan.  # noqa: E501

        :return: The repeat of this ScanSchedule.  # noqa: E501
        :rtype: Repeat
        """
        return self._repeat

    @repeat.setter
    def repeat(self, repeat):
        """Sets the repeat of this ScanSchedule.

        Settings for repeating a scheduled scan.  # noqa: E501

        :param repeat: The repeat of this ScanSchedule.  # noqa: E501
        :type: Repeat
        """

        self._repeat = repeat

    @property
    def scan_engine_id(self):
        """Gets the scan_engine_id of this ScanSchedule.  # noqa: E501

        The identifier of the scan engine to be used for this scan schedule. If not set, the site's assigned scan engine will be used.  # noqa: E501

        :return: The scan_engine_id of this ScanSchedule.  # noqa: E501
        :rtype: int
        """
        return self._scan_engine_id

    @scan_engine_id.setter
    def scan_engine_id(self, scan_engine_id):
        """Sets the scan_engine_id of this ScanSchedule.

        The identifier of the scan engine to be used for this scan schedule. If not set, the site's assigned scan engine will be used.  # noqa: E501

        :param scan_engine_id: The scan_engine_id of this ScanSchedule.  # noqa: E501
        :type: int
        """

        self._scan_engine_id = scan_engine_id

    @property
    def scan_name(self):
        """Gets the scan_name of this ScanSchedule.  # noqa: E501

        A user-defined name for the scan launched by the schedule. If not explicitly set in the schedule, the scan name will be generated prior to the scan launching. Scan names must be unique within the site's scan schedules.  # noqa: E501

        :return: The scan_name of this ScanSchedule.  # noqa: E501
        :rtype: str
        """
        return self._scan_name

    @scan_name.setter
    def scan_name(self, scan_name):
        """Sets the scan_name of this ScanSchedule.

        A user-defined name for the scan launched by the schedule. If not explicitly set in the schedule, the scan name will be generated prior to the scan launching. Scan names must be unique within the site's scan schedules.  # noqa: E501

        :param scan_name: The scan_name of this ScanSchedule.  # noqa: E501
        :type: str
        """

        self._scan_name = scan_name

    @property
    def scan_template_id(self):
        """Gets the scan_template_id of this ScanSchedule.  # noqa: E501

        The identifier of the scan template to be used for this scan schedule. If not set, the site's assigned scan template will be used.  # noqa: E501

        :return: The scan_template_id of this ScanSchedule.  # noqa: E501
        :rtype: str
        """
        return self._scan_template_id

    @scan_template_id.setter
    def scan_template_id(self, scan_template_id):
        """Sets the scan_template_id of this ScanSchedule.

        The identifier of the scan template to be used for this scan schedule. If not set, the site's assigned scan template will be used.  # noqa: E501

        :param scan_template_id: The scan_template_id of this ScanSchedule.  # noqa: E501
        :type: str
        """

        self._scan_template_id = scan_template_id

    @property
    def start(self):
        """Gets the start of this ScanSchedule.  # noqa: E501

        The scheduled start date and time. Date is represented in ISO 8601 format. Repeating schedules will determine the next schedule to begin based on this date and time.  # noqa: E501

        :return: The start of this ScanSchedule.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ScanSchedule.

        The scheduled start date and time. Date is represented in ISO 8601 format. Repeating schedules will determine the next schedule to begin based on this date and time.  # noqa: E501

        :param start: The start of this ScanSchedule.  # noqa: E501
        :type: str
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

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
        if issubclass(ScanSchedule, dict):
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
        if not isinstance(other, ScanSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
