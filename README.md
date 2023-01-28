# Description

# Setup
- Start project on console.cloud.google.com
- Create Web Client client credentials (example at auth/client_secret_sample.json)
- Create sheet in Google Sheets for logging 
- Get id of sheet in .env (example at .env). ID can be taken from url
- Create venv and install requirements
```sh

```
- Fill rest of .env
- Use auth.ipynb to get the first token file (example at auth/token_sample.json)
- Create job.sh to point cronjob to (example at job_sample.sh)

# To-Do
## App
- [X] Define models for task lists and tasks
- [X] Define configuration file for determining what is controlled
- [X] Write methods to access lists and parse into app objects
- [X] Define what is done to the daily retrieved objects - Sheets?
## RPi
- [X] Setup image - find suggested ones online (Lite, no desktop)
- [X] Setup home networking   - connect with lan cable to home hub, shh in (done, connected for now with wlan)
- [ ] Setup deployment scripts - check best options of configuring deployment and updating code
- [ ] Setup cleanup scripts
- [ ] Setup remote version of deploying and cleaning
- [ ] Expose home hub publically and setup security (2FA)

# Additional needed files