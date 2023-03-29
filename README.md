# Hive Performance Ltd

Hive Performance Ltd have created an all-in-one Sports Management solution for both teams and individuals.

The Application comprises of individual tools, all of which can be integrated together.

## Set-Up

To start the Database for the application, you will need:

* 2 Environments Variables:
    * DB_PASSWORD
    * SECRET_KEY  

* Docker & Docker-Compose installed on your machine

To run the application, on Linux:

```bash
git clone https://gitlab.com/jordan-grindrod/hiveperformance.git hiveperformance && cd $_

docker-compose pull && docker-compose up -d
```

## Wellness Tool

The Wellness tool is designed to allow Athletes to submit a daily Wellness Questionnaire, and for both Athletes and Staff to see statistics regarding the results of this Questionnaire.
