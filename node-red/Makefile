GIT_COMMIT := $(shell git rev-parse --short HEAD)
GIT_SOURCE := $(shell git config --get remote.origin.url)
QUAY_REPO_USER := kaszpir
QUAY_REPO_NAME := node-red

help:
	@grep -E '(^[0-9a-zA-Z_-]+:.*?##.*$$)|(^##)' Makefile | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'

version: ## show git version
	@echo GIT_COMMIT IS $(GIT_COMMIT)

lint-dockerfile: ## Runs hadolint against application dockerfile
	docker run --rm -v "$(PWD):/data" -w "/data" hadolint/hadolint hadolint Dockerfile

docker_config: ## configure docker to allow multi-arch builds
	docker run --privileged --rm tonistiigi/binfmt --install all

nodered_amd64: ARCH=amd64
nodered_arm64: ARCH=arm64
nodered_amd64 nodered_arm64: ## build node-red amd or arm image
	docker buildx build --load \
		--platform=linux/${ARCH} \
		-t node-red:${GIT_COMMIT}-${ARCH} \
		--build-arg GIT_COMMIT=${GIT_COMMIT} \
		--build-arg GIT_SOURCE=${GIT_SOURCE} \
		-f Dockerfile .

nodered: ## build ml api images
	$(MAKE) nodered_amd64 nodered_arm64

list_images: ## list images if they were built
	@docker image ls | grep ${GIT_COMMIT}

clean: ## delete built images for current commit
	docker image ls | grep ${GIT_COMMIT} | awk '{print $$3}' | sort | uniq | xargs docker rmi -f || true

all: lint-dockerfile nodered list_images ## build all

quay_amd64: ARCH=amd64
quay_arm64: ARCH=arm64
quay_amd64 quay_arm64:
	$(MAKE) nodered_${ARCH}
	docker tag node-red:${GIT_COMMIT}-${ARCH} quay.io/${QUAY_REPO_USER}/${QUAY_REPO_NAME}:${GIT_COMMIT}-${ARCH}
	docker push quay.io/${QUAY_REPO_USER}/${QUAY_REPO_NAME}:${GIT_COMMIT}-${ARCH}

quay: ## build ml api images and push to quay.io
	$(MAKE) quay_amd64 quay_arm64


bake: ## run image builds with docker buildx, see docker-bake.hcl
	GIT_COMMIT=${GIT_COMMIT} GIT_SOURCE=${GIT_SOURCE} docker buildx bake

.DEFAULT_GOAL := help
.PHONY: help lint-dockerfile nodered_amd64 nodered_arm64 nodered list_images clean all bake
