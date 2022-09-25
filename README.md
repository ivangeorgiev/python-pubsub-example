# Event-driven Python with pubsub

## Install

```bash
$ python -m venv .venv
$ source .venv/Scripts/activate
$ pip install -r requirements.txt
```

## Run simple example

```bash
$ python simple_pubsub.py
```

Should produce following output:

```
============
New Order:
============
ID: 35f18675-7600-48ca-bf5d-48a303ab70fb
Items: ['100 inch TV', 'magic carpet']
============
New Order:
============
ID: b07794c7-21f7-4eea-b3a7-986f6098235f
Items: ['soft cheese', 'dutch mashrooms']
```

## Run advanced example

```bash
$ python advanced_pubsub.py
```

Produces the same output as the simple example:

```
============
New Order:
============
ID: 35f18675-7600-48ca-bf5d-48a303ab70fb
Items: ['100 inch TV', 'magic carpet']
============
New Order:
============
ID: b07794c7-21f7-4eea-b3a7-986f6098235f
Items: ['soft cheese', 'dutch mashrooms']
```