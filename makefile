# Makefile for running Advent of Code solutions
# Requires global nodemon installation
# Default values for day and problem

day ?= 1
problem ?= 1

# Target: run
# Usage: make run day=12 problem=1
run:
	@echo "Running solution for Day $(day), Problem $(problem)..."
	@nodemon -r . --ext py,txt --exec "PYTHONPATH=. DAY=${day} python3 day$(day)/solution$(problem).py"
