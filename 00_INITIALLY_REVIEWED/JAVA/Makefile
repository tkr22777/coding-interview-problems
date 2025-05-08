# Java Compilation Makefile
# ------------------------------------------------------------
# Usage:
#   Compile and run a Java class:
#   make run CLASS=DecodeString
# ------------------------------------------------------------

.PHONY: run

# Main target to compile and run a Java file
run:
	@if [ -z "$(CLASS)" ]; then \
		echo "Usage: make run CLASS=YourJavaClassName"; \
		echo "Example: make run CLASS=DecodeString"; \
	else \
		if [ -f "$(CLASS).java" ]; then \
			javac $(CLASS).java && java $(CLASS) && rm -f *.class; \
		else \
			echo "Error: $(CLASS).java not found"; \
		fi \
	fi