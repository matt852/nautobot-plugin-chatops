# Frequently Asked Questions

## "This app responded with Status Code 404" error returned while picking a filter from a slash command

If a 404 error is being returned while trying to use a slash command that allows for filtering, there is most likely a typo within the Interactivity Request URL for your application.

- Navigate to [https://api.slack.com/apps](https://api.slack.com/apps) and select your Nautobot ChatOps application that is currently in development
- Under **Features**, navigate to "Interactivity & Shortcuts"
- Under **Interactivity**, confirm that the Request URL is of the format: `https://<server>/api/plugins/chatops/slack/interaction/` (Note the trailing slash)