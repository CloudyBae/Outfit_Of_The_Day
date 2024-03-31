build-CoreLayer:
	python3.10 ./setup.py build
	pip3.10 wheel -w tmp -e
	mkdir $(ARTIFACTS_DIR)/python
	pip3.10 install tmp/core-* --target $(ARTIFACTS_DIR)/python/ 
