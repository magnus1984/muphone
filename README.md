# muphone
A phone ownership validation microservice 

## Introduction
muphone is an AWS lambda microservice that allows you to verify ownership of a 
user provided phone number. This is usually needed in "sign up" scenarios on 
many websites. Here are the typical steps of a validation workflow:

1. A user submits a phone number through a form on your website.
2. The user is sent a generated validation code at the phone number provided.
3. The user submits the received validation code and the phone number is 
verified.

The service is RESTful and can easily integrate with any http clients 
available.

## Live Demo
You can interact with the microservice with your favorite http client library. 
I like to use httpie for that:

```bash
http POST https://muphone.portfolio.hedgenet.info/phone number=<your number>
```

The format of the phone has to be Once a phone number is submitted, you can query the current verification 
status:

```bash
http GET https://muphone.portfolio.hedgenet.info/phone number=='+15147174993'
```

### React Live Demo
If you prefer, there is a live demo of the microservice that shows integration 
with a simple React Frontend.

## Deployment
The microservice uses AWS CloudFormation for automated deployment. If you want 
to deploy the microservice on your own you will need ...


## Author
Jonathan Pelletier (jomagnus1984@gmail.com)
