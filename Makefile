build-html:
	git describe --abbrev=0 --tags | xargs -I % uv version %
	uv version --short > src/_version
	sphinx-build --write-all src html

create-dev:
	uv sync
