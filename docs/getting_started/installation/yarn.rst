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

=====
YARN
=====

Apache Hadoop YARN is a cluster resource management framework for managing the resources and scheduling jobs in a
Hadoop cluster. It's supported to submit PyFlink jobs to YARN for execution.


Set up Python environment
-------------------------

It requires Python 3.6 or above with PyFlink pre-installed to be available on the nodes of the YARN cluster.
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

    ./bin/flink run-application -t yarn-application \
          -Djobmanager.memory.process.size=1024m \
          -Dtaskmanager.memory.process.size=1024m \
          -Dyarn.application.name=<ApplicationName> \
          -pyclientexec /path/to/venv/bin/python3 \
          -pyexec /path/to/venv/bin/python3 \
          -pyfs shipfiles \
          -pym word_count

In the above example, it assumes that there is already a Python virtual environment available at /path/to/venv on all
the cluster nodes. It should be noted that options **-pyclientexec** and **-pyexec** are also
required to specify to use the given Python virtual environment at client side (for job compiling) and server side
(for Python UDF execution) separately.

* Specify the Python virtual environments during submitting PyFlink jobs

It also supports to distribute the Python virtual environment during submitting PyFlink jobs. In this way,
the Python virtual environment will be distributed to the cluster nodes where PyFlink jobs are running on during job starting up.
This is more flexible and useful when it's not possible to set up the Python environments in advance on the cluster
nodes or when there are some special requirements where the pre-installed Python environments could not meet.

.. code-block:: bash

    ./bin/flink run-application -t yarn-application \
          -Djobmanager.memory.process.size=1024m \
          -Dtaskmanager.memory.process.size=1024m \
          -Dyarn.application.name=<ApplicationName> \
          -Dyarn.ship-files=/path/to/shipfiles \
          -pyarch shipfiles/venv.zip \
          -pyclientexec venv.zip/venv/bin/python3 \
          -pyexec venv.zip/venv/bin/python3 \
          -pyfs shipfiles \
          -pym word_count

In the above example, the Python virtual environment is specified via option **-pyarch**. It will be distributed to
the cluster nodes during job execution. It should be noted that options **-pyclientexec** and **-pyexec** are also
required to specify to use the given Python virtual environment at client side (for job compiling) and server side
(for Python UDF execution) separately.

.. note::
    It assumes that the Python dependencies needed to execute the job are already placed in the directory
    /path/to/shipfiles. For example, it should contain venv.zip and word_count.py for the above example.

    As it executes the job on the JobManager in YARN application mode, the paths specified in **-pyarch** and **-py**
    are paths relative to shipfiles which is the directory name of the shipped files.

    The archive files specified via **-pyarch** will be distributed to the TaskManagers through blob server where the file
    size limit is 2 GB. If the size of an archive file is more than 2 GB, you could upload it to a distributed file
    system and then use the path in the command line option **-pyarch**.

* Mix use of the above options

You could also mix use of the above options, that is, pre-install a few commonly used Python virtual environments on the
cluster nodes and use custom Python virtual environment when there are some special requirements.


Submit PyFlink jobs to YARN cluster
-----------------------------------

It supports to execute PyFlink jobs in application mode, per-job mode and session mode in YARN deployment.

You could execute PyFlink jobs in application mode as following:

.. code-block:: bash

    ./bin/flink run-application -t yarn-application \
          -Djobmanager.memory.process.size=1024m \
          -Dtaskmanager.memory.process.size=1024m \
          -Dyarn.application.name=<ApplicationName> \
          -Dyarn.ship-files=/path/to/shipfiles \
          -pyarch shipfiles/venv.zip \
          -pyclientexec venv.zip/venv/bin/python3 \
          -pyexec venv.zip/venv/bin/python3 \
          -pyfs shipfiles \
          -pym word_count

You could execute PyFlink jobs in per-job mode as following:

.. code-block:: bash

    ./bin/flink run -t yarn-per-job \
          -Djobmanager.memory.process.size=1024m \
          -Dtaskmanager.memory.process.size=1024m \
          -Dyarn.application.name=<ApplicationName> \
          -Dyarn.ship-files=/path/to/shipfiles \
          -pyarch shipfiles/venv.zip \
          -pyclientexec /path/to/venv/bin/python3 \
          -pyexec venv.zip/venv/bin/python3 \
          -pyfs /path/to/shipfiles \
          -pym word_count

.. note::
    Per-Job mode has been deprecated since Flink 1.15 and may be dropped in the future releases. It's suggested to use
    Application mode. See `YARN Per-Job Mode <https://nightlies.apache.org/flink/flink-docs-stable/docs/deployment/resource-providers/yarn/#per-job-mode-deprecated>`_ for more details.

    It should be noted that there are some differences compared with the application mode. For option **-pyclientexec**,
    it should point to a path on the client node (node executing the above command) as the job is compiled at the client
    side in per-job mode. If it's not specified, it will use the Python environment of the current shell environment.

You could also execute PyFlink jobs in session mode as following:

.. code-block:: bash

    ./bin/flink run -t yarn-session \
              -Djobmanager.memory.process.size=1024m \
              -Dtaskmanager.memory.process.size=1024m \
              -Dyarn.application.id=<application_XXXX_YY> \
              -Dyarn.ship-files=/path/to/shipfiles \
              -pyarch shipfiles/venv.zip \
              -pyclientexec /path/to/venv/bin/python3 \
              -pyexec venv.zip/venv/bin/python3 \
              -pyfs /path/to/shipfiles \
              -pym word_count

See `Session Mode <https://nightlies.apache.org/flink/flink-docs-stable/docs/deployment/resource-providers/yarn/#session-mode>`_ for more details.

.. note::
    Same as the per-job mode, the option **-pyclientexec** should point to a path on the client node
    (node executing the above command) as the job is compiled at the client side in per-job mode.
    If it's not specified, it will use the Python environment of the current shell environment.
