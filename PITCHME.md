# Rocket League
# Database
##### on RLDB.me

---

### Group Members
- John O'kane
  - unit testing, QA
- Melanie Rivera
  - design, data collection
- Alex Gonzales
  - backend, API, documentation, data collection, db management
- George Weng
  - frontend
- Mustafa Taleb
  - sysadmin, backend, API, data collection

---

### Tools?

---

## Demonstration

---

### Self-Critique
- What did we do well?
  - data collection
  - navigation
  - continuous integration
- What did we learn?
  - Docker, a necessary evil
  - Google Cloud Platform, expensive
- What can we do better?
  - planning and assignment of tasks
  - CSS
- What puzzles us?
  - visualizations

---

### Event4Me Critique
- What did they do well?
  - beautiful, consistent design
  - 5 data sources
- What did we learn from their website?
  - database was slow for everyone
  - load everything before displaying
- What can they do better?
  - contrast! (difficulty reading the grey on grey)
- What puzzles us about their website?

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

### Q&A