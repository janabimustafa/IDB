## Rocket League
## Database
##### on RLDB.me

---

### Group Members
+++
#### Melanie Rivera
Frontend, data collection
+++
#### John O'kane
Unit testing, QA Engineer
+++
#### Alex Gonzales
Backend, API, documentation, data collection, db management
+++
#### George Weng
Frontend, visualization
+++
#### Mustafa Taleb
Sysadmin, backend, API, data collection

---

### Docker
+++
#### Easy start for developers
```bash
docker-compose build
docker-compose up -d
```
+++
#### Easy builds for production
```bash
docker-compose -f docker-compose-travis.yml build
```
---

### Servers & CI
+++
#### Servers
- Two micro instances on Google Compute Engine for dev and prod
- Database is hosted on both vms separate from the Docker workspace
- Dev site available on dev.rldb.me
- Live site available on rldb.me
+++
#### Travis
- Builds and tests latest changes and pull requests
- Pushes Docker images
  - When the build is against the dev branch, a Docker image with :dev tag is pushed
  - When the build is against the master branch, a Docker image with the :latest tag is pushed
+++
#### Watchtower
A Dockerized application to automate the deployment process
- Polls Docker hub for the latest versions of our images
- Deploys the new version, cleaning up afterwards

---

## Demonstration

---

## Rest API

---

## Unit Tests

---

### Self-Critique
+++
#### What did we do well?
- Data collection
  - 2 APIs, 1 XPath scraper for supplemental data
- Navigation
- Continuous integration
- Version control
  - 368 commits, 36 branches, 64 pull requests, 6 releases
  - Branches and pull requests
  - only 1 merge conflict ever!
+++
#### What did we learn?
- Docker
- Google Cloud Platform, expen$$$ive
- React
- Trello
- GitFlow
- Selenium
- Teamwork
+++
#### What can we do better?
- Planning and assignment of tasks
- CSS
- Trello board card labels/titles/descriptions
- Communication
+++
#### What puzzles us?
- Visualizations
- React

---

### Event4Me Critique
+++
#### What did they do well?
- Beautiful, consistent design
- 5 data sources
+++
#### What did we learn from their website?
- Load everything before displaying
+++
#### What can they do better?
- Contrast! (difficulty reading the grey on grey)
- Events with multiple artists show up as different events
- Past events still show up
+++
#### What puzzles us about their website?
- The default sorting for events
---

### Visualization

---

### Q&A