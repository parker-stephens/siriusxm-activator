# siriusxm-activator

This is an extremely basic HTML page that can theoretically activate a Sirius radio for three months at a time. I say theoretically because you must disable CORS in your browser, otherwise the browser prevents cross-site scripting.

You must first generate a login token that will let you send requests to the Sirius API.

Then you input the radio ID in the box, and select make account (creates trial account for radio), then select activate (sends refresh signal) radio.

I personally have found it much easier to use a REST client with a GUI to send the requests.

## Background

In the past people have used the SiriusXM Dealer app with a spoofed location (or, get this, some have driven into a dealership parking lot) to activate their radios for free. Sirius first mitigated this in versions > 2.1 by not creating an account for the radio if there was not one found, requiring you to call dealer support. This was different because in 2.1 if there was not an account, it would create a trial account. People found that the 2.1 app still worked, however, and just downgraded their version. Sirius eventually mitigated all of this by forcing a dialog box to update the app if you were on anything < 2.4.

I had a feeling that eventually something like this would happen, and was also just curious as to how the app worked. I intercepted the network requests made by the app, and was able to reproduce all the steps in activating a radio on the 2.1 app.
