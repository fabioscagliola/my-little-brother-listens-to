# My little brother listens to

If you are my little brother and want to track your own listens, then this is the project for you!

Well, actually, whatever your relation to me is, you may use this simple Python script to dump the last releases you tracked on ListenBrainz into a frontmatter format like the one my little brother uses in his [media log](https://blog.scaglio.id/medialog/).

Copy `.env.dist` to `.env`, add your ListenBrainz API URL, and run the following commands:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python my_little_brother_listens_to.py
```

