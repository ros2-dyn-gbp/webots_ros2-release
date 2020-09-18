#!/usr/bin/env python

# Copyright 1996-2019 Cyberbotics Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This module simply returns WEBOTS_HOME."""

import os


def get_webots_home():
    path = os.path.abspath(__file__)
    while os.path.basename(path) != 'lib':
        previousPath = path
        path = os.path.dirname(path)
        if previousPath == path:
            return None
    return os.path.join(os.path.dirname(path), 'share', 'webots_ros2_desktop', 'webots')
