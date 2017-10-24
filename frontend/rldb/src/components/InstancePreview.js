import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class InstancePreview extends Component {
    render() {
        return (
            <div>
                <div className="col-md-2 col-sm-3 col-xs-6">
                    <Link to={`/crate/${this.props.name}`}>
                    <div className="panel">
                        <div className="panel-heading">
                            <h3>{this.props.name}</h3>
                        </div>
                        <div className="panel-body">
                            <img className="img-responsive" src="https://via.placeholder.com/100x100" alt={this.props.name + "Image"} />
                            <p>{this.props.value}</p>
                        </div>
                    </div>
                    </Link>
                </div> 
            </div>
        )
    }
}

export default InstancePreview;