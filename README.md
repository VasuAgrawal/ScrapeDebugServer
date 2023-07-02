# ScrapeDebugServer

```
python -m pip install flask gunicorn
gunicorn -w 1 -b 0.0.0.0:5000 scrape_debug_server:app
```

Run this inside a tmux shell ideally