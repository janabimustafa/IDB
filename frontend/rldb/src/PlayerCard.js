import React, {Component} from 'react';

import './playerCard.css';

class PlayerCard extends Component {

    render() {
        return (
            <div className=" col-md-4 col-sm-6 text-center">
                <a href="">
                    <img className="img-rounded" src={this.props.data.image}/>
                    <h2>{this.props.data.name}</h2>
                </a>
                <div className="caption">
                    <p>Platform: {this.props.data.platform ? this.props.data.platform : "unknown"}</p>
                </div>
            </div>
        )
    }
}

export default PlayerCard;