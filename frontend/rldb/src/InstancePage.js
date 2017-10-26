import React, {Component} from 'react';

class InstancePage extends Component {
    constructor(props) {
        super(props);

        this.state = {
            data: []
        };
    }

    //is it better to do fetch in constructor or in componentDidMount
    componentDidMount() {
        fetch('/api' + {this.props.match.url}), { 
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

    render() {
        return (
            <div className="container text-center">
                <h1>Instance Page for {this.props.match.url}</h1>
                <p></p>
            </div>
        )
    }
}

export default InstancePage;