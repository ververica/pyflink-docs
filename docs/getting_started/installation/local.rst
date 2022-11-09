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
Local
=====

This page shows you how to set up PyFlink development environment in your local machine.
This is usually used for local execution or development in an IDE.


Set up Python environment
-------------------------

It requires Python 3.6 or above with PyFlink pre-installed to be available in your local environment.
It's suggested to use Python virtual environments to set up your local Python environment. See `Create a Python virtual environment <prepare.rst#create-a-python-virtual-environment>`_ for more details
on how to prepare Python virtual environments with PyFlink installed.


Execute PyFlink jobs in terminal
--------------------------------

You could execute PyFlink jobs locally as following:

.. code-block:: bash

    curl -L https://raw.githubusercontent.com/apache/flink/master/flink-python/pyflink/examples/table/word_count.py -o word_count.py
    python3 word_count.py

If there any any problems, you could check the logging messages in the log file as following:

.. code-block:: bash

    # Get the installation directory of PyFlink
    python3 -c "import pyflink;import os;print(os.path.dirname(os.path.abspath(pyflink.__file__)))"
    # It will output a path like the following:
    # /path/to/python/site-packages/pyflink

    # Check the logging under the log directory
    ls -lh /path/to/python/site-packages/pyflink/log
    # You will see the log file as following:
    #  -rw-r--r--  1 dianfu  staff    45K 10 18 20:54 flink-dianfu-python-B-7174MD6R-1908.local.log


Execute PyFlink jobs in IDE
---------------------------

You need firstly configure the Python virtual environment for your IDE. See `Configure a virtual environment <https://www.jetbrains.com/help/idea/creating-virtual-environment.html>`_
for more details on how to configure the Python virtual environment in IntelliJ IDEA.

Right click on the job file and execute it. If there are any problems, you could check the logging messages in the log
file which resides under the log directory of PyFlink installation directory as following:

.. code-block:: bash

    # Check the logging under the log directory of PyFlink
    ls -lh /path/to/python/site-packages/pyflink/log
