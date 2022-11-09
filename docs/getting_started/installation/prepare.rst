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

============
Preparation
============

This page shows you how to install PyFlink using pip, conda, installing from the source, etc.

Python Version Supported
------------------------

.. list-table::
   :widths: 25 50
   :header-rows: 1

   * - PyFlink Version
     - Python Version Supported
   * - PyFlink 1.16
     - Python 3.6 to 3.9
   * - PyFlink 1.15
     - Python 3.6 to 3.8
   * - PyFlink 1.14
     - Python 3.6 to 3.8

You could check your Python version as following:

.. code-block:: bash

    python3 --version


Create a Python virtual environment
-----------------------------------

Virtual environment gives you the ability to isolate the Python dependencies of different projects by creating a
separate environment for each project. It is a directory tree which contains its own Python executable files and the
installed Python packages.

It is useful for local development to create a standalone Python environment and also useful when deploying a PyFlink
job to production when there are massive Python dependencies. It's supported to use Python virtual environment in your PyFlink jobs,
see `PyFlink Dependency Management <https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/python/dependency_management/#archives>`_ for more details.


Create a virtual environment using virtualenv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To create a virtual environment using virtualenv, run:

.. code-block:: bash

    python3 -m pip install virtualenv

    # Create Python virtual environment under a directory, e.g. venv
    virtualenv venv

    # You can also create Python virtual environment with a specific Python version
    virtualenv --python /path/to/python/executable venv

The virtual environment needs to be activated before to use it. To activate the virtual environment, run:

.. code-block:: bash

    source venv/bin/activate

That is, execute the activate script under the bin directory of your virtual environment.


Create a virtual environment using conda
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To create a virtual environment using conda (suppose miniconda), run:

.. code-block:: bash

    # Download and install miniconda, the latest miniconda installers are available in https://repo.anaconda.com/miniconda/

    # Suppose the name of the downloaded miniconda installer is miniconda.sh
    chmod +x miniconda.sh
    # install miniconda
    ./miniconda.sh -b -p miniconda

    # Activate the miniconda environment
    source miniconda/bin/activate

    # Create conda virtual environment under a directory, e.g. venv
    conda create --name venv python=3.8 -y


The conda virtual environment needs to be activated before to use it. To activate the conda virtual environment, run:

.. code-block:: bash

    conda activate venv


Install PyFlink
---------------

You could then install the latest PyFlink package into your virtual environment. Note that the Flink version and PyFlink
version need to be consistent. For example, if you are using Flink 1.15, then you should use PyFlink 1.15

Installing using PyPI
~~~~~~~~~~~~~~~~~~~~~

PyFlink could be installed using `PyPI <https://pypi.org/project/apache-flink/>`_ as following:

.. code-block:: bash

    python3 -m pip install apache-flink


Installing using Conda
~~~~~~~~~~~~~~~~~~~~~~

PyFlink could be installed using Conda as following:

.. code-block:: bash

    python3 -m pip install apache-flink


Installing from Source
~~~~~~~~~~~~~~~~~~~~~~

To install PyFlink from source, you could refer to `Build PyFlink <https://nightlies.apache.org/flink/flink-docs-stable/docs/flinkdev/building/#build-pyflink>`_.


Check the installed package
---------------------------

You could then perform the following checks to make sure that the installed PyFlink package is ready for use:

.. code-block:: bash

    curl -L https://raw.githubusercontent.com/apache/flink/master/flink-python/pyflink/examples/table/word_count.py -o word_count.py
    python3 word_count.py
    # You will see outputs as following:
    # Use --input to specify file input.
    # Printing result to stdout. Use --output to specify output path.
    # +I[To, 1]
    # +I[be,, 1]
    # +I[or, 1]
    # +I[not, 1]
    # +I[to, 1]
    # +I[be,--that, 1]
    # ...

If there are any problems, you could perform the following checks.

Check the logging messages in the log file to see if there are any problems:

.. code-block:: bash

    # Get the installation directory of PyFlink
    python3 -c "import pyflink;import os;print(os.path.dirname(os.path.abspath(pyflink.__file__)))"
    # It will output a path like the following:
    # /path/to/python/site-packages/pyflink

    # Check the logging under the log directory
    ls -lh /path/to/python/site-packages/pyflink/log
    # You will see the log file as following:
    #  -rw-r--r--  1 dianfu  staff    45K 10 18 20:54 flink-dianfu-python-B-7174MD6R-1908.local.log

Besides, you could also check if the files of the PyFlink package are consistent.
It may happen that you have installed an old version of PyFlink before and multiple PyFlink versions exist at the
same time for some reason.

.. code-block:: bash

    # List the jar packages under the lib directory
    ls -lh /path/to/python/site-packages/pyflink/lib
    # It will output a list of jar packages as following:
    #  -rw-r--r--  1 dianfu  staff   190K 10 18 20:43 flink-cep-1.15.2.jar
    #  -rw-r--r--  1 dianfu  staff   475K 10 18 20:43 flink-connector-files-1.15.2.jar
    #  -rw-r--r--  1 dianfu  staff    93K 10 18 20:43 flink-csv-1.15.2.jar
    #  -rw-r--r--  1 dianfu  staff   110M 10 18 20:43 flink-dist-1.15.2.jar
    #  -rw-r--r--  1 dianfu  staff   171K 10 18 20:43 flink-json-1.15.2.jar
    #  -rw-r--r--  1 dianfu  staff    20M 10 18 20:43 flink-scala_2.12-1.15.2.jar
    #  -rw-r--r--  1 dianfu  staff    10M 10 18 20:43 flink-shaded-zookeeper-3.5.9.jar
    #  -rw-r--r--  1 dianfu  staff    15M 10 18 20:43 flink-table-api-java-uber-1.15.2.jar
    #  -rw-r--r--  1 dianfu  staff    35M 10 18 20:43 flink-table-planner-loader-1.15.2.jar
    #  -rw-r--r--  1 dianfu  staff   2.9M 10 18 20:43 flink-table-runtime-1.15.2.jar
    #  -rw-r--r--  1 dianfu  staff   203K 10 18 20:43 log4j-1.2-api-2.17.1.jar
    #  -rw-r--r--  1 dianfu  staff   295K 10 18 20:43 log4j-api-2.17.1.jar
    #  -rw-r--r--  1 dianfu  staff   1.7M 10 18 20:43 log4j-core-2.17.1.jar
    #  -rw-r--r--  1 dianfu  staff    24K 10 18 20:43 log4j-slf4j-impl-2.17.1.jar

Please make sure that the versions of all the Flink jar packages are consistent, e.g. 1.15.2 in the above example.
