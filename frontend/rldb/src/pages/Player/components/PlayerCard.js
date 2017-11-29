import React, {Component} from 'react';
import {Link} from 'react-router-dom';

import './playerCard.css';

class PlayerCard extends Component {

    getPlatform (platform) {
        var platforms = ["unknown", "Steam", "Playstation", "Xbox"];
        return platforms[platform];
    } 
    makePlural (noun) {
        var lastChar = noun.slice(-1)
        console.log('last char in ' + noun + ' is ' + lastChar);
        if (lastChar === 'y')
            return noun.replace('y', 'ies');
        else
            return noun + 's';
    }
    render() {
        return (
            <div className="player-card grow col-md-2 col-sm-4 text-center">
                <Link to={`/${this.makePlural(this.props.data.type)}/${this.props.data.name}`}>
                    <img className="img-rounded img-player" src={this.props.data.image ? this.props.data.image : "http://via.placeholder.com/150x150"}  alt="player"/>
                    <h2>{this.props.data.name}</h2>
                </Link>
                <br/>
                <div className="caption">
                    <p>{this.getPlatform(this.props.data.platform)}</p>
                    <br/>
                    <p>Skill Rating: {this.props.data.skill_rating}</p>
                    <p>Wins: {this.props.data.wins}</p>
                </div>
            </div>
        )
    }
}

export default PlayerCard;