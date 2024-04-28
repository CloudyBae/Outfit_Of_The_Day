SAM_TEMPLATE ?= template.yml

validate:
	@sam validate --lint

build:
	sam build --use-container --parallel --template $(SAM_TEMPLATE)
