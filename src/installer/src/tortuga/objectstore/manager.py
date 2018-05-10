# Copyright 2008-2018 Univa Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from redis import Redis

from .base import ObjectStore
from .redis import RedisObjectStore


class ObjectStoreManager:
    """
    Object store manager

    """
    _redis_client: Redis = None

    @classmethod
    def get(cls, namespace: str) -> ObjectStore:
        """
        Get an object store for a specified namespace.

        :param str namespace: the namespace for the object store
        :return ObjectStore:  the object store instance

        """
        if not cls._redis_client:
            cls._redis_client = Redis()
        return RedisObjectStore(namespace=namespace,
                                redis_client=cls._redis_client)
