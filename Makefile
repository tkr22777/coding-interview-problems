.PHONY:

javac-java:
	javac ${FILENAME}.java; java ${FILENAME}; rm ${FILENAME}.class
