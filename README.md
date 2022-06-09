<div id="top"></div>
<div align="center">
<a href="https://github.com/Falc0n2k/reply-assistant/releases"><img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/falc0n2k/reply-assistant?style=for-the-badge"></a>
<a href="#"><img alt="Project status" src="https://img.shields.io/badge/Status-Active-blue?style=for-the-badge"></a>
<a href="https://github.com/Falc0n2k/reply-assistant/blob/main/LICENSE.txt"><img alt="GitHub" src="https://img.shields.io/github/license/falc0n2k/reply-assistant?style=for-the-badge"></a>

<a href="https://github.com/Falc0n2k/reply-assistant/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/falc0n2k/reply-assistant?style=for-the-badge"></a>
<a href="https://github.com/Falc0n2k/reply-assistant/network/members"><img alt="GitHub forks" src="https://img.shields.io/github/forks/falc0n2k/reply-assistant?style=for-the-badge"></a>
<a href="#"><img alt="GitHub repo stars" src="https://img.shields.io/github/stars/falc0n2k/reply-assistant?style=for-the-badge"></a>
<a href="https://github.com/Falc0n2k/reply-assistant/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues-raw/falc0n2k/reply-assistant?style=for-the-badge"></a>
</div>

<br/>
<br/>

<h1 align="center">Reply Assistant</h1>
<p align="center">A lightweight Reddit bot that provides automated responses.</p>
</div>

<br/>
<br/>

## About The Project

A bot for Reddit communiites that provides a response based on a keyword detected in the body of the post or in a comment. Helpful for tech support communities who'd like to automate error code responses for customers, or frequently asked questions.

### Built With

* [Python](https://www.json.org/)

### Dependencies

* [PRAW - Python Reddit API Wrapper](https://github.com/praw-dev/praw) by u/bboe
* [Python 3](https://www.python.org/download/releases/3.0/)

### What problem does this module solve?

As a frequent Redditor, I came to realize that moderators in high-traffic communities (particularly, those in the tech support realm) need an efficient way to reply with information critical to providing a good experience for community users, but without the repetititon of having to type the same responses out each time or copy/pasta.

This automation aims to solve that problem by allowing moderators to script responses based on keyword detection (such as an error code or other trigger phrase), providing a real-time response.

### How does it work?

When a user posts content that contains a keyword or trigger phrase relevant to a given community the bot will respond with a top-level comment on that post stating the phrase and whatever text mods choose. For example, if a keyword is an error code, a moderator in a tech support community might choose to put a description of that error code and some frequently identified methods on solving the problem. Mods can also include links to external resources, and their community's wiki, if needed, to enhance the experience.

### Contributing

I still have a little technical debt on this bot:

* Add compatibility for the latest PRAW version

If you'd like to help, consider forking this repo and submitting a pull request.

### License

Distributed under the MIT License. See [LICENSE.txt](/LICENSE.txt) for more information.

### Acknowledgments

* [djshadowxm82](https://github.com/djshadowxm82) - co-author
