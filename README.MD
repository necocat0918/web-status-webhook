# Simple Webhook System

Feel free to modify or use this python script.

It is a little bit hard to read, but it works :)

## How to use it?

To use this script, you must edit it yourself. You are able to customize line 4 ~ 20

```
webhook = 'webhook here!' #Enter your webhook
```
Fill the text "webhook here!" to your webhook to make the script actually work.

```
website = 'website here!' #Enter the target website

```
Fill the text "website here!" to your website link to also make the script actually work.

```
alternative = True # if there's an alternative, flag it to True.
alternativeLink = 'alternative here!'
```
Just as the script says, change "True" to "False" if you don't have any alternative domains.

<sup> Also, please make sure that the first letter is capitlized else it will be an error.</sup>

```
datadown = {
    'content' : '@everyone the website is currently **down**'
}

datadownAlternative = {
    'content':'@everyone the dns is **not available**, please use [this domain](' + alternativeLink + ')'
}

dataOnline = {
    'content':'@everyone the website is back online!'
}
```
You can edit the message by changing the area that the default messages use.
Just think you're typing in discord.