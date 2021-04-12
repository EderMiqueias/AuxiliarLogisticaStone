import React from 'react'

const ItemNavbar = props => {
    const itemStyle = {
        fontSize: '22px',
        paddingLeft: "24px"
    }

    return (
        <li className="nav-item active" style={itemStyle}>
            <a className="nav-link" href={props.src}> <strong>{props.content}</strong> </a>
        </li>
    );
}

export default ItemNavbar;
