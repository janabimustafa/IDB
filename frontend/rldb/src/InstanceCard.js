import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import './instanceCard.css';

class InstanceCard extends Component {

    getRarity (rarity_num) {
        if (!rarity_num)
            return "unknown";
        var rarities = ["unknown", "common", "uncommon", "rare", "very rare", "limted", "premium", "import", "exotic", "black market"];
        return rarities[rarity_num];
    }
    
    getApiType (type) {
        var apiTypes = {"crate" : "crates", "body":"bodies", "paint":"paints", "player":"players", "wheel":"wheels"};
        return apiTypes[type];
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
        console.log(this.props.data.type);
        return (
            <div className="col-md-4 col-sm-6 text-center">
                <Link onClick={this.forceUpdate} to={`/${this.makePlural(this.props.data.type)}/${this.props.data.name}`}>
                    <img className="img-rounded" src={this.props.data.image}/>
                    <h2>{this.props.data.name}</h2>
                </Link>
                <div className="caption">
                    <p>Rarity: { this.getRarity(this.props.data.rarity) }</p>
                    <p>Item Type: {this.props.data.type}</p>
                    <p>Release Date: {this.props.data.release_date ? this.props.data.release_date : "unknown"}</p>
                    <p>Source: {this.props.data.source ? this.props.data.source : "drop"}</p>
                </div>
            </div>
        )
    }
}

export default InstanceCard;