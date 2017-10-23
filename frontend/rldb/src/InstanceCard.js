import React, {Component} from 'react';

class InstanceCard extends Component {
    render() {
        return (
            <div>
                <h1>InstanceCard</h1>
                <h2>{this.props.name}</h2>
            </div>
        )
    }
}

export default InstanceCard;