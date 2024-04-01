build-CoreLayer:
    python3.10 ./setup.py build
    pip3.10 wheel -w tmp -e .
    mkdir $(ARTIFACTS_DIR)/python
    WHEEL_FILE := $(shell ls tmp/core-*.whl)
    pip3.10 install $(WHEEL_FILE) --target $(ARTIFACTS_DIR)/python/
