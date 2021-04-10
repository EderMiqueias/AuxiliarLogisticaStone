import React from 'react'

export default props => {
    const itemStyle = {
        fontSize: '22px',
        paddingLeft: "24px"
    }

    return (
        <li className="nav-item active" style={itemStyle}>
            <a className="nav-link" href="#"> <strong>{props.content}</strong> </a>
        </li>
    );
}
