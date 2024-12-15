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

# Target: create
# Usage: make create day=12
create:
	@echo "Creating Day $(day) solution..."
	@mkdir -p day$(day)  # Create a directory for the new day
	@cp _template/solution1.py day$(day)/solution1.py  # Copy the template Python file
	@cp _template/solution2.py day$(day)/solution2.py  # Copy the template Python file
	@cp _template/input_1.txt day$(day)/input_1.txt  # Copy the template input files
	@cp _template/input_0.txt day$(day)/input_0.txt
	@sed -i '' 's/day\/X/day\/$(day)/g' day$(day)/solution1.py  # Update solution1.py comment
	@sed -i '' 's/day\/X/day\/$(day)/g' day$(day)/solution2.py  # Update solution2.py comment
	@echo "day $(day) folder created successfully"