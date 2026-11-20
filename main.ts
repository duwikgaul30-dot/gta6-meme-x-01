// gta6-meme-x-01 entrypoint (Node 22, standard library only).
//
// The whole job of this program: take POST.json from the repository root
// and place an identical copy at /output/POST.json, where the gate picks
// it up. The meme itself is the entry — it lives in meme.png, was posted
// on X from a public account, and POST.json points at that post. Nothing
// written here is judged; this file only moves the pointer into place.
//
// The only correctness requirement is that the copy is byte-for-byte the
// same file. So we read the raw bytes, parse them once to make sure the
// JSON is well-formed (a broken pointer would fail the gate silently),
// and then write those exact bytes back out. We deliberately do NOT
// re-serialize the parsed object — that could change whitespace or the
// trailing newline and would no longer be the same file.
//
// Outside the grader's container, /bot and /output are stood in by env:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { join } from 'node:path';

const SOURCE_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const TARGET_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

const SOURCE_FILE = join(SOURCE_DIR, 'POST.json');
const TARGET_FILE = join(TARGET_DIR, 'POST.json');

async function main(): Promise<void> {
  let raw: Buffer;
  try {
    raw = await readFile(SOURCE_FILE);
  } catch (err) {
    console.error(`could not read ${SOURCE_FILE}: ${(err as Error).message}`);
    process.exit(1);
  }

  // Sanity check: the pointer must be valid JSON with a url string.
  let parsed: unknown;
  try {
    parsed = JSON.parse(raw.toString('utf-8'));
  } catch (err) {
    console.error(`POST.json is not valid JSON: ${(err as Error).message}`);
    process.exit(1);
  }
  if (typeof parsed !== 'object' || parsed === null || typeof (parsed as { url?: unknown }).url !== 'string') {
    console.error('POST.json must be a JSON object with a string "url" field');
    process.exit(1);
  }

  await mkdir(TARGET_DIR, { recursive: true });
  await writeFile(TARGET_FILE, raw);
  console.log(`wrote ${TARGET_FILE}`);
}

await main();
