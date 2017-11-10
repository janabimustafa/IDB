import React, {Component} from 'react';

import LoadingOverlay from './LoadingOverlay';

//this page just copy pasted from static instead of rewriting with react-bootstrap

class About extends Component {
  constructor(props){
    super(props);
    
    this.state = {
      data: null
    };
  }

  componentDidMount(){
    fetch('/api/meta/about', {
      method: 'GET',
      dataType: 'json'
    })
    .then(function(response) {
      return response.json()
    })
    .then(j => {
      console.log(j);
      this.setState({
        data: j
      });
    });
  }


  render() {    
    if (this.state.data === null)
      return (<LoadingOverlay />)
    return (
        <div className="container">
          <hr/>  
          <h1>About</h1>
          <hr/>  

          <br/>
          <h3>We are the Supersonic Acrobatic Rocket-Powered Engineers.</h3>
          <h3>RocketLeagueDB (RLDB.me) is a database for most things Rocket League for Rocket League fans.</h3>
          <br/>
          <a className="source-link" href="http://docs.janabimustafa.apiary.io/">Link to Apiary API</a>
          <br></br>
          <a className="source-link" href="https://github.com/janabimustafa/idb">Link to GitHub Repo</a>
          <br></br>
          <a className="source-link" href="https://trello.com/b/XG6xjh7g/project-4">Link to Trello</a>
          <br></br>
          <a className="source-link" href="https://utexas.box.com/s/yonyad8ubdccb7hvadxbmmdso1nnhquf">Link to Technical Report</a>
          <br></br>
          <a className="source-link" href="https://utexas.box.com/s/o9m3o9dejlj60rte192f86clga005uzi">Link to UML Diagram (UT Box)</a>

          <h3>Data Sources</h3>
          <div className="row">
            <div className="source-card col-md-3">
              <div className="source-image-container">        
                <img className="source-image" src="https://vignette.wikia.nocookie.net/rocketleague/images/b/b8/Wiki-welcome.png/revision/latest?cb=20170913175236" alt="Welcome to the Rocket League Wiki"/>
              </div>
              <br/><br/>
              <a className="source-link" href="http://rocketleague.wikia.com/api/v1">Rocket League Wikia</a>
              <br/><br/>
              <p>The Rocket League Wikia is a fan contributed wiki page. We employ a python script to scrape each catergory and obtain all items in the category. Then, we obtain all related items for each item.</p>    
            </div>
            <div className="source-card col-md-3">
              <div className="source-image-container">
                <img className="source-image" src="https://rocketleaguestats.com/assets/img/logo/rls_logotype_fullcolor_light.png" alt="RocketLeague Stats logo"/>
              </div>
              <br/><br/>
              <a className="source-link" href="http://documentation.rocketleaguestats.com">RocketLeagueStats</a>
              <br/><br/>
              <p>RocketLeagueStats is a fan-made collection of Rocket League player statistics. We use their API to obtain player information. The API returns JSON, so we use that information for the player info.</p>
            </div>
            <div className="source-card col-md-3">
              <div className="source-image-container">
                <img className="source-image" src="https://rocket-league.com/assets/images/logos/rocket-league-garage-footer.svg" alt="RocketLeague Stats logo"/>
              </div>
              <br/><br/>
              <a className="source-link" href="https://rocket-league.com/items">Rocket League Garage</a>
              <br/><br/>
              <p>Rocket League Garage is a fan-made Rocket League site containing the names and images of most in-game items. We scrape the site using X-Path to obtain the images and names of the items to add them to our database.</p>
            </div>
          </div>

          <h3>Project Info</h3>
          <p>{this.state.data["num_commits"]} Total Commits</p>
          <p>{this.state.data["num_issues"]} Total Issues</p>
          <p>19 Total Unit Tests</p>

          <h3>Project Tools</h3>
          <p>Git: A version control system.</p>
          <p>Docker: A software container platform.</p>
          <p>Flask: A web framework.</p>
          <p>React: A JavaScript library for building UIs.</p>
          <p>Traefik: A modern reverse proxy and load balancer.</p>
          <p>Apiary: A platform for API design, development, and documentation.</p>
          <p>Boostrap: A framework for developing UIs.</p>
          <p>Slack: A communication platform.</p>
          <p>Trello: A web-based project management platform.</p>

          <h3>Our Team</h3>
          <div className="row">
            <div className="col-md-4 text-center">
              <img className="img-rounded" src="img/about/melanie.jpg"  alt="contributor"></img>
                <h2>Melanie Rivera</h2>
                <p>I am a senior in UTCS and Platinum II in Rocket League Competitive Standard.</p>
                <p>Responsibilities: technical writer, trello manager, front-end.</p>
                <p>{this.state.data["commits"]["obits13"]} Commits</p>
                <p>{this.state.data["issues"]['Melanie L Rivera']} Issues</p>
                <p>0 Unit Tests</p>
            </div>
            <div className="col-md-4 text-center">
              <img className="img-rounded" src="img/about/mustafa.jpeg" alt="contributor"></img>
                <h2>Mustafa Taleb</h2>
                <p>I am a senior in UTCS and Diamond II in Rocket League Competitive Standard.</p>
                <p>Responsibilities: sysadmin, back-end, front-end, API</p>
                <p>{this.state.data['commits']["janabimustafa"]} Commits</p>
                <p>{this.state.data["issues"]["Mustafa Taleb"]} Issues</p>
                <p>4 Unit Tests</p>
            </div>
            <div className="col-md-4 text-center">
              <img className="img-rounded" src="img/about/alex.jpg" alt="contributor"></img>
                <h2>Alex Gonzales</h2>
                <p>I am a senior in UTCS and can count on two hands the number of games of Rocket League I have played.</p>
                <p>Responsibilities: Back-End, API, Documentation.</p>
                <p>{this.state.data['commits']["Musi13"]} Commits</p>
                <p>{this.state.data["issues"]["Alex Gonzales"]} Issues</p>
                <p>0 Unit Tests</p>
            </div>
          </div>

          <div className="row">
            <div className="col-md-2"></div>
            <div className="col-md-4 text-center">
              <img className="img-rounded" src="img/about/george.jpg" alt="contributor"></img>
                <h2>George Weng</h2>
                <p>I'm a sophomore in UTCS. That's all from me!</p>
                <p>Responsibilities: front-end</p>
                <p>{this.state.data['commits']["gweng88"]} Commits</p>
                <p>{this.state.data["issues"]["George Weng"]} Issues</p>
                <p>0 Unit Tests</p>
            </div>
            <div className="col-md-4 text-center">
              <img className="img-rounded" src="img/about/john.jpg" alt="contributor"></img>
                <h2>John Okane</h2>
                <p>UTCS Half-Senior (what do you call it when you're graduating a semester early, rather than late, anyway?!). I used to be a big rocket league player "back in the day".</p>
                <p>Responsibilities: Back-end, API, comedic relief</p>
                <p>{this.state.data['commits']["lprekon"]} Commits</p>
                <p>{this.state.data["issues"]["John O'Kane"]} Issues</p>
                <p>19 Unit Tests</p>
            </div>
            <div className="col-md-2"></div>
          </div>
        </div>
    )
  }
}
export default About;