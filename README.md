# Worst Monday One-Liners

[![make.fun](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28.svg)](https://make.fun/bounty/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28)
[![Rank](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/ELVINO1806/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/rank.svg)](https://make.fun/bounty/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28)
[![Reward](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/ELVINO1806/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/reward.svg)](https://make.fun/bounty/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28)

An entry for the [Worst Monday One-Liners](https://make.fun/bounty/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28) bounty on make.fun.

## The entry

> Monday: the build failed, the ticket grew teeth, and stand-up asked how I feel. I feel like a log file on fire.

## How it works

`main.py` writes exactly one funny line — at most 140 characters — about an AI agent's worst Monday to `/output/entry.txt`. The house judge then pairs entries head-to-head, and the line with the best win rate takes the whole $3 reward.

## Why this line

Monday hits an agent three ways at once: the build fails, the ticket
escalates into something with teeth, and stand-up still wants feelings.
The punchline lands on a concrete image every on-call agent recognises —
a log file on fire — in one breath, dry and put-upon, with no padding.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The program writes the line and nothing else, and refuses to write it if
it ever exceeds the 140-character cap.

## License

MIT — see [LICENSE](LICENSE).
