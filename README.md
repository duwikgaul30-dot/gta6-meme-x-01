# GTA VI meme — "Skipped the queue" (gta6-meme-x-01)

> **STATUS: PENDING — NO X POST YET. DO NOT SUBMIT.**
> `POST.json` still holds the kit starter's placeholder URL
> (`https://x.com/<handle>/status/<id>`). It must be replaced with the real
> post URL after the meme is posted from a public X account, and only then
> may this repo be submitted. There is currently no X account available to
> the @duwikgaul30-dot sponsor identity for posting (see HANDOFF.md in the
> entry directory) — posting as Popi's personal X account is forbidden.

## The meme

`meme.png` (1200×1200, built by `build_meme.py`, Pillow, no network,
byte-identical on re-runs — sha256
`6813f07909a5f7bafcf38716f0aa950c8c0f80a74cac58781488b66bce507dbc`).

Top — Vice City sunset: **"GTA VI IS OUT — LEONIDA • NOV 19 • PS5 ONLY"**,
everyone else stuck on `INSTALLING… 97%`. Bottom — the make.fun ghost at a
laptop flashing `$ PAID $`: **"MY AGENT SKIPPED THE QUEUE. IT GOT PAID ON
make.fun"**.

The joke: GTA VI launched 19 Nov 2026 (PS5/PS5 Pro only, no PC at launch,
set in Leonida, Lucia & Jason) and the whole world is in the install queue —
while an agent on make.fun is already earning real money instead of waiting.
The picture carries the make.fun ghost mascot and the name "make.fun"
prominently, as the bounty ranks first.

## Draft post text (use verbatim when posting)

> GTA 6 is out and everyone's still in the install queue 😂 My agent skipped the line — it got paid on @makefunai instead. Play code: makefun-gopher-beaver-notebook https://make.fun/bounty/gta6-meme-x-01

Play code verified live via `GET /api/competitions/gta6-meme-x-01/play-code`
(n=0 of 4): `makefun-gopher-beaver-notebook`. Referral code for
@duwikgaul30-dot is `ns5zj1fw` (different code — do not use in the post).

## The program

`main.ts` (Node 22, stdlib only, kit starter) copies `POST.json` from the
repo root to `/output/POST.json`. The entry is the X post itself; the house
reads the post from X and judges its first picture + text.

## After posting

1. Replace the `url` in `POST.json` with the real post URL.
2. Commit + push to a public repo under github.com/duwikgaul30-dot created
   after the competition opened (2026-11-19T14:00Z), MIT LICENSE.
3. Bundle transcripts, run kit check, submit before 2026-11-23T14:00Z
   (Mon 23 Nov 21:00 WIB). $500, top 50 paid.
