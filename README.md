[![header.jpg](https://raw.githubusercontent.com/atompie/tracardi/tracardi-unomi-master/screenshots/github-splash.png)](https://raw.githubusercontent.com/atompie/tracardi/tracardi-unomi-master/screenshots/github-splash.png)

# Tracardi Open-source Customer Data Platform

[Tracardi](http://www.tracardi.com)  is a open-source Customer Data Platform.

TRACARDI is an API-first solution, low-code / no-code platform aimed at any e-commerce business that 
wants to start using user data for marketing purposes. If you own a brand new e-commerce platform or 
a legacy system you can integrate TRACARDI easily. Use TRACARDI for:

 * **Customer Data Integration** - You can ingest, aggregate and store customer data
   from multiple sources in real time at any scale and speed due to elastic search backend.
   
 * **Customer Data Modelling** -  You can manage data. Define rules that will model data delivered
   from your page and copy it into user profile. You can segment customers into custom segments.
   
 * **User Experience Personalization** - You can personalize user experience with
   real-time customer segmentation and targeting.
   
 * **Profile Unification** - You can merge customer data from various sources to
   single profile. Auto de-duplicate customer records. Blend customers in one account.
   
 * **Automation** - TRACARDI is a great framework for creating
   marketing automation apps. You can send your data to other systems easily

# Read-map

### Version 0.4.0

#### Use cases
- [x] Collecting events from web-page by JavaScript
- [x] Binding events to elements on the page
- [x] Gathering user properties
- [x] Merging user profiles
- [x] Simple segmentation

#### Features
- [x] Defining user data enhancement by workflow
- [x] Workflow staging – working copy of workflow is not affecting currently running workflows. Workflow is executed only after it is deployed not during editing. 
- [x] Simple workflow debugging
- [x] Triggering workflow by rules
- [x] Source configuration
- [x] Credentials inside source
- [x] Source should have type of query storage or event sourcing.
- [x] Plugins configuration
- [x] Schema for PII
- [x] Filtering of action plugins
- [x] User and password configurable by ENV
- [x] Cleaner debug information
- [ ] Documentation for all delivered actions
- [x] Global state of profile, session, event visible in Debugger.
- [x] Branding
- [ ] Custom nodes naming

#### Removals

- [x] Remove UQL Manual

### Version 0.4.1

Feature freeze. Fixes and testing.

- [ ] Review todos
- [ ] Performance tests
- [ ] Scaling test
- [ ] Unit tests
- [ ] Integration tests
- [ ] Project management: Feature list for contributors
- [ ] UX: Simplify selecting event for debugging
- [ ] Console log
- [ ] Search



### Version 0.5.0

#### Use cases

- [ ] Proof of concept for dynamic front-end loading

#### Features:
- [ ] Every time segments raises error log that error to tracardi-segment-error index - so we can see that this segment is not right. 
- [ ] Standard Error Reporting
- [ ] Tracardi user profile domain object
- [ ] Setting user and password from interface (user profile)
- [ ] Forgot password functionality
- [ ] Workflow parameters – Workflow has its own parameters that can be copied to action parameters. This allows for making workflow as a closed solution with own configuration. With this feature a ready to use workflows could be defined. 
- [ ] Reading data from external sources – use source configuration to fetch data
- [ ] If Action – Should use plain/text editor not application/json

- [ ] GraphQL Endpoint for profile fetching.
- [ ] Profiler as part of debugger
- [x] Refactor menu to take less space
- [ ] Finish manual
- [ ] Error log
- [ ] text/plain - editor in config
- [x] Editable name for node in flow


### Version 0.6.0

#### Features:
   - [ ] Scheduler


# Installation

In order to run Tracardi you must have docker installed on your linux machine. Please refer to 
docker installation manual to see how to install docker.

## Dependencies

Tracardi need elasticsearch as its backend. Please run elasticsearch single node docker before you start Tracardi. 

### Start Elasticsearch docker

```
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.13.2
```

## Start Tracardi API

Tracardi must connect to elastic. To do that we will set ELASTIC_HOST variable to your laptop's IP. 

```
docker run -p 8686:80 -e ELASTIC_HOST=http://<your-laptop-ip>:9200 tracardi/tracardi:0.5.0.rc-1
```


## Test Tracardi API

Go to http://localhost:8686/docs and see if you get the API documentation.

## Start Tracardi GUI

Building may take some time  - up to 15min.

```
git clone https://github.com/atompie/tracardi-gui.git
cd tracardi-gui/
docker build . -t tracardi-gui
docker run -p 8787:80 -e API_URL=http://127.0.0.1:8686 tracardi-gui
```

## Tracardi GUI

Open browser and go to http://127.0.0.1:8787 Login with default user admin and password admin.

# Scaling Tracardi for heavy load. 
 
TRACARDI was developed with scalability in mind. Scaling is as easy as scaling a docker container. 
No additional configuration is needed. 

# Developement tracking

TRACARDI is #buildinpublic that means that you can track and influence its development. 

Take a look at [YouTube channel](https://bit.ly/3pbdbPR) and see what Tracardi can do for you.


## Screenshots

### Browsing events

![Screenshot 1](https://github.com/atompie/tracardi/raw/0.4.0-dev/screenshots/main.png)

### Workflow of consumer data collection and enhancement 

![Workflow](https://pbs.twimg.com/media/E3WHL7nWUAA7men?format=jpg&name=large)

### Trigger rules

![Screenshot 2](https://github.com/atompie/tracardi/raw/0.4.0-dev/screenshots/main1.png)

### Editing plugins

![Screenshot 3](https://pbs.twimg.com/media/E4FqslsVEAgRS6d?format=jpg&name=large)


# Front-End

This repository contains source for tracardi backend API. You must run it with [https://github.com/atompie/tracardi-gui] 
to see the frontend. 


# Call for contributors

We are looking for contributors. Would you like to help with Tracardi development fork Tracardi or contact us at 
tracardi.cdp@gmail.com or any social platform.

# Support us

If you would like to support us please follow us on [Facebook](https://bit.ly/3uPwP5a) or [Twitter](https://bit.ly/3uVJwLJ), tag us and leave your comments. Subscribe to our [Youtube channel](https://bit.ly/3pbdbPR) to see development process and new upcoming features.

Spread the news about TRACARDI so anyone interested get to know TRACARDI.

We appreciate any help that helps make TRACARDI popular. 

# Donate

You can support us on [BOUNTY-SOURCE](https://www.bountysource.com/teams/tracardi)

# License

Tracardi is available under MIT with Common Clause license.

