PyFlink Docs
=================================
PyFlink is a Python API for Apache Flink that allows you to build scalable batch and streaming workloads,
such as real-time data processing pipelines, large-scale exploratory data analysis, Machine Learning (ML) pipelines and ETL processes.
If you’re already familiar with Python and libraries such as Pandas, then PyFlink makes it simpler to leverage the full capabilities of the Flink ecosystem.
Depending on the level of abstraction you need, there are two different APIs that can be used in PyFlink: PyFlink Table API and PyFlink DataStream API.

How to build docs locally
---------------------------------

1. Install dependency requirements

``python3 -m pip install -r dev/requirements.txt``

2. Conda install pandoc 

``conda install pandoc``

3. Build the docs

``python3 setup.py build_sphinx``

4. Open the ``pyflink-docs/build/sphinx/html/index.html`` in the Browser
