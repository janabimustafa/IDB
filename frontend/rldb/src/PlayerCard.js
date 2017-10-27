import React, {Component} from 'react';
import {Link} from 'react-router-dom';

import './playerCard.css';

class PlayerCard extends Component {

    getPlatform (platform) {
        var platforms = ["unknown", "Steam", "Playstation", "Xbox"];
        return platforms[platform];
    } 

    render() {
        return (
            <div className=" col-md-3 col-sm-3 text-center">
                <Link to={`/${this.props.data.type}/${this.props.data.name}`}>
                    <img className="img-rounded img-player" src={this.props.data.image ? this.props.data.image : "http://via.placeholder.com/150x150"}/>
                    <h2>{this.props.data.name}</h2>
                </Link>
                <div className="caption">
                    <p>Platform: {this.getPlatform(this.props.data.platform)}</p>
                    <p>Skill Rating: {this.props.data.skill_rating}</p>
                    <p>Wins: {this.props.data.wins}</p>
                </div>
            </div>
        )
    }
}

export default PlayerCard;