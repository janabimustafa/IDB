import React, {Component} from 'react';

import './LoadingOverlay.css';

class LoadingOverlay extends Component {

    render() {
        return (
            <div className="spinner">
                <div className="ball ball-1"></div>
                <div className="ball ball-2"></div>
                <div className="ball ball-3"></div>
                <div className="ball ball-4"></div>
            </div>
        )
    }
}

export default LoadingOverlay;