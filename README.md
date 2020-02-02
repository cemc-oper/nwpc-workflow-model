# nwpc-workflow-model

[![Build Status](https://travis-ci.org/perillaroc/nwpc-workflow-model.svg?branch=master)](https://travis-ci.org/perillaroc/nwpc-workflow-model)
[![codecov](https://codecov.io/gh/perillaroc/nwpc-workflow-model/branch/master/graph/badge.svg)](https://codecov.io/gh/perillaroc/nwpc-workflow-model)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/de25858ec56640bc96aad839e0af83e3)](https://www.codacy.com/app/perillaroc/nwpc-workflow-model?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=perillaroc/nwpc-workflow-model&amp;utm_campaign=Badge_Grade)

The workflow model using in NWPC, supports SMS and ecFlow.

## Introduction

In NWPC, we run tasks using a workflow software, such as SMS and ecFLow by ECMWF.
`nwpc-workflow-model` is designed to bring a workflow model into our programs.

## Components

### SMS
 
Please see [nwpc_workflow_model/sms/README.md](nwpc_workflow_model/sms/README.md) for more information.

### ecFlow

Same as SMS.

## Getting Started

Download the latest source code from Github and install `nwpc-workflow-model` using:

```bash
python setup.py install
```

## Tests

Install packages for test using `pip install .[test]`.

Use `pytest` to run tests.

## License

Copyright &copy; 2016-2020, perillaroc at nwpc-oper.

`nwpc-workflow-model` is licensed under [The MIT License](https://opensource.org/licenses/MIT).
