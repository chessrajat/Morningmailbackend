# Morning mails

## Endpoints

---

## Auth

- Register (POST) - ```/api/v1/user/register/```
```
{
	"name": "",
	"email": "",
	"password": "",
	"re_password": ""
}
```

- Login (POST) - ```/api/v1/user/token/```
```
{
	"email": "",
	"password": ""
}
```

- Logout (POST) - ```/api/v1/user/logout/```
```
{
	"refresh": ""
}
```

- Refresh Token (POST) - ```/api/v1/user/token/refresh/```
```
{
	"refresh": ""
}
```

## Emails

- Daily Stats (GET) - ```/api/v1/email/dailystats/?days=7```
- Subscribers Stats (GET) - ```/api/v1/email/subscriberstats/```
- Track Open Email (GET) - ```/api/v1/email/track/<track_id>/```
- Send Email to all the users for testing purposes (GET) - ```/api/v1/email/sendmails/```