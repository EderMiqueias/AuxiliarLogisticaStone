import React from 'react';

export default (props) => {
    return (
        <div className="legend">
            <div
                className="blockP"
                style={{ backgroundColor: props.color }}>
            </div>
            <p>{props.text}</p>
        </div>
    )
}