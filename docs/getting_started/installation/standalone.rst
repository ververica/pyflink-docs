..  Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

..    http://www.apache.org/licenses/LICENSE-2.0

..  Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.

==========
Standalone
==========

The standalone mode is the most barebone way of deploying Flink. This page shows you how to set up Python environment
and execute PyFlink jobs in a standalone Flink cluster.

Set up Python environment
-------------------------

It requires Python 3.6 or above with PyFlink pre-installed to be available on the nodes of the standalone cluster.
It's suggested to use Python virtual environments to set up the Python environment.
See `Create a Python virtual environment <prepare.rst#create-a-python-virtual-environment>`_ for more details on how
to prepare Python virtual environments with PyFlink installed.

Once the Python virtual environment is available, it needs to be deployed on the cluster. There are the following
options to deploy it:

* Install Python virtual environments on all the cluster nodes in advance

You could install Python virtual environments on all the cluster nodes with PyFlink pre-installed before submitting
PyFlink jobs. Note that if you have a lot of jobs which use different Python versions and Flink versions, you could
create multiple Python virtual environments to isolate them. For each PyFlink job, it could choose one of these Python
virtual environments to use.

.. code-block:: bash

    ./bin/flink run \
          --jobmanager <jobmanagerHost>:8081 \
          -pyclientexec /path/to/venv/bin/python3 \
          -pyexec /path/to/venv/bin/python3 \
          -py word_count.py

In the above example, it assumes that there is already a Python virtual environment available at /path/to/venv on all
the cluster nodes of the standaone cluster. It should be noted that options **-pyclientexec** and **-pyexec** are also
required to specify to use the given Python virtual environment at client side (for job compiling) and server side
(for Python UDF execution) separately.

* Specify the Python virtual environments during submitting PyFlink jobs

It also supports to distribute the Python virtual environment during submitting PyFlink jobs. In this way,
the Python virtual environment will be distributed to the cluster nodes where PyFlink jobs are running on during job starting up.
This is more flexible and useful when it's not possible to set up the Python environments in advance on the cluster
nodes or when there are some special requirements where the pre-installed Python environments could not meet.

.. code-block:: bash

    ./bin/flink run \
          --jobmanager <jobmanagerHost>:8081 \
          -pyarch /path/to/venv.zip \
          -pyclientexec /path/to/venv/bin/python3 \
          -pyexec venv.zip/venv/bin/python3 \
          -py word_count.py

In the above example, the Python virtual environment is specified via option **-pyarch**. It will be distributed to
the cluster nodes during job execution. It should be noted that option **-pyexec** is also
required to specify the Python virtual environment to use at server side (for Python UDF execution).

For the Python virtual environment at client side (for job compiling), option **-pyclientexec** could be used. If it's
not specified, it will use the Python environment of the current shell.


* Mix use of the above options

You could also mix use of the above options, that is, pre-install a few commonly used Python virtual environments on the
cluster nodes of the standalone cluster and use custom Python virtual environment when there are some special requirements.


Submit PyFlink jobs to a standalone Flink cluster
-------------------------------------------------

You could submit PyFlink jobs to a standalone Flink cluster as following:

.. code-block:: bash

    ./bin/flink run \
              --jobmanager <jobmanagerHost>:8081 \
              -pyarch /path/to/venv.zip \
              -pyexec venv.zip/venv/bin/python3 \
              -py word_count.py

See `Submitting PyFlink jobs <https://nightlies.apache.org/flink/flink-docs-stable/docs/deployment/cli/#submitting-pyflink-jobs>`_ for more details.
