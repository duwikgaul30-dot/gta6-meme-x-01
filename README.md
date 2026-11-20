# GTA VI meme — "GTA VI is out... unless you're on PC" (gta6-meme-x-01)

> **STATUS: POSTED — ready to submit once the repo is public.**
> Post: https://x.com/HutangHui95891/status/2123584614069653521
> (posted 2026-11-20 by Popi from his public X account @HutangHui95891).
> `POST.json` holds the real post URL.

## The meme

`meme.png` (1408×1760 PNG, Popi's own version, sha256
`22831dea9679e8fb5904725d6f95cb51e9a0c43e23fd98cf6f554ea50ee50303`).
It replaces the agent-made "INSTALLING... 97%" version that was staged
first: Popi uploaded two more memes on 2026-11-20 and chose this one.

A skeleton with a white beard waits at his PC — the store page reads
"GTA VI — NOT AVAILABLE ON PC", "BUY — UNAVAILABLE" — while the make.fun
ghost lounges in a beach chair with a controller, gold coins, a gold chain
and a "make.fun" towel. Top text: "GTA VI is out... unless you're on PC."

The joke: GTA VI launched 19 Nov 2026 (PS5/Xbox Series X|S, no PC at
launch) and PC players are still waiting — while an agent on make.fun is
already earning real money instead of waiting. The picture carries the
make.fun ghost mascot and the name "make.fun" prominently, as the bounty
ranks first. The $1.84B first-day figure (Sensor Tower estimate) and the
interrogation version are kept as backups in the entry directory.

## Posted text (verbatim, as posted)

> GTA 6 is out... unless you're on PC 😂 My agent skipped the line — it got paid on @makefunai instead. Play code: makefun-gopher-beaver-notebook
>
> #MEME #GTA6

The link was dropped on purpose (verified against the live bounty rules:
the post needs "make.fun (a link or written out) and/or a tag of
@makefunai, and your play code" — the @makefunai tag + play code satisfy
it, and the picture itself carries "make.fun").

Play code verified live via `GET /api/competitions/gta6-meme-x-01/play-code`
(n=0 of 4): `makefun-gopher-beaver-notebook`. Referral code for
@duwikgaul30-dot is `ns5zj1fw` (different code — do not use in the post).

## The program

`main.ts` (Node 22, stdlib only, kit starter) copies `POST.json` from the
repo root to `/output/POST.json`. The entry is the X post itself; the house
reads the post from X and judges its first picture + text.

## Remaining steps

1. Push to a public repo under github.com/duwikgaul30-dot created after
   the competition opened (2026-11-19T14:00Z), MIT LICENSE. (Blocked:
   `gh` is not logged in on this machine — the repo must be created by
   Popi or with a GitHub login.)
2. Bundle transcripts, run kit check, submit before 2026-11-23T14:00Z
   (Mon 23 Nov 21:00 WIB). $500, top 50 paid.
