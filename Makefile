validate:
	@sam validate --lint

build:
	sam build --use-container --parallel --template template.yml
