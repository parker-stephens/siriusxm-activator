# siriusxm-activator

This is a python script that can activate a Sirius radio for three months at a time.

It does this by replicating the API calls that the SXM dealer app makes when activating a radio.

When you run the script, it will ask for your radio ID. Then, it should activate if the createAccount and update_2 responses are SUCCESS.

Running [this](https://replit.com/@parkercs/activateradio) replit can be done in the browser.

## Background

In the past people have used the SiriusXM Dealer app with a spoofed location (or, get this, some have driven into a dealership parking lot) to activate their radios for free. Sirius first mitigated this in versions > 2.1 by not creating an account for the radio if there was not one found, requiring you to call dealer support. This was different because in 2.1 if there was not an account, it would create a trial account. People found that the 2.1 app still worked, however, and just downgraded their version. Sirius eventually mitigated all of this by forcing a dialog box to update the app if you were on anything < 2.4.

I had a feeling that eventually something like this would happen, and was also just curious as to how the app worked. I intercepted the network requests made by the app, and was able to reproduce all the steps in activating a radio on the 2.1 app.
