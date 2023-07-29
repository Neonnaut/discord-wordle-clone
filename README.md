# Discord Wordle Clone

A bot for playing a clone of Wordle.

**Note 1:** This project is inspired by the popular word game called "Wordle" but is not affiliated.

**Note 2:** This is a fork of https://github.com/DenverCoder1/discord-wordle-clone.

## Changes in this fork

- This fork has been migrated to discord.py version 2.3.1.
- The Wordle commands have been migrated to a cog
- The Wordle commands have been migrated to hybrid commands
- Jonah Lawrence's help cog has been added as a cog, with some small formatting changes
- The embeds have been reworded in some small ways
- The emoji images have been directly added to this fork
- The yellow letters have been changed to a darker shade of yellow (easier to read)
- `codes-for-getting-emojs.txt` has been added for easily getting the emoji codes from your server(s)
- The dict-popular word list has had 13 U.S. American spellings with "-or" removed from the popular word list
- The dict-popular word list has had 1 U.S. American spelling "fiber" removed from the popular word list
- The dict-popular word list has had 5 colloquial U.S. American words senor, amigo, santo, gator, youse removed from the popular word list
- The dict-popular word list has had the following words removed because... they're not English??: bijou, brava, playa, chico
- The dict-popular word list has had the following proper nouns, outdated-by-200-years words, extremely obscure words, and other truly bizzare removed: allee, ascot, bates, becks, begat, belie, benny, brent, brock, burro, carbo, cates, catty, chang, coles, demur, erica, ethyl, faggy, fitch, hallo, harts, haute, honda, hullo, hurst, kabob, kelly, kerry, kooks, laird, laura, lazar, loran, mamie, marge, massa, mavis, maxim, miggs, mohel, molto, mondo, natty, nelly, paris, rajah, rioja, sahib, saith, shiva, stein, steno, strep, vesta, wiggy, xerox
- The dict-popular word list has had duplicate "white" removed
- Added "texta" and "twerk" to the sowpods list.

## Setup

- In the [Discord developer portal](https://discord.com/developers/applications) create a new application and give it a name. Under `Bot` select "add bot"
- Under `Bot`, turn on PRESENCE INTENT, SERVER MEMBERS INTENT and MESSAGE CONTENT INTENT
- Generate an invite link for your bot under `QAuth2 > URL Generator`, with "bot" > "manage roles", "read messages/view channels", "send messages", "use external emojis" and "add reactions" permissions
- Use the invite link in your browser to invite your bot to any servers you want the bot in
- Download the `bot` folder to your environment, the one with the `__main__.py` file, `.env` file and `cogs` folder
- Install python 3.10+. Make sure you have set Python to the system path to use pip
- Install dependencies with `pip install REQUIREMENTS.txt`
- You can change the bot prefix in the `constants.py` file
- Rename `.env.example` to `.env` in the `wordlebot` folder. Make sure the file is called ".env" and _not_ ".env.txt"
- Back in the developer portal, under `Bot`, copy your bot's secret token. Paste it in the `.env` file where `TOKEN=your_token_here` -- with your bot's secret token replacing "your_token_here"
- Uload the emojis in the emoji folder to your server(s)
- Get your emoji codes by pasting `codes-for-getting-emojis.txt` in a channel on your server(s) and replacing the emoji codes in `wordle_utils.py` with the new emoji codes
- Run it as a module with `python wordlebot`, or `sudo nohup python3 wordlebot` or whatever command you use to run python scripts in your environment; or directly run the `__main__.py` file. Congratulations, you are now self-hosting a discord bot
- You can play wordle by using the command `/wordle`
- You might need to turn on all intents in the developer portal, or change the bots intents in the `__main__.py` file
