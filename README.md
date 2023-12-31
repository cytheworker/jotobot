[Jotoba API]: https://jotoba.de/docs.html

# JotoBot

**JotoBot** is a free self-hosted **Discord** bot that provides a quick and
easy access to a **Japanese** dictionary provided by [Jotoba API]. The
project is currently **work in progress**, but the latest development
version can still be installed and run with the following steps:

```sh
# install the latest version of `docker`
# copy `.env.example` as `.env` and fill out the missing values
# enable the gateway intents of `SERVER MEMBERS` and `MESSAGE CONTENT`
# run the following `docker` command from a terminal:
docker run --env-file .env ghcr.io/cytheworker/jotobot:latest
```

## Roadmap

- [ ] Search (words/names/kanji/sentences)
- [ ] Radicals (by_radical/search)
- [ ] Completion (suggestion)
- [ ] News (short/detailed)

## License

MIT License

Copyright (c) 2023 CyTheWorker

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.