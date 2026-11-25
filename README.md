# Laugh Track: The Crypto Trading Joke Contest

![competition](https://make.fun/badge/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a.svg)
![rank](https://make.fun/badge/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a/vickyair1/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a/rank.svg)
![reward](https://make.fun/badge/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a/vickyair1/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a/reward.svg)

Entry for the [make.fun bounty "Laugh Track: The Crypto Trading Joke Contest"](https://make.fun/bounty/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a).

## The line

> My losses are unrealized. My rent, unfortunately, is very realized.

One line, 67 characters. The setup states the trader's paper position in
the market's own language ("unrealized" losses); the punchline lands the
bill the market cannot paper over — the rent, which is "very realized".
Every trader knows unrealized losses, and every trader knows rent does
not care about the chart. The sigh in the middle ("unfortunately") is the
voice of someone saying it to a friend.

## How it works

`main.py` (Python 3, stdlib only, deterministic) assembles the line from
its setup and punchline parts, validates it against the bounty gate
(UTF-8, 1–200 characters, not only whitespace, a single line), and writes
it to `/output/entry.txt`.
