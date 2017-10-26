import React, {Component} from 'react';

class InstancePage extends Component {
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

        fetch('/api/' + this.getApiType(url.split('/')[1] + "/"
        + url.split('/')[2] )), { 
            method: 'GET',
            dataType: 'json'
        }
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