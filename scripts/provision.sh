#!/usr/bin/env bash

which python3 || {
    apt-get update
    apt-get install -y python3
}
