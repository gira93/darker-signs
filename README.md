# Darker Signs

## A complete rewrite of 2006 "Dark Signs" from Vectra Media

## What's this?

This is what's called a "Hacking Simulation" game (or a text puzzle game if you want).
The scope is to simulate an hacking environment for fun.

Long wall of text coming with story and motivation,
so here's a TLDR if you just want to play:

### Running

After cloning the repo, run `./start.sh` to run the game.
The script will setup venv, install dependencies
and then run the game.

### Restarting

The game stores everything inside a `rootfs` directory that will be
created on first run.
If you want to restart the game, just delete the `rootfs` directory
and run `./start.sh`

## What's "Dark Signs"?

Dark Signs was a 2006 free game developed by Vectra Media and Terminal Zero Media;
It was rebranded a lot of times, at some point it was a multiplayer hacking game.

## And this is based on which version?

Darker Signs is based on the latest Single player game of 2006, version 0.96.1.
This is a complete rewrite in Python (instead of Visual Basic)
and it runs completely in CLI (no GUI).

## Why?

Some months ago I rediscovered Dark Signs
(which is still available at: <https://darksigns.com/>);
I was hooked again like I was years ago.

There was only a problem, it's difficult to make it run stable on Linux;
I had problems with full screen modes and some crashes.

So that night I started looking inside the game files and found out that
all of the servers where saved in a directory, plain VB scripts, clear as day.

That started a night long rabbit hole of finding hidden stuff in the game,
there were servers never mentioned anywhere, broken side missions,
part of the game missing entirely (remember, the game never had a v1.0 release).

So I decided to take what was working of the game, mainly the "main" story line,
and rewrite it in a modern language.

I've chosen Python because it matched well with the original VB language
and the conversion should've been easier...
And it was actually.

## And?

And so I started writing a CLI "engine", a simulation of chroot environment.

In a couple of days I had a working CLI, basic unix command (ls, cd, cat),
and a fake "network system", with dns and servers.

Thanks to a couple of helper scripts I wrote,
I was able to populate my "dns" (a JSON file) with all the in-game servers.

Then I started writing code for the servers by hand,
this was the longest part, there wasn't a way to automate that
(not that I could find).

And I did it, it's not perfect, it's not finished
but you can play and complete the entire main quest.

## What did you change from the original?

Mainly the storyline, I wrote it to be a bit more consistent,
I gave you (the player) a reason to be there basically.

## Closing

This is a project of pure passion, a fun way for me to do something
with a language I don't really know but appreciate
(I'm a Ruby / JavaScript / TypeScript developer IRL).

So you will find mistakes, things written suboptimally
(or straight up wrong).
