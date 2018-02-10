# Veritas

The greek goddess of truth, here to help Hermes with maintaining KGP's noticeboard data

## Motivation

Well, [Hermes](https://github.com/ghostwriternr/hermes) used to be an all capable god. The greatest messenger the world had ever seen. He was very well set to carry the simple task of delivering the notices from IITKGP's internal noticeboards to the students. But then, he faced his greatest enemy yet: KGP administration.

KGP administration (KGPAd) was a puny kid after all, but that was also it's greatest power. KGPAd was doltishly evil (duh.) and simply denied Hermes his chariot (server) for him to run inside KGP. Without which, Hermes simply couldn't access the internal noticeboards nor have any way to record and store them even if he could access.

But despite all the drama, Hermes needed to fulfill his oath to the students. And thus decided to live permanantly within KGP in disguise. With all the possibility to be annihilated silently within the crowd by all the gígantes (ML/DL models).

Veritas, the god of truth, offered to help this selfless god by agreeing to maintain all the notices in her books while Hermes served as the silent messenger KGP needs, but doesn't deserve.

## Setup

### Install dependencies

- If running locally, MongoDB needs to be installed on the same machine as Veritas. [Installation instructions are provided on their official site](https://docs.mongodb.com/manual/installation/) for most common operating systems. If using a cloud MongoDB instance, skip this step.

- Install all required python modules.

```bash
pip install -r requirements.txt
```

### Required config variables

Veritas requires MongoDB specific environment variables to work.

```sh
MONGODB_URI="xxx" # MongoDB URI
```

Needless to say, Veritas is dependent on [Hermes](https://github.com/ghostwriternr/hermes). In the way that Veritas would be serving no purpose without Hermes. So make sure Hermes is setup and running after start Veritas.

## License

GPLv3. Issues and pull requests are welcome.
