SAM_TEMPLATE ?= template.yml
AWS_REGION ?= 'us-east-1'
DEPLOY_ENV ?= unknown
STACKNAME ?= 'ootd'

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
		--stack-name $(STACKNAME)
		--tags \
			DeploymentEnv=$(DEPLOY_ENV) \
			StackName=$(STACKNAME) \
		--parameter-overrides \
			ServiceEnv=$(DEPLOY_ENV) \
			ResourceEnv=$(RESOURCE_ENV) \
			StackName=$(STACKNAME) \
