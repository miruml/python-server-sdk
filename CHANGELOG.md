# Changelog

## 0.6.2 (2025-11-12)

Full Changelog: [v0.6.1...v0.6.2](https://github.com/miruml/python-server-sdk/compare/v0.6.1...v0.6.2)

### Bug Fixes

* **client:** close streams without requiring full consumption ([c50bca7](https://github.com/miruml/python-server-sdk/commit/c50bca723dc9398bf97d9db9d881f8090b9deef0))
* compat with Python 3.14 ([6e10abe](https://github.com/miruml/python-server-sdk/commit/6e10abeb80e20e1d64eb9e1d251bd2d426ed62ad))


### Chores

* **internal/tests:** avoid race condition with implicit client cleanup ([445023e](https://github.com/miruml/python-server-sdk/commit/445023e773a89e857f47d1ca9fb61f0c1f6fde7b))
* **internal:** grammar fix (it's -&gt; its) ([5c82d3a](https://github.com/miruml/python-server-sdk/commit/5c82d3a7b9f90620c68e850441cbd204d475e8d0))
* **package:** drop Python 3.8 support ([80b7c35](https://github.com/miruml/python-server-sdk/commit/80b7c35b8dbe72ecf05cca08217b934eb8bef3a5))

## 0.6.1 (2025-10-21)

Full Changelog: [v0.6.0...v0.6.1](https://github.com/miruml/python-server-sdk/compare/v0.6.0...v0.6.1)

### Bug Fixes

* stainless config to have 'webhooks' parameter ([ec481f9](https://github.com/miruml/python-server-sdk/commit/ec481f97b1f760d96690958db51cf6fb39ebb3a0))


### Refactors

* **api:** remove 'config_schemas' expansion on config types ([bb3bc05](https://github.com/miruml/python-server-sdk/commit/bb3bc05defb45180a838c0e6f91d42f7669e0f7f))

## 0.6.0 (2025-10-21)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/miruml/python-server-sdk/compare/v0.5.0...v0.6.0)

### Features

* **api:** manual updates ([1f24c3f](https://github.com/miruml/python-server-sdk/commit/1f24c3f238e13344e158a909a8444fe6a02534ec))
* **api:** manual updates ([616466d](https://github.com/miruml/python-server-sdk/commit/616466d196871cb65ad48ecccf292be3596043b1))
* **api:** uat environment ([67e2b55](https://github.com/miruml/python-server-sdk/commit/67e2b5530fadfbd61d67e85d4fc5b4c363558fd9))
* **api:** update to v0.1.0 ([af3571c](https://github.com/miruml/python-server-sdk/commit/af3571c82e8ef891ca6c891cb4361e342a2f8fec))


### Bug Fixes

* **api:** expansions to use bracket format ([0344365](https://github.com/miruml/python-server-sdk/commit/03443654ab20a279be8594224358a15b746cfd01))
* **api:** restore webhook event models ([3e556df](https://github.com/miruml/python-server-sdk/commit/3e556dfa6728fd8a0e6e2206b6d5e38200f8325e))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([c54533f](https://github.com/miruml/python-server-sdk/commit/c54533f4c9d33df7720a786ef80f275d7bfd2e83))
* **internal:** detect missing future annotations with ruff ([ea21d88](https://github.com/miruml/python-server-sdk/commit/ea21d88960b9babe76a058adc0446205f909317f))
* update SDK settings ([e7bd9a6](https://github.com/miruml/python-server-sdk/commit/e7bd9a6b432ceeb9e9746577c0588bc3d8d6d81c))
* update SDK settings ([e6ec403](https://github.com/miruml/python-server-sdk/commit/e6ec4031305e950d8f61d18a55344de0e36f752b))


### Documentation

* update docs ([c152552](https://github.com/miruml/python-server-sdk/commit/c15255242bb7a5051d8618682afd0b981fe32396))


### Styles

* alphabetize webhook imports ([944a3ef](https://github.com/miruml/python-server-sdk/commit/944a3ef1b90d1efcff434ad218237107fb216a56))


### Refactors

* **api:** rename miru-server to miru ([163c465](https://github.com/miruml/python-server-sdk/commit/163c4659c64f6b954d9b91e7b340554f0919efa6))
* **api:** revert package name to miru_server_sdk ([0c8b7d7](https://github.com/miruml/python-server-sdk/commit/0c8b7d74ae67df4005fc069c4575ffae78b975c6))
* webhook payload to be type 'Any' instead of 'string' ([d0f5bdf](https://github.com/miruml/python-server-sdk/commit/d0f5bdf96c37812e15ddba85ce45e898491546ae))

## 0.5.0 (2025-10-07)

Full Changelog: [v0.4.1...v0.5.0](https://github.com/miruml/python-server-sdk/compare/v0.4.1...v0.5.0)

### Features

* **api:** uat environment ([67e2b55](https://github.com/miruml/python-server-sdk/commit/67e2b5530fadfbd61d67e85d4fc5b4c363558fd9))

## 0.4.1 (2025-10-05)

Full Changelog: [v0.4.1-beta.3...v0.4.1](https://github.com/miruml/python-server-sdk/compare/v0.4.1-beta.3...v0.4.1)

### Documentation

* update docs ([c152552](https://github.com/miruml/python-server-sdk/commit/c15255242bb7a5051d8618682afd0b981fe32396))

## 0.4.1-beta.3 (2025-10-05)

Full Changelog: [v0.4.1-beta.2...v0.4.1-beta.3](https://github.com/miruml/python-server-sdk/compare/v0.4.1-beta.2...v0.4.1-beta.3)

### Bug Fixes

* **api:** expansions to use bracket format ([0344365](https://github.com/miruml/python-server-sdk/commit/03443654ab20a279be8594224358a15b746cfd01))

## 0.4.1-beta.2 (2025-10-05)

Full Changelog: [v0.4.1-beta.1...v0.4.1-beta.2](https://github.com/miruml/python-server-sdk/compare/v0.4.1-beta.1...v0.4.1-beta.2)

### Styles

* alphabetize webhook imports ([944a3ef](https://github.com/miruml/python-server-sdk/commit/944a3ef1b90d1efcff434ad218237107fb216a56))


### Refactors

* webhook payload to be type 'Any' instead of 'string' ([d0f5bdf](https://github.com/miruml/python-server-sdk/commit/d0f5bdf96c37812e15ddba85ce45e898491546ae))

## 0.4.1-beta.1 (2025-10-05)

Full Changelog: [v0.4.1-beta.0...v0.4.1-beta.1](https://github.com/miruml/python-server-sdk/compare/v0.4.1-beta.0...v0.4.1-beta.1)

### Features

* **api:** manual updates ([1f24c3f](https://github.com/miruml/python-server-sdk/commit/1f24c3f238e13344e158a909a8444fe6a02534ec))
* **api:** manual updates ([616466d](https://github.com/miruml/python-server-sdk/commit/616466d196871cb65ad48ecccf292be3596043b1))

## 0.4.1-beta.0 (2025-10-05)

Full Changelog: [v0.4.0...v0.4.1-beta.0](https://github.com/miruml/python-server-sdk/compare/v0.4.0...v0.4.1-beta.0)

### Refactors

* **api:** rename miru-server to miru ([163c465](https://github.com/miruml/python-server-sdk/commit/163c4659c64f6b954d9b91e7b340554f0919efa6))
* **api:** revert package name to miru_server_sdk ([0c8b7d7](https://github.com/miruml/python-server-sdk/commit/0c8b7d74ae67df4005fc069c4575ffae78b975c6))

## 0.4.0 (2025-09-23)

Full Changelog: [v0.0.1...v0.4.0](https://github.com/miruml/python-server-sdk/compare/v0.0.1...v0.4.0)

### Chores

* update SDK settings ([e7bd9a6](https://github.com/miruml/python-server-sdk/commit/e7bd9a6b432ceeb9e9746577c0588bc3d8d6d81c))
* update SDK settings ([e6ec403](https://github.com/miruml/python-server-sdk/commit/e6ec4031305e950d8f61d18a55344de0e36f752b))
