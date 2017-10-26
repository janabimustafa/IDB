import React, {Component} from 'react';

import './instanceCard.css';

class InstanceCard extends Component {

    render() {
        return (
            <div className=" col-md-4 col-sm-6 text-center">
                <a href="">
                    <img className="img-rounded" src={this.props.data.image}/>
                    <h2>{this.props.data.name}</h2>
                </a>
                <div className="caption">
                    <p>Rarity: {this.props.data.rarity ? this.props.data.rarity : "unknown"}</p>
                    <p>Item Type: {this.props.data.type}</p>
                    <p>Release Date: {this.props.data.release_date ? this.props.data.release_date : "unknown"}</p>
                    <p>Source: {this.props.data.source ? this.props.data.source : "unknown"}</p>
                </div>
            </div>
        )
    }
}

export default InstanceCard;