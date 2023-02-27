# Requirements Doc for ClapTrap

## Microservice Design

* All need a local DB for any permenant data storage, persistent data
* API's are needed connect Microservices together and provide transfer of information
* The code that implements this microservice's goal

Graphically:

```
+----- Microservice A -----+
|                          |
| +-- Logic --+            >-- API 1
| |    ...    |            |
| +-v---------+            }-- API 2
|   |                      |
|   |    +-- DB --+        ]-- API 3
|   -----<   ...  |        |
|        +--------+        |
+--------------------------+
```

### Basics of a Microservice

#### Benefits

* Separation of Concerns
* Failsafe / Redundancy
* Everything is completely Modular (coding language, ect.)

### Services in ClapTrap

#### Frontend: UI

We shall have a service to handle the user interaction.

Tech: `bottle.py` is our main tool here

#### STORAGE SERVICE

#### 

#### OTHER SERVICE ??


## Technologies to be Used

### Python

Python shall be our language of implementation.

### SQLite

SQLite will be our DB.

### Bottle

Bottle will be our web UI and routing.

## Use Cases

### Create Post

```mermaid
sequenceDiagram
  User->>+WebUI: Go to web site
  WebUI->>-User: Present user's "timeline"
  User-->>WebUI: Creates a Post
  WebUI-->>Database: Stores post on database
  Database-->>MicroService: Creates Post
  MicroService-->>WebUI: Puts post on Web for others to see 
```

### Rate a post

```mermaid
sequenceDiagram
    User->>-WebUI: Go to website
    WebUI->>-User: Present user's "timeline"
```

### Comment on a post

```mermaid
    sequenceDiagram
```

### Read someone else's posts

### Repost someone else's post