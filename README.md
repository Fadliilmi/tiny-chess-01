# tiny-chess-01

[![make.fun](https://img.shields.io/badge/make.fun-tiny--chess--01-blue)](https://make.fun/competitions/tiny-chess-01)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](main.py)

A chess engine in 4,089 bytes of Python, built for the
[make.fun](https://make.fun) tiny-chess-01 competition: the strongest
engine that fits in 4 KB.

`main.py` is the whole engine. It talks to the contest env over HTTP
(`POST /game`, `POST /move`), plays every game of the gauntlet, and
exits when the trial is done. No model calls, no clock, no randomness:
a fixed 70,000-node budget per move, so a replay plays the same moves.

Inside: a 64-square board, negamax alpha-beta with quiescence search
and iterative deepening, killer moves, MVV-LVA move ordering, and a
material + piece-square evaluation with a pawn-shield king safety term.

## Grade it locally

From the competition kit directory:

    node cli/makefun.mjs grade-local --kit . --bot <this repo> --driver docker
