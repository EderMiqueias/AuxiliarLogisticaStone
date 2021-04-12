import React from 'react';

 const Legend = (props) => {
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

export default Legend;
