# -*- coding: utf-8 -*-
"""Repository traffic stats logic."""
from __future__ import unicode_literals

from .. import models


class ViewsStats(models.GitHubCore):
    """The total number of repository views, per day or week, for the last 14
    days.

    See also https://developer.github.com/v3/repos/traffic/

    .. note::

        Timestamps are aligned to UTC midnight of the beginning of the day or
        week. Week begins on Monday.

    This object has the following attributes:

    .. attribute:: count

        The total number of views.

    .. attribute:: uniques

        The total number of unique views.

    .. attribute:: views

        A list of dictionaries containing daily or weekly statistical data.

    """

    def _update_attributes(self, stats_object):
        self.count = stats_object["count"]
        self.uniques = stats_object["uniques"]
        self.views = stats_object["views"]
        if self.views:
            for view in self.views:
                view["timestamp"] = self._strptime(view["timestamp"])

    def _repr(self):
        return ("<Views Statistics "
                "[{s.count}, {s.uniques} unique]>").format(s=self)
