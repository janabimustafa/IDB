## Rocket League
## Database
##### on RLDB.me

---

### Group Members
+++
#### John O'kane
Unit testing, QA
+++
#### Melanie Rivera
Design, data collection
+++
#### Alex Gonzales
Backend, API, documentation, data collection, db management
+++
#### George Weng
Frontend
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

### Self-Critique
+++
#### What did we do well?
- Data collection
- Navigation
- Continuous integration
+++
#### What did we learn?
- Docker
- Google Cloud Platform, expensive
+++
#### What can we do better?
- Planning and assignment of tasks
- CSS
+++
#### What puzzles us?
- Visualizations

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


### Q&A