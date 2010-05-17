#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#

"""DB-related operations."""


__all__ = ['Put', 'Delete']


class Put(object):
  """Put entity into datastore via mutation_pool.

  See mapreduce.context.MutationPool.
  """

  def __init__(self, entity):
    """Constructor.

    Args:
      entity: an entity to put.
    """
    self.entity = entity

  def __call__(self, context):
    """Perform operation.

    Args:
      context: mapreduce context as context.Context.
    """
    context.mutation_pool.put(self.entity)


class Delete(object):
  """Delete entity from datastore via mutation_pool.

  See mapreduce.context.MutationPool.
  """

  def __init__(self, entity):
    """Constructor.

    Args:
      entity: an entity to delete.
    """
    self.entity = entity

  def __call__(self, context):
    """Perform operation.

    Args:
      context: mapreduce context as context.Context.
    """
    context.mutation_pool.delete(self.entity)
