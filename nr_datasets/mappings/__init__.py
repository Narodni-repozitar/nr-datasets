# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# My site is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Mappings.

Mappings define how nr_datasets and their fields will be indexed in Elasticsearch.
The provided nusl-common-v1.0.0.json file is an example of how to index nr_datasets
in Elasticsearch. You need to provide one mapping per major version of
Elasticsearch you want to support.
"""

from __future__ import absolute_import, print_function
