# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from tests import BaseSessionTest

class TestKinesis(BaseSessionTest):
    def test_subscribe_to_shard_removed(self):
        kinesis = self.session.create_client('kinesis', 'us-west-2')
        try:
            kinesis.subscribe_to_shard
        except AttributeError:
            pass
        else:
            self.fail('subscribe_to_shard was available on the kinesis client')
