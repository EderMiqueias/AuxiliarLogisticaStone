import React from 'react'

import ItemNavbar from './ItemNavbar'
import navLogo from '../../assets/images/logo_stone.png'

const Navbar = props => {
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <a className="navbar-brand" href="/">
                <img src={navLogo} height="30" alt="" />
            </a>
            <div className="collapse navbar-collapse" id="navbarSupportedContent">
                <ul className="navbar-nav mr-auto">
                    <ItemNavbar content="Polos" src="/polos"/>
                </ul>
            </div>
        </nav>
    );
}

export default Navbar;
