import React, {Component} from 'react';

//this page just copy pasted from static instead of rewriting with react-bootstrap

class About extends Component {
  constructor(props){
    super(props);
    
    this.state = {
      commits: {
        "Musi13" : 0,
        "gweng88" : 0,
        "janabimustafa" : 0,
        "lprekon" : 0,
        "obits13" : 0,
        "total" : 0
      },
      trello: {
        "total" : 0
      },
      tests: {
        "total" : 0
      }
    };
  }

  componentDidMount(){
    fetch('https://api.github.com/repos/janabimustafa/IDB/stats/contributors', {
      method: 'GET',
      dataType: 'json'
    })
    .then(function(response) {
      return response.json()
    })
    .then(j => {
      var commits = {}

      let sum = 0;
      for (let i = 0; i < j.length; i++) {
        commits[j[i].author.login] = j[i].total;
        sum += j[i].total;
      }
      commits["total"] = sum;
      this.setState({
        commits: commits
      });
      console.log("github");
      console.log(commits);
    });
  }


  render() {
    return (
        <div className="container">
          <h1>About</h1>
          <p>We are the Supersonic Acrobatic Rocket-Powered Engineers.</p>
          <p>RocketLeagueDB (RLDB.me) is a database for most things Rocket League made for Rocket League fans.</p>
          <a href="http://docs.janabimustafa.apiary.io/">Link to Apiary API</a>
          <br></br>
          <a href="https://github.com/janabimustafa/idb">Link to GitHub Repo</a>
          <br></br>
          <a href="https://trello.com/b/tAZ12NXY/project-2">Link to Trello</a>
          <br></br>
          <a href="https://utexas.box.com/s/jy9pa6ja68ogjylym7wxg38tyg0ik5tk">Link to Technical Report</a>

          <h3>Data Sources</h3>
          <a href="http://rocketleague.wikia.com/api/v1">Rocket League Wikia</a>
          <p>The Rocket League Wikia is a fan contributed wiki page. We employ a python script to scrape each catergory and obtain all items in the category. Then, we obtain all related items for each item.</p>
          <a href="http://documentation.rocketleaguestats.com">RocketLeagueStats</a>
          <p>RocketLeagueStats is a fan-made collection of Rocket League player statistics. We use their API to obtain player information. The API returns JSON, so we use that information for the player info.</p>

          <h3>Project Info</h3>
          <p>{this.state.commits["total"]} Total Commits</p>
          <p>29 Total Issues</p>
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
              <img className="img-rounded" src="img/about/melanie.jpg"></img>
                <h2>Melanie Rivera</h2>
                <p>I am a senior in UTCS and Platinum II in Rocket League Competitive Standard.</p>
                <p>Responsibilities: technical writer, trello manager, front-end.</p>
                <p>{this.state.commits["obits13"]} Commits</p>
                <p>9 Issues</p>
                <p>0 Unit Tests</p>
            </div>
            <div className="col-md-4 text-center">
              <img className="img-rounded" src="img/about/mustafa.jpeg"></img>
                <h2>Mustafa Taleb</h2>
                <p>I am a senior in UTCS and Diamond II in Rocket League Competitive Standard.</p>
                <p>Responsibilities: sysadmin, back-end, front-end, API</p>
                <p>{this.state.commits["janabimustafa"]} Commits</p>
                <p>8 Issues</p>
                <p>0 Unit Tests</p>
            </div>
            <div className="col-md-4 text-center">
              <img className="img-rounded" src="img/about/alex.jpg"></img>
                <h2>Alex Gonzales</h2>
                <p>I am a senior in UTCS and can count on two hands the number of games of Rocket League I have played.</p>
                <p>Responsibilities: Back-End, API, Documentation.</p>
                <p>{this.state.commits["Musi13"]} Commits</p>
                <p>6 Issues</p>
                <p>0 Unit Tests</p>
            </div>
          </div>

          <div className="row">
            <div className="col-md-2"></div>
            <div className="col-md-4 text-center">
              <img className="img-rounded" src="img/about/george.jpg"></img>
                <h2>George Weng</h2>
                <p>I'm a sophomore in UTCS. That's all from me!</p>
                <p>Responsibilities: front-end</p>
                <p>{this.state.commits["gweng88"]} Commits</p>
                <p>5 Issues</p>
                <p>0 Unit Tests</p>
            </div>
            <div className="col-md-4 text-center">
              <img className="img-rounded" src="img/about/john.jpg"></img>
                <h2>John Okane</h2>
                <p>UTCS Half-Senior (what do you call it when you're graduating a semester early, rather than late, anyway?!). I used to be a big rocket league player "back in the day".</p>
                <p>Responsibilities: Back-end, API, comedic relief</p>
                <p>{this.state.commits["lprekon"]} Commits</p>
                <p>3 Issues</p>
                <p>19 Unit Tests</p>
            </div>
            <div className="col-md-2"></div>
          </div>
        </div>
    )
  }
}
export default About;