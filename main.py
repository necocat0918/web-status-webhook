import requests
import time

webhook = 'webhook here!' #Enter your webhook
website = 'website here!' #Enter the target website

alternative = True # if there's an alternative, flag it to True.
alternativeLink = 'alternative here!'

datadown = {
    'content' : '@everyone the website is currently **down**'
}

datadownAlternative = {
    'content':'@everyone the dns is **not available**, please use [this domain](' + alternativeLink + ')'
}

dataOnline = {
    'content':'@everyone the website is back online!'
}

currentlyDown = False
alternativeDown = False

# A little spaghetti down there, may be a little hard to read.
# But as long as it works, I'll take it.

def checkTargetWeb():
   
   global currentlyDown 
   global alternativeDown # Anti-spamming

   # Connect to website
   try:
       checkWebsite = requests.get(website, timeout=10)
       checkWebsite.raise_for_status()
   except requests.exceptions.RequestException as err:
       print('The server might be dead')
       print(err)
       if currentlyDown == False:
          if alternative == True:
              if alternativeDown == False:
                 try:
                    checkAlternative = requests.get(alternativeLink, timeout=10)
                    checkAlternative.raise_for_status()
                 except requests.exceptions.RequestException as err:
                     requests.post(webhook, json=datadown)
                     currentlyDown = True
                     alternativeDown = True
              else:
                  requests.post(webhook, json=datadownAlternative)
                  alternativeDown = False
          else:
              requests.post(webhook, json=datadown)
              currentlyDown = True
       
   else:
       print('The website is up and running')

       if currentlyDown == True:
           requests.post(webhook, json=dataOnline)

       currentlyDown = False

def main():
   while True:
       checkTargetWeb() # Loop basically
       time.sleep(60)

if __name__ == '__main__':
    main()
