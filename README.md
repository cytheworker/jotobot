[Discord]: https://discord.com/
[Flake8]: https://flake8.pycqa.org/en/latest/
[Git]: https://git-scm.com/
[Jotoba API]: https://jotoba.de/docs.html
[Pyright]: https://github.com/microsoft/pyright

# JotoBot

**JotoBot** allows an easy access to a Japanese
dictionary provided by [Jotoba API] on [Discord].

## Roadmap

- [ ] Search
- [ ] Image
- [ ] Radicals
- [ ] Completion
- [ ] News

## Hosting

We have no plan on hosting the bot ourself, but feel free to host the bot yourself!

```sh
# ensure the latest version of `git` and `docker` are installed
git clone https://github.com/cytheworker/jotobot.git
cd jotobot

# ensure the gateway intents of `SERVER MEMBERS` and `MESSAGE CONTENT` are enabled
echo DISCORD_TOKEN=[YOUR DISCORD BOT TOKEN] >> .env
docker compose up --build # optionally `just run` if you have `just` installed
```

## Contributing

Any form of contributions are greatly welcomed and appreciated! There are no strict
guidelines and rules in terms of code styling and issue/pull request templating,
but we enforce the use of [Flake8] and [Pyright] on the codebase, as well as a
clear and detailed description/explanation of proposed issues/pull requests.

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