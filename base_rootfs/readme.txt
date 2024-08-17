What you have in front of you is a VERY small and VERY limited chroot environment.

It was initially wrote in a language that ran on mAcrosoft computers only;
Later it was rewritten in Python and that's the version you are looking at.

Here's how it works:
You have some basic terminal commands:
- "cd", "ls" for directory navigation
- "cat", to look at file contents (you used it to display this readme)
- "clear", can clear the screen if needed
- "help", shows a list of available commands
- "exit", just exits the entire environment

Now comes the fun part:
- "mail", it's a receive-only mailbox, you'll use this a lot.
- "connect", allows you to connect to remote systems providing an address/IP and a port
  for example: "connect test-server.com 22"
- "scan", allows you to scan an address/IP for open ports, useful if you then need to connect to it.
  for example: "scan test-server.com"

Everything else you need to figure out by yourself.
Have Fun!
