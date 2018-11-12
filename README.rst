*****************************
PyConCA 2018 asyncio tutorial
*****************************

crypto exchange example re: web sockets

Tutorial Wiki: https://github.com/pyconca/2018-wiki/wiki/Tutorials#building-your-own-crypto-exchange-in-async-python

Slides: https://docs.google.com/presentation/d/1bJ38Fv6K2Xmgqq-7mZHcWT39wo_P0sfThGt2R-QkcHs/edit?usp=sharing

Repo: https://github.com/ankitml/pyconca-tutorial-exchange


Environment
===========

::

  conda env create -f environment.yaml
  conda activate asyncio-tutorial
  pip install -r requirements.txt


Testing
=======

Install `Simple Web Socket Client`_ add-on for Firefox (or Chrome).

.. _Simple Web Socket Client: https://addons.mozilla.org/en-US/firefox/addon/simple-websocket-client/

Run ``ws.py`` to launch async web socket server.

Open http://localhost:9999/ in `Simple Web Socket Client`_.

Close and re-open web socket client any time ``ws.py`` is re-started.
