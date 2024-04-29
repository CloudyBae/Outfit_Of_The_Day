SAM_TEMPLATE ?= template.yml
AWS_REGION ?= 'us-east-1'
DEPLOY_ENV ?= unknown
STACK_NAME ?= 'ootd'

validate:
	@sam validate --lint

build:
	sam build --use-container --parallel --template template.yml

deploy:
	sam deploy \
		--region $(AWS_REGION) \
		--resolve-s3 \
		--no-fail-on-empty-changeset \
		--template-file $(SAM_TEMPLATE)
		--stack-name $(STACK_NAME) \
		--tags \
			DeploymentEnv=$(DEPLOY_ENV) \
			StackName=$(STACK_NAME) \
		--parameter-overrides \
			ServiceEnv=$(DEPLOY_ENV) \
			ResourceEnv=$(RESOURCE_ENV) \
			StackName=$(STACK_NAME) \
