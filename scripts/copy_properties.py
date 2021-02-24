#!/usr/bin/env python
#
# Copyright (c) 2021 Cloudify Platform Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from cloudify import ctx
from cloudify.state import ctx_parameters as inputs


if __name__ == '__main__':
    ctx.logger.debug(
        'Executing copy_properties.py script. Source node instance '
        'runtime-properties: {}'.format(
            ctx.source.instance.runtime_properties
        )
    )

    for key in ctx.target.instance.runtime_properties:
        ctx.source.instance.runtime_properties['target_' + key] = \
            ctx.target.instance.runtime_properties[key]

    ctx.logger.debug(
        'Copied properties from target node instance to source node instance. '
        'New source node instance runtime-properties: {}'.format(
            ctx.source.instance.runtime_properties
        )
    )