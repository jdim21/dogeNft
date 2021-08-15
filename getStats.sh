#!/bin/bash

echo "Number of max attribute rolls: "
ls images | grep -v _ | wc | awk '{print $1}'

echo "Number of single attribute rolls: "
ls images/*.?*_*_*_*_* | wc | awk '{print $1}'

echo "Number of zero attribute rolls: "
ls images/*.?_____.* | wc | awk '{print $1}'
