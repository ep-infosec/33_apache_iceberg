# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from .pending_update import PendingUpdate


class DeleteFiles(PendingUpdate):

    def delete_files(self, path=None, datafile=None):
        if datafile is not None:
            path = datafile.path

        self._delete_from_path(path)
        return self

    def _delete_from_path(self):
        raise NotImplementedError()

    def delete_from_row_filter(self, expr):
        raise NotImplementedError()
