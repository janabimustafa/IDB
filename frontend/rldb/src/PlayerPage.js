import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class PlayerPage extends Component {
    constructor(props) {
        super(props);

        this.state = {
            data: []
        };
    }

    getApiType (type_name) {
        var apiTypes = {"crate":"crates", "paint":"paints", "body":"bodies","player":"players"};
        return apiTypes[type_name];
    } 

    //is it better to do fetch in constructor or in componentDidMount
    componentDidMount() {
        var url = this.props.match.url

        fetch('/api/' + this.getApiType(url.split('/')[1]) + "/" + url.split('/')[2] , { 
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

    getPlatform (platform) {
        var platforms = ["unknown", "Steam", "Playstation", "Xbox"];
        return platforms[platform];
    } 

    render() {
        return (
            <div className="container">
                <h1>{this.state.data.name}</h1>
                <div className="row">
                    <div className="col-md-4">
                        <img className="img-rounded" src={this.state.data.image ? this.state.data.image : "http://via.placeholder.com/300x300"}/>
                    </div>
                    <div className="col-md-8 text-center">
                        <h3>Platform: {this.getPlatform(this.state.data.platform)}</h3>
                        <h3>Skill Rating: {this.state.data.skill_rating}</h3>
                        <h3>Wins: {this.state.data.wins}</h3>
                        <Link to={'/'+ this.props.match.url.split('/')[1]}>
                        <h3>Go back.</h3>
                        </Link>
                    </div>
                <p></p>
                </div>
            </div>
        )
    }
}

export default PlayerPage;