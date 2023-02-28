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

#### Meta Service

Its job is to know the status and state of all services and provide
information on such to any client.

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
  User-->>Meta: Go to Meta
  Meta-->>User: Redirects to a WebUI
  User-->>WebUI: Goes to user home page

  WebUI-->>Meta: Get/Query the less active Storage service
  Meta-->WebUI: Least used Storage

  WebUI-->>User: User's home page

  User-->>Storage: User presses "Save Post" button

```

WebUI-->>Storage: Stores post on database
Storage-->>MicroService: Creates Post
MicroService-->>WebUI: Puts post on Web for others to see 

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