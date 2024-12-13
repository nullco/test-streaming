# Streaming testing

PoC for streaming endpoint.

Open several browser windows to check how concurrency works with different gunicorn worker modes


## Sync

Less performant of all options. Each worker blocks entier for the duration of the streaming response

```bash
 gunicorn app:app -w 1
```

## Gevent

Uses gevent library. This networking library monkey-patches all low-level IO libraries and make async transparent for the programmer

```bash
 gunicorn app:app -w 1 -k gevent
```
