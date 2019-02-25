#!/bin/bash
.PHONY: default
.SILENT:


default:

start_flask:
	docker run -p 5000:5000 flask:latest

build_flask:
	docker build -t flask:latest .