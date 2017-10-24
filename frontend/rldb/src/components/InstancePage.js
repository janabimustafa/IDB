import React, {Component} from 'react';

class InstancePage extends Component {
    render() {
        return (
            <div className="container text-center">
                <h1>Instance Page for {this.props.name}</h1>
            </div>
        )
    }
}

export default InstancePage;