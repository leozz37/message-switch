# Texugo

[![CodeFactor](https://www.codefactor.io/repository/github/leozz37/texugo/badge)](https://www.codefactor.io/repository/github/leozz37/texugo)
[![Build Status](https://travis-ci.com/leozz37/texugo.svg?branch=master)](https://travis-ci.com/leozz37/texugo)
[![Build status](https://ci.appveyor.com/api/projects/status/qqp2al1e827jx70m?svg=true)](https://ci.appveyor.com/project/leozz37/texugo)
[![Coverage Status](https://coveralls.io/repos/github/leozz37/texugo/badge.svg?branch=master)](https://coveralls.io/github/leozz37/texugo?branch=master)
[![Documentation](https://codedocs.xyz/leozz37/texugo.svg)](https://codedocs.xyz/leozz37/texugo/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Texugo is a flexible multiplatform server message switch and gateway using Modern C++ based on Boost Asio and MQ.

## Features

- End-to-end system that process messages, supporting [RabbitMQ](https://www.rabbitmq.com/) and [Boost.ASIO](https://www.boost.org/doc/libs/1_66_0/doc/html/boost_asio.html);
- Flexible port binding;
- Reliably serve devices across multiple networks;
- TODO: Storing messages and logs on [MongoDB](https://www.mongodb.com/) (or [MongoDB Atlas](https://www.mongodb.com/cloud/atlas));
- Logging support with [spdlog](https://github.com/gabime/spdlog);
- TODO: Metrics monitoring with [Prometheus](https://prometheus.io/);
- TODO: Data visualization with [Grafana](https://grafana.com/);
- Support to build and run the binary on [Docker](https://www.docker.com/);
- Support to docker-compose to run all the services dependencies;

## Installation

Follow these steps:

### Clone this repository

`$ git clone https://github.com/leozz37/texugo.git`

### Create a build directory and build binary

`$ mkdir build && cd build`

`$ cmake .. && make`

## Server Configs

You can change the default route settings by changing the _routingAddresses_ array on the resources/settings.json file.

```settings.json

"routingAddresses": [
    {
      "AAAAAAA": "3000"
    },
    {
      "BBBBBBB": "3001"
    },
    {
      "CCCCCCC": "3002"
    },
    {
      "DDDDDDD": "3003"
    },
    {
      "EEEEEEE": "3004"
    }
  ]
```
