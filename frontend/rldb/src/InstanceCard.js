import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import './instanceCard.css';

class InstanceCard extends Component {

    getRarity (rarity_num) {
        if (!rarity_num)
            return "unknown";
        var rarities = ["unknown", "common", "uncommon", "rare", "very rare", "limited", "premium", "import", "exotic", "black market"];
        return rarities[rarity_num];
    }

    getRarityColor (raw_rarity) {
        return "color-" + this.getRarity(raw_rarity);
    }

    getBorderColor (raw_rarity) {
        return "border-" + this.getRarity(raw_rarity);
    }

    upperCaseFirst(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
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
            <div className={'instance-card grow col-md-2 col-sm-4 text-center ' + this.getBorderColor(this.props.data.rarity) }>
                    <Link onClick={this.forceUpdate} to={`/${this.makePlural(this.props.data.type)}/${this.props.data.name}`}>
                        <img className="img-rounded img-item" src={this.props.data.image}  alt="rocket-league-item"/>                           
                   
                        <div className="caption">
                            <h3>{this.props.data.name}</h3>
                            <br/>
                            <p className={this.getRarityColor(this.props.data.rarity)}>{this.getRarity(this.props.data.rarity).toUpperCase()}</p>
                            <br/>
                            <p className="">Item Type: {this.upperCaseFirst(this.props.data.type)}</p>
                            <p>Release Date: {this.props.data.release_date ? this.props.data.release_date : "Unknown"}</p>
                            <p>Source: {this.props.data.source ? this.upperCaseFirst(this.props.data.source) : "Drop"}</p>
                        </div>                            
                    </Link>
            </div>
        )
    }
}

export default InstanceCard;